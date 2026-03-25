import os
import sys
import yaml
import requests
import re
import time
from datetime import datetime

# ==========================================
# 1. 飞书数据读取与图片下载引擎
# ==========================================
class FeishuReader:
    def __init__(self, config_file="feishu_config.yml"):
        self.config_file = config_file
        # 建议在终端 export，或者在此硬编码（仅限私有仓库）
        self.app_id = os.environ.get("FEISHU_APP_ID", "cli_a924e03710219cee")
        self.app_secret = os.environ.get("FEISHU_APP_SECRET", "5klcCSICBJWjCHn9ngKJH4imARMnptWk")

        if not self.app_id or not self.app_secret:
            print("❌ 错误：未找到 FEISHU_APP_ID 或 FEISHU_APP_SECRET 环境变量！")
            sys.exit(1)
            
        self.app_token = self._load_app_token()
        self.tenant_access_token = None
        self.base_url = "https://open.feishu.cn/open-apis"
        self.table_map = {} 
        
        # 🌟 关键：禁用代理配置，防止 Connection Reset
        self.proxies = {"http": None, "https": None}

    def _load_app_token(self):
        if not os.path.exists(self.config_file):
            print(f"❌ 找不到配置: {self.config_file}")
            sys.exit(1)
        with open(self.config_file, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f).get('app_token')

    def authenticate(self):
        """获取 Tenant Access Token 授权 (带异常处理)"""
        print("⏳ [1/4] 正在请求飞书 API 授权...")
        url = f"{self.base_url}/auth/v3/tenant_access_token/internal"
        
        try:
            res_obj = requests.post(
                url, 
                json={"app_id": self.app_id, "app_secret": self.app_secret},
                proxies=self.proxies, # 强制直连
                timeout=10
            )
            res = res_obj.json()
            if res.get("code") == 0:
                self.tenant_access_token = res.get("tenant_access_token")
                print("✅ 授权成功！")
            else:
                print(f"❌ 授权失败: {res.get('msg')}")
                sys.exit(1)
        except Exception as e:
            print("\n" + "!"*40)
            print("❌ 网络连接异常 (Connection Error)")
            print(f"错误详情: {e}")
            print("💡 建议: 请尝试关闭 VPN、梯子或校园网代理后再运行。")
            print("!"*40)
            sys.exit(1)

    def _get_headers(self):
        return {
            "Authorization": f"Bearer {self.tenant_access_token}",
            "Content-Type": "application/json; charset=utf-8"
        }

    def load_table_map(self):
        print("⏳ [2/4] 获取数据表结构...")
        url = f"{self.base_url}/bitable/v1/apps/{self.app_token}/tables"
        try:
            res = requests.get(url, headers=self._get_headers(), proxies=self.proxies).json()
            if res.get("code") == 0:
                tables = res["data"]["items"]
                for t in tables:
                    self.table_map[t["name"]] = t["table_id"]
                print(f"📊 成功找到 {len(self.table_map)} 个数据表。")
            else:
                print(f"❌ 获取表格列表失败: {res.get('msg')}")
                sys.exit(1)
        except Exception as e:
            print(f"❌ 获取表结构时网络报错: {e}")
            sys.exit(1)

    def download_media(self, file_token, save_path):
        if not file_token: return False
        if os.path.exists(save_path): return True

        url = f"{self.base_url}/drive/v1/medias/{file_token}/download"
        try:
            res = requests.get(url, headers=self._get_headers(), proxies=self.proxies, timeout=30)
            if res.status_code == 200:
                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                with open(save_path, 'wb') as f:
                    f.write(res.content)
                return True
        except Exception as e:
            print(f"⚠️ 图片下载网络抖动 (Token: {file_token[:5]}...): {e}")
        return False

    def sanitize_filename(self, name):
        if not name: return "default"
        safe_name = re.sub(r'[^a-zA-Z0-9_\-]', '', str(name).replace(' ', '_')).lower()
        return safe_name if safe_name else "default"

    def fetch_records(self, table_name):
        if table_name not in self.table_map: return []
        table_id = self.table_map[table_name]
        url = f"{self.base_url}/bitable/v1/apps/{self.app_token}/tables/{table_id}/records"
        
        all_records = []
        has_more = True
        page_token = ""

        print(f"\n📥 [3/4] 拉取表格记录：{table_name}")
        while has_more:
            params = {"page_size": 100, "page_token": page_token}
            try:
                res = requests.get(url, headers=self._get_headers(), params=params, proxies=self.proxies).json()
                if res.get("code") == 0:
                    data = res["data"]
                    items = data.get("items", [])
                    for item in items:
                        record = item["fields"]
                        # 处理 Avatar 和 Image 逻辑保持不变...
                        for field_key in ["Avatar", "Image"]:
                            media_list = record.get(field_key)
                            if media_list and isinstance(media_list, list) and len(media_list) > 0:
                                f_token = media_list[0].get('file_token')
                                if f_token:
                                    slug = self.sanitize_filename(record.get('Name_en') or record.get('Title_en') or "asset")
                                    ext = os.path.splitext(media_list[0].get('name', '.jpg'))[1]
                                    folder = "team" if field_key == "Avatar" else "papers"
                                    save_name = f"{slug}_{f_token[:8].lower()}{ext}"
                                    save_path = f"assets/images/{folder}/{save_name}"
                                    if self.download_media(f_token, save_path):
                                        record[f'local_{field_key.lower()}_path'] = f"/{save_path}"
                        all_records.append(record)
                    has_more = data.get("has_more", False)
                    page_token = data.get("page_token", "")
                else:
                    break
            except Exception as e:
                print(f"❌ 分页拉取数据时报错: {e}")
                break
        return all_records

# ==========================================
# 2. 数据转换器 (保持不变)
# ==========================================
class DataConverter:
    @staticmethod
    def _get_text(field): return str(field).strip() if field else ""
    @staticmethod
    def _get_option(field): return field.get("text", "") if isinstance(field, dict) else str(field)
    @staticmethod
    def _get_link(field): return field.get("link", "") if isinstance(field, dict) else str(field)

    @classmethod
    def convert_team(cls, records):
        yaml_list = []
        for r in records:
            item = {
                "name": {"zh": cls._get_text(r.get("Name_zh")), "en": cls._get_text(r.get("Name_en"))},
                "group_id": cls._get_option(r.get("Group_ID")),
                "rank": int(r.get("Rank") if r.get("Rank") else 99),
                "title": {"zh": cls._get_text(r.get("Title_zh")), "en": cls._get_text(r.get("Title_en"))},
                "avatar": r.get("local_avatar_path", ""),
                "email": cls._get_text(r.get("Email")),
                "bio": {"zh": cls._get_text(r.get("Bio_zh")), "en": cls._get_text(r.get("Bio_en"))},
                "links": {
                    "homepage": cls._get_link(r.get("Link_Homepage")),
                    "github": cls._get_link(r.get("Link_GitHub")),
                    "scholar": cls._get_link(r.get("Link_Scholar"))
                }
            }
            yaml_list.append(item)
        return sorted(yaml_list, key=lambda x: x.get("rank", 99))

    @classmethod
    def convert_publications(cls, records):
        yaml_list = []
        for r in records:
            item = {
                "title": {"zh": cls._get_text(r.get("Title_zh")), "en": cls._get_text(r.get("Title_en"))},
                "authors": cls._get_text(r.get("Authors")),
                "venue": cls._get_text(r.get("Venue")),
                "year": int(r.get("Year") if r.get("Year") else 2024),
                "highlight": cls._get_text(r.get("Highlight")),
                "image": r.get("local_image_path", ""),
                "links": {"paper": cls._get_link(r.get("Link_Paper")), "code": cls._get_link(r.get("Link_Code"))}
            }
            yaml_list.append(item)
        return sorted(yaml_list, key=lambda x: x.get("year", 0), reverse=True)

    @classmethod
    def convert_research(cls, records):
        yaml_list = []
        for r in records:
            item = {
                "icon": cls._get_text(r.get("Icon")),
                "title": {"zh": cls._get_text(r.get("Title_zh")), "en": cls._get_text(r.get("Title_en"))},
                "description": {"zh": cls._get_text(r.get("Desc_zh")), "en": cls._get_text(r.get("Desc_en"))},
                "image": r.get("local_image_path", "")
            }
            yaml_list.append(item)
        return yaml_list

    @classmethod
    def convert_news(cls, records):
        yaml_list = []
        for r in records:
            timestamp = r.get("Date")
            date_str = datetime.fromtimestamp(timestamp / 1000).strftime('%Y.%m') if timestamp else ""
            item = {
                "date": date_str,
                "title": {"zh": cls._get_text(r.get("Title_zh")), "en": cls._get_text(r.get("Title_en"))},
                "link": cls._get_link(r.get("Link"))
            }
            yaml_list.append(item)
        return sorted(yaml_list, key=lambda x: x.get("date", ""), reverse=True)

# ==========================================
# 3. 核心执行入口
# ==========================================
if __name__ == "__main__":
    print("="*60)
    print("🚀 LV Group - 飞书数据同步引擎 (Final Proxy-Fixed Version)")
    print("="*60)

    reader = FeishuReader()
    reader.authenticate()
    reader.load_table_map()
    
    sync_tasks = [
        {"table": "团队成员", "func": DataConverter.convert_team, "file": "_data/team.yml", "key": "avatar"},
        {"table": "学术论文", "func": DataConverter.convert_publications, "file": "_data/publications.yml", "key": "image"},
        {"table": "研究方向", "func": DataConverter.convert_research, "file": "_data/research.yml", "key": "image"},
        {"table": "新闻动态", "func": DataConverter.convert_news, "file": "_data/news.yml", "key": None}
    ]
    
    os.makedirs("_data", exist_ok=True)
    
    for t in sync_tasks:
        raw_records = reader.fetch_records(t["table"])
        if not raw_records: continue
        
        filtered = [r for r in raw_records if "必填" not in str(r.get("Name_zh", "")) and "示例" not in str(r.get("Name_zh", ""))]
        clean_data = t["func"](filtered)
        
        if t["key"]:
            print(f"\n🔍 [{t['table']}] 资产校验清单：")
            for item in clean_data[:3]:
                name = item.get("name", {}).get("en") or item.get("title", {}).get("en") or "N/A"
                print(f"   ✅ {name.ljust(20)} -> {item.get(t['key'])}")

        with open(t["file"], "w", encoding="utf-8") as f:
            f.write(f"# Auto-generated from Feishu Bitable: {t['table']}\n")
            yaml.dump(clean_data, f, allow_unicode=True, sort_keys=False, indent=2, default_flow_style=False)
        print(f"    💾 文件更新成功: {t['file']}")

    print("\n" + "="*60)
    print("🎉 同步大功告成！")
    print("="*60)