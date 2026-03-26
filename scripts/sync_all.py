import os
import sys
import yaml
import requests
import re
import glob
from datetime import datetime

# ==========================================
# 1. 飞书数据读取与图片下载引擎
# ==========================================
class FeishuReader:
    def __init__(self, config_file="feishu_config.yml"):
        """初始化读取器，加载配置和凭证"""
        self.config_file = config_file
        # ⚠️ 优先从环境变量获取秘钥，防止代码泄露
        self.app_id = os.environ.get("FEISHU_APP_ID")
        self.app_secret = os.environ.get("FEISHU_APP_SECRET")

        if not self.app_id or not self.app_secret:
            print("❌ 错误：未找到 FEISHU_APP_ID 或 FEISHU_APP_SECRET 环境变量！")
            sys.exit(1)
            
        self.app_token = self._load_app_token()
        self.tenant_access_token = None
        self.base_url = "https://open.feishu.cn/open-apis"
        self.table_map = {} 
        self.proxies = {"http": None, "https": None}

    def _load_app_token(self):
        if not os.path.exists(self.config_file):
            print(f"❌ 找不到配置: {self.config_file}")
            sys.exit(1)
        with open(self.config_file, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f).get('app_token')

    def authenticate(self):
        print("⏳ [1/4] 正在请求飞书 API 授权...")
        url = f"{self.base_url}/auth/v3/tenant_access_token/internal"
        try:
            res_obj = requests.post(
                url, 
                json={"app_id": self.app_id, "app_secret": self.app_secret},
                proxies=self.proxies,
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
            print(f"❌ 网络连接异常: {e}")
            sys.exit(1)

    def _get_headers(self):
        return {
            "Authorization": f"Bearer {self.tenant_access_token}",
            "Content-Type": "application/json; charset=utf-8"
        }

    def load_table_map(self):
        print("⏳ [2/4] 获取数据表结构...")
        url = f"{self.base_url}/bitable/v1/apps/{self.app_token}/tables"
        res = requests.get(url, headers=self._get_headers(), proxies=self.proxies).json()
        if res.get("code") == 0:
            for t in res["data"]["items"]:
                self.table_map[t["name"]] = t["table_id"]
            print(f"📊 成功找到 {len(self.table_map)} 个数据表。")

    def download_media(self, download_url, save_path):
        """核心下载逻辑：直接使用带权限的 url 避免 400 错误"""
        if not download_url: return False
        try:
            print(f"      ⬇️ 下载图片: {os.path.basename(save_path)} ...", end="", flush=True)
            res = requests.get(download_url, headers=self._get_headers(), proxies=self.proxies, timeout=30)
            if res.status_code == 200:
                with open(save_path, 'wb') as f:
                    f.write(res.content)
                print(" [成功]")
                return True
            else:
                print(f" [失败: HTTP {res.status_code}]")
        except Exception as e:
            print(f" [网络抖动: {e}]")
        return False

    def sync_unique_media(self, file_token, download_url, slug, folder, original_filename):
        """去重与清理管理器"""
        if not file_token or not download_url: return ""
        
        ext = os.path.splitext(original_filename)[1].lower()
        if not ext: ext = ".jpg"
        
        token_suffix = file_token[:8].lower()
        save_name = f"{slug}_{token_suffix}{ext}"
        save_dir = f"assets/images/{folder}"
        save_path = f"{save_dir}/{save_name}"
        
        os.makedirs(save_dir, exist_ok=True)

        if os.path.exists(save_path):
            return f"/{save_path}"
            
        old_files = glob.glob(f"{save_dir}/{slug}_*.*")
        for old_file in old_files:
            try:
                os.remove(old_file)
                print(f"      🗑️ 清理旧图: {os.path.basename(old_file)}")
            except OSError:
                pass
                
        if self.download_media(download_url, save_path):
            return f"/{save_path}"
            
        return ""

    def sanitize_filename(self, name):
        if not name: return "default"
        return re.sub(r'[^a-zA-Z0-9_\-]', '', str(name).strip().replace(' ', '_')).lower()

    def fetch_records(self, table_name):
        if table_name not in self.table_map: return []
        table_id = self.table_map[table_name]
        url = f"{self.base_url}/bitable/v1/apps/{self.app_token}/tables/{table_id}/records"
        
        all_records = []
        has_more = True
        page_token = ""

        print(f"\n📥 [3/4] 拉取与处理：{table_name}")
        
        # 🌟 动态路由配置：告诉脚本去哪个字段找图片，存到哪里，前缀怎么取
        media_routes = {
            "团队成员": {"field": "Avatar", "folder": "team", "slug_key": "Name_en", "is_long_title": False},
            "学术论文": {"field": "Image", "folder": "papers", "slug_key": "Title_en", "is_long_title": True},
            "研究方向": {"field": "Image", "folder": "research", "slug_key": "Title_en", "is_long_title": False}
        }
        
        route = media_routes.get(table_name)

        while has_more:
            params = {"page_size": 100, "page_token": page_token}
            res = requests.get(url, headers=self._get_headers(), params=params, proxies=self.proxies).json()
            if res.get("code") == 0:
                data = res["data"]
                for item in data.get("items", []):
                    record = item["fields"]
                    
                    # 只有当前表配置了图片路由，才进行下载处理
                    if route:
                        field_name = route["field"]
                        media_data = record.get(field_name)
                        
                        if media_data and isinstance(media_data, list) and len(media_data) > 0:
                            file_token = media_data[0].get('file_token')
                            download_url = media_data[0].get('url') # 带权限校验的 URL
                            original_name = media_data[0].get('name', '')
                            
                            # 生成干净的标识前缀
                            raw_slug_str = str(record.get(route["slug_key"], ""))
                            if route["is_long_title"]:
                                # 论文标题太长，只取前 3 个单词作为文件名一部分
                                raw_slug_str = "_".join(raw_slug_str.split()[:3])
                                
                            slug = self.sanitize_filename(raw_slug_str)
                            
                            local_path = self.sync_unique_media(file_token, download_url, slug, route["folder"], original_name)
                            if local_path:
                                record[f'local_{field_name.lower()}_path'] = local_path

                    all_records.append(record)
                has_more = data.get("has_more", False)
                page_token = data.get("page_token", "")
            else:
                break
        return all_records

# ==========================================
# 2. 全量数据清洗与转换器
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
                "role": {"zh": cls._get_text(r.get("Role_zh")), "en": cls._get_text(r.get("Role_en"))},
                "avatar": r.get("local_avatar_path", ""), # 映射本地图片
                "bio": {"zh": cls._get_text(r.get("Bio_zh")), "en": cls._get_text(r.get("Bio_en"))},
                "email": cls._get_text(r.get("Email")),
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
                "image": r.get("local_image_path", ""), # 映射本地图片
                "abstract": {"zh": cls._get_text(r.get("Abstract_zh")), "en": cls._get_text(r.get("Abstract_en"))},
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
                "image": r.get("local_image_path", "") # 映射本地图片
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
    print("🚀 LV Group - 飞书全量数据智能同步引擎 (防 400 + 自动清理)")
    print("="*60)

    reader = FeishuReader()
    reader.authenticate()
    reader.load_table_map()
    
    # 全量同步任务配置
    sync_tasks = [
        {"table": "团队成员", "func": DataConverter.convert_team, "file": "_data/team.yml", "key": "avatar"},
        {"table": "学术论文", "func": DataConverter.convert_publications, "file": "_data/publications.yml", "key": "image"},
        {"table": "研究方向", "func": DataConverter.convert_research, "file": "_data/research.yml", "key": "image"},
        {"table": "新闻动态", "func": DataConverter.convert_news, "file": "_data/news.yml", "key": None}
    ]
    
    os.makedirs("_data", exist_ok=True)
    
    print("\n[4/4] 转换数据并写入 YAML 文件...")
    for t in sync_tasks:
        raw_records = reader.fetch_records(t["table"])
        if not raw_records: continue
        
        # 🌟 核心修改：跳过第 1 行（索引 0）的示例/占位符，直接从第 2 行（索引 1）开始读取
        filtered = raw_records[1:] if len(raw_records) > 1 else []
        
        clean_data = t["func"](filtered)
        
        # 打印资产映射状态 (如果该表有图片字段)
        if t["key"]:
            print(f"\n🔍 [{t['table']}] 媒体资产映射：")
            for item in clean_data:
                # 获取名称
                name = item.get("name", {}).get("en") or item.get("title", {}).get("en") or "Unknown"
                # 如果论文标题太长，截断显示
                display_name = (name[:20] + '..') if len(name) > 20 else name
                # 获取路径
                path = item.get(t["key"])
                status = "✅" if path else "⚠️ 未配图"
                print(f"   {status} {display_name.ljust(22)} -> {path}")

        # 写入 Jekyll 的 Data 文件
        with open(t["file"], "w", encoding="utf-8") as f:
            f.write(f"# Auto-generated from Feishu Bitable: {t['table']}\n")
            f.write(f"# Sync Time: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
            yaml.dump(clean_data, f, allow_unicode=True, sort_keys=False, indent=2, default_flow_style=False)
            
        print(f"    💾 数据已更新: {t['file']}")

    print("\n" + "="*60)
    print("🎉 全量同步大功告成！代码已支持所有的图文数据！")
    print("="*60)