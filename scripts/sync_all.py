import os
import sys
import yaml
import requests
import re
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

    def _load_app_token(self):
        if not os.path.exists(self.config_file):
            print(f"❌ 找不到配置: {self.config_file}")
            sys.exit(1)
        with open(self.config_file, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f).get('app_token')

    def authenticate(self):
        print("⏳ [1/4] 正在请求飞书 API 授权...")
        url = f"{self.base_url}/auth/v3/tenant_access_token/internal"
        res = requests.post(url, json={"app_id": self.app_id, "app_secret": self.app_secret}).json()
        if res.get("code") == 0:
            self.tenant_access_token = res.get("tenant_access_token")
            print("✅ 授权成功！")
        else:
            print(f"❌ 授权失败: {res.get('msg')}")
            sys.exit(1)

    def _get_headers(self):
        return {
            "Authorization": f"Bearer {self.tenant_access_token}",
            "Content-Type": "application/json; charset=utf-8"
        }

    def load_table_map(self):
        print("⏳ [2/4] 获取数据表结构...")
        url = f"{self.base_url}/bitable/v1/apps/{self.app_token}/tables"
        res = requests.get(url, headers=self._get_headers()).json()
        if res.get("code") == 0:
            tables = res["data"]["items"]
            for t in tables:
                self.table_map[t["name"]] = t["table_id"]
            print(f"📊 成功找到 {len(self.table_map)} 个数据表。")
        else:
            print(f"❌ 获取表格列表失败: {res.get('msg')}")
            sys.exit(1)

    def download_media(self, file_token, save_path):
        """下载附件，包含空 Token 校验防止 400 错误"""
        if not file_token:
            return False
            
        url = f"{self.base_url}/drive/v1/medias/{file_token}/download"
        headers = {"Authorization": f"Bearer {self.tenant_access_token}"}
        
        # 如果文件已存在则跳过，减少 API 调用
        if os.path.exists(save_path):
            return True

        print(f"      ⬇️ 下载图片: {os.path.basename(save_path)} ...", end="")
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            with open(save_path, 'wb') as f:
                f.write(res.content)
            print(" [成功]")
            return True
        else:
            print(f" [失败: HTTP {res.status_code}]")
            return False

    def sanitize_filename(self, name):
        if not name: return "default"
        safe_name = re.sub(r'[^a-zA-Z0-9_\-]', '', str(name).replace(' ', '_')).lower()
        return safe_name if safe_name else "default"

    def fetch_records(self, table_name):
        if table_name not in self.table_map:
            print(f"⚠️ 未找到 '{table_name}' 数据表，跳过。")
            return []

        table_id = self.table_map[table_name]
        url = f"{self.base_url}/bitable/v1/apps/{self.app_token}/tables/{table_id}/records"
        all_records = []
        has_more = True
        page_token = ""

        print(f"\n📥 [3/4] 拉取与处理：{table_name}")
        while has_more:
            params = {"page_size": 100, "page_token": page_token}
            res = requests.get(url, headers=self._get_headers(), params=params).json()
            if res.get("code") == 0:
                data = res["data"]
                if "items" in data:
                    for item in data["items"]:
                        record = item["fields"]
                        
                        # --- 核心图片命名逻辑：语义化前缀 + File Token 前8位 ---
                        
                        # 1. 团队成员头像
                        if table_name == "团队成员":
                            avatar_data = record.get('Avatar')
                            if avatar_data and isinstance(avatar_data, list):
                                file_token = avatar_data[0].get('file_token')
                                if file_token:
                                    ext = os.path.splitext(avatar_data[0]['name'])[1]
                                    token_suffix = file_token[:8].lower()
                                    safe_name = self.sanitize_filename(record.get('Name_en'))
                                    save_path = f"assets/images/team/{safe_name}_{token_suffix}{ext}"
                                    if self.download_media(file_token, save_path):
                                        record['local_avatar_path'] = f"/{save_path}"

                        # 2. 学术论文 Teaser 图
                        elif table_name == "学术论文":
                            image_data = record.get('Image')
                            if image_data and isinstance(image_data, list):
                                file_token = image_data[0].get('file_token')
                                if file_token:
                                    ext = os.path.splitext(image_data[0]['name'])[1]
                                    token_suffix = file_token[:8].lower()
                                    title_prefix = "_".join(str(record.get('Title_en', '')).split()[:3])
                                    safe_name = self.sanitize_filename(title_prefix)
                                    save_path = f"assets/images/papers/{safe_name}_{token_suffix}{ext}"
                                    if self.download_media(file_token, save_path):
                                        record['local_image_path'] = f"/{save_path}"

                        # 3. 研究方向背景图
                        elif table_name == "研究方向":
                            image_data = record.get('Image')
                            if image_data and isinstance(image_data, list):
                                file_token = image_data[0].get('file_token')
                                if file_token:
                                    ext = os.path.splitext(image_data[0]['name'])[1]
                                    token_suffix = file_token[:8].lower()
                                    safe_name = self.sanitize_filename(record.get('Title_en'))
                                    save_path = f"assets/images/research/{safe_name}_{token_suffix}{ext}"
                                    if self.download_media(file_token, save_path):
                                        record['local_image_path'] = f"/{save_path}"

                        all_records.append(record)
                
                has_more = data.get("has_more", False)
                page_token = data.get("page_token", "")
            else:
                print(f"❌ 拉取失败: {res.get('msg')}")
                break
        return all_records

# ==========================================
# 2. 数据清洗与转换器
# ==========================================
class DataConverter:
    @staticmethod
    def _get_text(field): return str(field).strip() if field else ""

    @staticmethod
    def _get_link(field):
        if isinstance(field, dict): return field.get("link", "")
        return str(field).strip() if field else ""

    @staticmethod
    def _get_option(field):
        if isinstance(field, dict): return field.get("text", "")
        return str(field).strip() if field else ""

    @staticmethod
    def _clean_empty(d):
        if isinstance(d, dict):
            return {k: v for k, v in ((k, DataConverter._clean_empty(v)) for k, v in d.items()) if v}
        elif isinstance(d, list):
            return [DataConverter._clean_empty(v) for v in d if v]
        return d

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
                "avatar": r.get("local_avatar_path", ""),
                "bio": {"zh": cls._get_text(r.get("Bio_zh")), "en": cls._get_text(r.get("Bio_en"))},
                "email": cls._get_text(r.get("Email")),
                "destination": {"zh": cls._get_text(r.get("Dest_zh")), "en": cls._get_text(r.get("Dest_en"))},
                "links": {
                    "homepage": cls._get_link(r.get("Link_Homepage")),
                    "scholar": cls._get_link(r.get("Link_Scholar")),
                    "github": cls._get_link(r.get("Link_GitHub")),
                    "linkedin": cls._get_link(r.get("Link_LinkedIn")),
                    "zhihu": cls._get_link(r.get("Link_Zhihu")),
                }
            }
            yaml_list.append(cls._clean_empty(item))
        return sorted(yaml_list, key=lambda x: x.get("rank", 99))

    @classmethod
    def convert_publications(cls, records):
        yaml_list = []
        for r in records:
            item = {
                "title": {"zh": cls._get_text(r.get("Title_zh")), "en": cls._get_text(r.get("Title_en"))},
                "authors": cls._get_text(r.get("Authors")),
                "type": cls._get_option(r.get("Type")),
                "venue": cls._get_text(r.get("Venue")),
                "year": int(r.get("Year") if r.get("Year") else 2024),
                "highlight": cls._get_text(r.get("Highlight")),
                "image": r.get("local_image_path", ""),
                "abstract": {"zh": cls._get_text(r.get("Abstract_zh")), "en": cls._get_text(r.get("Abstract_en"))},
                "links": {
                    "paper": cls._get_link(r.get("Link_Paper")),
                    "code": cls._get_link(r.get("Link_Code")),
                    "project": cls._get_link(r.get("Link_Project")),
                    "video": cls._get_link(r.get("Link_Video")),
                }
            }
            yaml_list.append(cls._clean_empty(item))
        return sorted(yaml_list, key=lambda x: x.get("year", 0), reverse=True)

    @classmethod
    def convert_research(cls, records):
        yaml_list = []
        for r in records:
            pts_zh = [p.strip() for p in cls._get_text(r.get("Points_zh")).split('\n') if p.strip() and "选填" not in p]
            pts_en = [p.strip() for p in cls._get_text(r.get("Points_en")).split('\n') if p.strip()]
            item = {
                "icon": cls._get_text(r.get("Icon")),
                "image": r.get("local_image_path", ""),
                "title": {"zh": cls._get_text(r.get("Title_zh")), "en": cls._get_text(r.get("Title_en"))},
                "description": {"zh": cls._get_text(r.get("Desc_zh")), "en": cls._get_text(r.get("Desc_en"))},
                "points": {"zh": pts_zh, "en": pts_en}
            }
            yaml_list.append(cls._clean_empty(item))
        return yaml_list

    @classmethod
    def convert_positions(cls, records):
        yaml_list = []
        for r in records:
            tags_zh = [t.strip() for t in cls._get_text(r.get("Tags_zh")).replace('，', ',').split(',') if t.strip() and "选填" not in t]
            tags_en = [t.strip() for t in cls._get_text(r.get("Tags_en")).replace('，', ',').split(',') if t.strip()]
            item = {
                "title": {"zh": cls._get_text(r.get("Title_zh")), "en": cls._get_text(r.get("Title_en"))},
                "count": {"zh": cls._get_text(r.get("Count_zh")), "en": cls._get_text(r.get("Count_en"))},
                "department": {"zh": cls._get_text(r.get("Dept_zh")), "en": cls._get_text(r.get("Dept_en"))},
                "icon": cls._get_text(r.get("Icon")),
                "theme": cls._get_option(r.get("Theme")) or "slate",
                "description": {"zh": cls._get_text(r.get("Desc_zh")), "en": cls._get_text(r.get("Desc_en"))},
                "tags": {"zh": tags_zh, "en": tags_en},
                "link": cls._get_link(r.get("Link"))
            }
            yaml_list.append(cls._clean_empty(item))
        return yaml_list

    @classmethod
    def convert_news(cls, records):
        yaml_list = []
        for r in records:
            timestamp = r.get("Date")
            date_str = datetime.fromtimestamp(timestamp / 1000).strftime('%Y.%m') if timestamp else ""
            item = {
                "date": date_str,
                "category": {"zh": cls._get_option(r.get("Category_zh")), "en": cls._get_option(r.get("Category_en"))},
                "title": {"zh": cls._get_text(r.get("Title_zh")), "en": cls._get_text(r.get("Title_en"))},
                "description": {"zh": cls._get_text(r.get("Desc_zh")), "en": cls._get_text(r.get("Desc_en"))},
                "link": cls._get_link(r.get("Link"))
            }
            yaml_list.append(cls._clean_empty(item))
        return sorted(yaml_list, key=lambda x: x.get("date", ""), reverse=True)


# ==========================================
# 3. 核心执行逻辑
# ==========================================
if __name__ == "__main__":
    print("="*60)
    print("🚀 LV Group - 飞书数据同步至 Jekyll (带附件下载)")
    print("="*60)

    reader = FeishuReader()
    reader.authenticate()
    reader.load_table_map()
    
    # 任务配置：表格名 -> 转换函数 -> 目标 YAML 文件
    sync_tasks = [
        {"table": "团队成员", "func": DataConverter.convert_team, "file": "_data/team.yml"},
        {"table": "学术论文", "func": DataConverter.convert_publications, "file": "_data/publications.yml"},
        {"table": "研究方向", "func": DataConverter.convert_research, "file": "_data/research.yml"},
        {"table": "招聘与招生", "func": DataConverter.convert_positions, "file": "_data/positions.yml"},
        {"table": "新闻动态", "func": DataConverter.convert_news, "file": "_data/news.yml"}
    ]
    
    os.makedirs("_data", exist_ok=True)
    
    print("\n[4/4] 转换数据并写入 YAML 文件...")
    for task in sync_tasks:
        table_name = task["table"]
        target_file = task["file"]
        
        raw_records = reader.fetch_records(table_name)
        if not raw_records:
            continue
            
        # 🌟 自动过滤包含“必填”或“示例”字样的引导/占位数据
        filtered_records = [
            r for r in raw_records 
            if "必填" not in str(r.get("Name_zh", "")) and "示例" not in str(r.get("Name_zh", ""))
        ]
        
        clean_data = task["func"](filtered_records)
        
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(f"# Auto-generated from Feishu Bitable: {table_name}\n")
            f.write(f"# Sync Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            yaml.dump(clean_data, f, allow_unicode=True, sort_keys=False, indent=2, default_flow_style=False)
            
        print(f"    ✅ 已生成/更新: {target_file}")

    print("\n" + "="*60)
    print("🎉 所有数据同步完成！你可以运行 bundle exec jekyll serve 预览网站了！")
    print("="*60)