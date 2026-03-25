import os
import sys
import yaml
import requests
import time

# ==========================================
# 1. 基础接口定义 (Schema Base)
# ==========================================
class BaseTableSchema:
    """所有数据表结构定义的抽象基类"""
    @property
    def table_name(self):
        raise NotImplementedError("子类必须实现 table_name 属性")

    @property
    def fields(self):
        raise NotImplementedError("子类必须实现 fields 属性")

    @property
    def sample_record(self):
        """提供一行给用户的示例/提示数据"""
        return {}


# ==========================================
# 2. 具体的子表定义 (双重提示版: 🔴 必填 / ⚪ 选填)
# ==========================================
class PeopleTableSchema(BaseTableSchema):
    @property
    def table_name(self): return "团队成员"
    @property
    def fields(self):
        return [
            {"field_name": "Name_zh", "type": 1, "description": {"text": "🔴 [必填] 成员的中文姓名"}}, 
            {"field_name": "Name_en", "type": 1, "description": {"text": "🔴 [必填] 英文姓名 (如: Wenbin Zuo)"}},
            {
                "field_name": "Group_ID", "type": 3, "description": {"text": "🔴 [必填] 决定成员显示在网站哪个板块"},
                "property": {
                    "options": [
                        {"name": "professor", "color": 0}, {"name": "associate_prof", "color": 1},
                        {"name": "assistant_prof", "color": 2}, {"name": "researchers", "color": 3},
                        {"name": "phd", "color": 4}, {"name": "master", "color": 5}, 
                        {"name": "undergrad", "color": 6}, {"name": "interns", "color": 7}, 
                        {"name": "alumni", "color": 8}
                    ]
                }
            },
            {"field_name": "Rank", "type": 2, "description": {"text": "⚪ [选填] 排序权重 (数字越小越靠前)"}}, 
            {"field_name": "Title_zh", "type": 1, "description": {"text": "🔴 [必填] 身份/年级 (如: 博士生)"}}, 
            {"field_name": "Title_en", "type": 1, "description": {"text": "🔴 [必填] 身份/年级英文版"}},
            {"field_name": "Role_zh", "type": 1, "description": {"text": "⚪ [选填] 组内职务 (如: 核心骨干)"}}, 
            {"field_name": "Role_en", "type": 1, "description": {"text": "⚪ [选填] 组内职务英文版"}},
            {"field_name": "Avatar", "type": 17, "description": {"text": "⚪ [选填] 拖拽正方形免冠照至此"}}, 
            {"field_name": "Bio_zh", "type": 1, "description": {"text": "⚪ [选填] 中文个人简介 (Alt+Enter 换行)"}}, 
            {"field_name": "Bio_en", "type": 1, "description": {"text": "⚪ [选填] 英文个人简介"}},
            {"field_name": "Email", "type": 1, "description": {"text": "⚪ [选填] 常用联系邮箱"}}, 
            {"field_name": "Dest_zh", "type": 1, "description": {"text": "⚪ [选填] (仅校友填写) 毕业去向"}}, 
            {"field_name": "Dest_en", "type": 1, "description": {"text": "⚪ [选填] (仅校友填写) 毕业去向英文版"}},
            {"field_name": "Link_Homepage", "type": 15, "description": {"text": "⚪ [选填] 个人主页链接"}}, 
            {"field_name": "Link_Scholar", "type": 15, "description": {"text": "⚪ [选填] Google Scholar 主页"}},
            {"field_name": "Link_GitHub", "type": 15, "description": {"text": "⚪ [选填] GitHub 主页"}}, 
            {"field_name": "Link_LinkedIn", "type": 15, "description": {"text": "⚪ [选填] LinkedIn 主页"}}, 
            {"field_name": "Link_Zhihu", "type": 15, "description": {"text": "⚪ [选填] 知乎主页"}}
        ]
        
    @property
    def sample_record(self):
        return {
            "Name_zh": "🔴[必填] 张三 (请替换)", "Name_en": "🔴[必填] San Zhang",
            "Group_ID": "professor", "Rank": 1,
            "Title_zh": "🔴[必填] 教授 / 博导", "Title_en": "🔴[必填] Professor",
            "Role_zh": "⚪[选填] 课题组负责人", "Role_en": "⚪[选填] Principal Investigator",
            "Bio_zh": "⚪[选填] 💡提示：多行请按 Alt+Enter。👉 左侧头像也是选填的，直接拖入照片即可。",
            "Email": "⚪[选填] example@tongji.edu.cn", "Link_Homepage": "https://example.com" 
        }

class NewsTableSchema(BaseTableSchema):
    @property
    def table_name(self): return "新闻动态"
    @property
    def fields(self):
        return [
            {"field_name": "Date", "type": 5, "description": {"text": "🔴 [必填] 新闻发生日期"}}, 
            {
                "field_name": "Category_zh", "type": 3, "description": {"text": "🔴 [必填] 中文分类"},
                "property": {"options": [{"name": "实验室动态", "color": 0}, {"name": "开源项目", "color": 1}, {"name": "学术合作", "color": 2}, {"name": "荣誉奖项", "color": 3}, {"name": "基础设施", "color": 4}, {"name": "招生动态", "color": 5}]}
            }, 
            {
                "field_name": "Category_en", "type": 3, "description": {"text": "🔴 [必填] 英文分类"},
                "property": {"options": [{"name": "Lab Event", "color": 0}, {"name": "Open Source", "color": 1}, {"name": "Collaboration", "color": 2}, {"name": "Awards", "color": 3}, {"name": "Infrastructure", "color": 4}, {"name": "Admissions", "color": 5}]}
            },
            {"field_name": "Title_zh", "type": 1, "description": {"text": "🔴 [必填] 新闻中文标题"}}, 
            {"field_name": "Title_en", "type": 1, "description": {"text": "🔴 [必填] 新闻英文标题"}},
            {"field_name": "Desc_zh", "type": 1, "description": {"text": "⚪ [选填] 新闻详细描述"}}, 
            {"field_name": "Desc_en", "type": 1, "description": {"text": "⚪ [选填] 详细描述英文版"}}, 
            {"field_name": "Link", "type": 15, "description": {"text": "⚪ [选填] 相关外部链接"}}
        ]
        
    @property
    def sample_record(self):
        return {
            "Date": int(time.time() * 1000), 
            "Category_zh": "实验室动态", "Category_en": "Lab Event",
            "Title_zh": "🔴[必填] 全新官方网站上线", "Title_en": "🔴[必填] New Website Launched",
            "Desc_zh": "⚪[选填] 💡在这里详细描述事件经过...", "Link": "https://cdi-lv-group.github.io"
        }

class PublicationsTableSchema(BaseTableSchema):
    @property
    def table_name(self): return "学术论文"
    @property
    def fields(self):
        return [
            {"field_name": "Title_zh", "type": 1, "description": {"text": "🔴 [必填] 论文中文标题"}}, 
            {"field_name": "Title_en", "type": 1, "description": {"text": "🔴 [必填] 论文英文原名"}}, 
            {"field_name": "Authors", "type": 1, "description": {"text": "🔴 [必填] 作者列表 (用 <b>名字</b> 加粗课题组成员)"}},
            {
                "field_name": "Type", "type": 3, "description": {"text": "🔴 [必填] 论文类别"},
                "property": {"options": [{"name": "conference",

# ==========================================
# 3. 核心初始化引擎
# ==========================================
class FeishuBitableInitializer:
    def __init__(self, config_file="feishu_config.yml"):
        self.config_file = config_file
        # ⚠️ 强烈建议通过环境变量获取，防止代码泄露


        self.app_id = os.environ.get("FEISHU_APP_ID", "cli_a924e03710219cee")
        self.app_secret = os.environ.get("FEISHU_APP_SECRET", "5klcCSICBJWjCHn9ngKJH4imARMnptWk")
        self.app_token = self._load_app_token()
        self.tenant_access_token = None
        self.base_url = "https://open.feishu.cn/open-apis"
        self.schemas = [] 

    def register_schema(self, schema_instance: BaseTableSchema):
        self.schemas.append(schema_instance)

    def _load_app_token(self):
        print("▶️ [1/3] 读取配置文件锁定目标表格...")
        if not os.path.exists(self.config_file):
            print(f"❌ 找不到配置: {self.config_file}")
            sys.exit(1)
        with open(self.config_file, 'r', encoding='utf-8') as f:
            app_token = yaml.safe_load(f).get('app_token')
            if not app_token or "填入你的" in app_token:
                print("❌ 无效的 app_token！")
                sys.exit(1)
            return app_token

    def authenticate(self):
        print("▶️ [2/3] 正在获取全局授权 Token...")
        url = f"{self.base_url}/auth/v3/tenant_access_token/internal"
        res = requests.post(url, json={"app_id": self.app_id, "app_secret": self.app_secret}).json()
        if res.get("code") == 0:
            self.tenant_access_token = res.get("tenant_access_token")
            print("✅ 身份验证成功！")
        else:
            print(f"❌ 验证失败: {res}")
            sys.exit(1)

    def _get_headers(self):
        return {
            "Authorization": f"Bearer {self.tenant_access_token}",
            "Content-Type": "application/json; charset=utf-8"
        }

    def execute(self):
        print("\n▶️ [3/3] 开始批量部署被注册的数据表...")
        headers = self._get_headers()
        
        for schema in self.schemas:
            t_name = schema.table_name
            t_fields = schema.fields
            print(f"\n  ⚙️ 正在检查数据表：[{t_name}]")
            
            # 1. 尝试建表
            t_url = f"{self.base_url}/bitable/v1/apps/{self.app_token}/tables"
            t_res = requests.post(t_url, headers=headers, json={"table": {"name": t_name}}).json()
            
            # 如果表已存在，跳过
            if t_res.get("code") != 0:
                if t_res.get('code') == 1254605: 
                    print(f"  ⏭️ [跳过] 表 [{t_name}] 已存在。为防止数据重复，自动跳过初始化。")
                else:
                    print(f"  ❌ 建表失败: {t_res.get('msg')}")
                continue
                
            table_id = t_res["data"]["table_id"]
            
            # 2. 如果是新表，部署字段列
            f_url = f"{self.base_url}/bitable/v1/apps/{self.app_token}/tables/{table_id}/fields"
            success_count = 0
            for field in t_fields:
                f_res = requests.post(f_url, headers=headers, json=field).json()
                if f_res.get("code") == 0:
                    success_count += 1
                else:
                    print(f"    ⚠️ 列 [{field['field_name']}] 创建异常: {f_res.get('msg')}")
            
            print(f"  ✅ 字段部署完成 ({success_count}/{len(t_fields)} 列)！")
            
            # 3. 注入一条温馨提示的“示例数据”
            print("    - 正在为您注入【示例数据】指南...")
            r_url = f"{self.base_url}/bitable/v1/apps/{self.app_token}/tables/{table_id}/records"
            
            # 专门处理飞书的坑：虽然用户只想填字符串，但API严格要求封装成 dict，我们在发请求前动态转换一下
            processed_record = {}
            for k, v in schema.sample_record.items():
                # 判断是不是 URL 类型的列 (类型15在上面的 fields 定义中可查)
                is_link_field = any(f.get("field_name") == k and f.get("type") == 15 for f in t_fields)
                if is_link_field and isinstance(v, str):
                    processed_record[k] = {"link": v, "text": v} # 自动封装成飞书API接受的格式
                else:
                    processed_record[k] = v

            r_payload = {"fields": processed_record}
            r_res = requests.post(r_url, headers=headers, json=r_payload).json()
            
            if r_res.get("code") == 0:
                print("    ✅ 示例数据已填入！您可以在飞书网页中照猫画虎。")
            else:
                print(f"    ⚠️ 示例数据注入失败 (可忽略): {r_res.get('msg')}")
                
            time.sleep(0.8)


# ==========================================
# 4. 主程序入口
# ==========================================
if __name__ == "__main__":
    print("="*65)
    print("🚀 启动多维表格插件化引擎 (带自动填表 & 防重复机制)")
    print("="*65)
    
    engine = FeishuBitableInitializer()
    engine.register_schema(PeopleTableSchema())
    engine.register_schema(NewsTableSchema())
    engine.register_schema(PublicationsTableSchema())
    engine.register_schema(PositionsTableSchema())
    engine.register_schema(ResearchTableSchema())
    
    engine.authenticate()
    engine.execute()
    
    print("\n" + "="*65)
    print("🎉 恭喜！任务执行完毕。")
    print("👉 如果有新建的表，里面已经备好了示例提示数据供您参考！")
    print("="*65)