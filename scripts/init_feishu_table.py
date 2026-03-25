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
# 2. 具体的子表定义 (带有默认示例数据)
# ==========================================
class PeopleTableSchema(BaseTableSchema):
    @property
    def table_name(self): 
        return "团队成员"
        
    @property
    def fields(self):
        return [
            {"field_name": "Name_zh", "type": 1}, 
            {"field_name": "Name_en", "type": 1},
            {
                "field_name": "Group_ID", 
                "type": 3, # 3 代表单选标签
                "property": {
                    "options": [
                        # 严格对齐网站 _data/groups.yml 的分类字典
                        {"name": "professor", "color": 0},
                        {"name": "associate_prof", "color": 1},
                        {"name": "assistant_prof", "color": 2},
                        {"name": "researchers", "color": 3},
                        {"name": "phd", "color": 4}, 
                        {"name": "master", "color": 5}, 
                        {"name": "undergrad", "color": 6}, 
                        {"name": "interns", "color": 7}, 
                        {"name": "alumni", "color": 8}
                    ]
                }
            },
            {"field_name": "Rank", "type": 2}, # 2 代表数字型，用于控制网站上的排序
            {"field_name": "Title_zh", "type": 1}, 
            {"field_name": "Title_en", "type": 1},
            {"field_name": "Role_zh", "type": 1}, 
            {"field_name": "Role_en", "type": 1},
            
            # 🚀 核心升级：17 代表附件类型。这样成员就可以直接在飞书中拖拽上传免冠照了
            {"field_name": "Avatar", "type": 17}, 
            
            {"field_name": "Bio_zh", "type": 1}, 
            {"field_name": "Bio_en", "type": 1},
            {"field_name": "Email", "type": 1}, 
            {"field_name": "Dest_zh", "type": 1}, 
            {"field_name": "Dest_en", "type": 1},
            
            # 15 代表超链接类型
            {"field_name": "Link_Homepage", "type": 15}, 
            {"field_name": "Link_Scholar", "type": 15},
            {"field_name": "Link_GitHub", "type": 15}, 
            {"field_name": "Link_LinkedIn", "type": 15}, 
            {"field_name": "Link_Zhihu", "type": 15}
        ]
        
    @property
    def sample_record(self):
        return {
            "Name_zh": "张三 (示例)", 
            "Name_en": "San Zhang",
            "Group_ID": "professor", 
            "Rank": 1,
            "Title_zh": "教授 / 博导", 
            "Title_en": "Professor",
            "Role_zh": "课题组负责人", 
            "Role_en": "Principal Investigator",
            # 注意：通过 API 注入初始图片略微复杂，这里我们在文本列给用户留下操作指引
            "Bio_zh": "💡提示：在这里填写中文简介。多行请按 Alt+Enter 换行。👉 【头像】请直接将正方形照片拖入左侧 Avatar 单元格中。",
            "Bio_en": "💡Tip: Write English bio here. 👉 Drag and drop your square photo into the Avatar cell.",
            "Email": "example@tongji.edu.cn",
            # 超链接直接使用纯净的字符串形式即可，底层执行逻辑会自动帮你做字典封装
            "Link_Homepage": "https://example.com" 
        }

class NewsTableSchema(BaseTableSchema):
    @property
    def table_name(self): 
        return "新闻动态"
        
    @property
    def fields(self):
        return [
            # 5 代表日期类型，在飞书里会弹出日历选择器，方便大家统一时间格式
            {"field_name": "Date", "type": 5}, 
            
            # 🚀 核心升级：将中文分类改为单选标签，规范大家的输入，避免错别字
            {
                "field_name": "Category_zh", 
                "type": 3, 
                "property": {
                    "options": [
                        {"name": "实验室动态", "color": 0},
                        {"name": "开源项目", "color": 1},
                        {"name": "学术合作", "color": 2},
                        {"name": "荣誉奖项", "color": 3},
                        {"name": "基础设施", "color": 4},
                        {"name": "招生动态", "color": 5}
                    ]
                }
            }, 
            # 🚀 核心升级：同步将英文分类改为单选标签
            {
                "field_name": "Category_en", 
                "type": 3, 
                "property": {
                    "options": [
                        {"name": "Lab Event", "color": 0},
                        {"name": "Open Source", "color": 1},
                        {"name": "Collaboration", "color": 2},
                        {"name": "Awards", "color": 3},
                        {"name": "Infrastructure", "color": 4},
                        {"name": "Admissions", "color": 5}
                    ]
                }
            },
            
            {"field_name": "Title_zh", "type": 1}, 
            {"field_name": "Title_en", "type": 1},
            {"field_name": "Desc_zh", "type": 1}, 
            {"field_name": "Desc_en", "type": 1}, 
            
            # 15 代表超链接类型
            {"field_name": "Link", "type": 15}
        ]
        
    @property
    def sample_record(self):
        return {
            # 注入示例数据时，自动填入今天的时间戳
            "Date": int(time.time() * 1000), 
            "Category_zh": "实验室动态", 
            "Category_en": "Lab Event",
            "Title_zh": "LV课题组全新官方网站正式上线 (示例)", 
            "Title_en": "New LV Lab Official Website Launched",
            "Desc_zh": "💡提示：在这里填写新闻的详细中文描述。可以直接粘贴，无需管格式。",
            "Desc_en": "💡Tip: Write the detailed news description here...",
            # 超链接如果没有，用户可以直接在飞书里留空或填 #
            "Link": "https://cdi-lv-group.github.io"
        }

class PublicationsTableSchema(BaseTableSchema):
    @property
    def table_name(self): 
        return "学术论文"
        
    @property
    def fields(self):
        return [
            {"field_name": "Title_zh", "type": 1}, 
            {"field_name": "Title_en", "type": 1}, 
            {"field_name": "Authors", "type": 1},
            {
                "field_name": "Type", 
                "type": 3, 
                "property": {
                    "options": [
                        {"name": "conference", "color": 0}, 
                        {"name": "journal", "color": 1}, 
                        {"name": "preprint", "color": 2}
                    ]
                }
            },
            {"field_name": "Venue", "type": 1}, 
            # 2 代表数字类型，确保网页上的按年份倒序排列能正常运作
            {"field_name": "Year", "type": 2}, 
            {"field_name": "Highlight", "type": 1},
            
            # 🚀 核心升级：17 代表附件类型。支持直接拖拽上传论文的 Teaser 效果图！
            {"field_name": "Image", "type": 17}, 
            
            {"field_name": "Abstract_zh", "type": 1}, 
            {"field_name": "Abstract_en", "type": 1},
            
            # 15 代表超链接类型，飞书会自动识别并渲染为可点击的卡片或蓝色链接
            {"field_name": "Link_Paper", "type": 15}, 
            {"field_name": "Link_Code", "type": 15}, 
            {"field_name": "Link_Project", "type": 15}, 
            {"field_name": "Link_Video", "type": 15}
        ]
        
    @property
    def sample_record(self):
        return {
            "Title_zh": "统一单目标与多目标跟踪的联合学习框架 (示例)", 
            "Title_en": "Unified Learning Framework for SOT and MOT",
            # 提醒填表人核心成员加粗的 HTML 写法
            "Authors": "<b>Wenbin Zuo</b>, Jingkuan Song, Weiwei Guo*, et al.",
            "Type": "conference", 
            "Venue": "CVPR", 
            "Year": 2026,
            "Highlight": "Oral",
            # 在文本提示中指导用户如何上传图片
            "Abstract_zh": "💡提示：复制粘贴论文摘要到这里。👉 【Image】列请直接将论文的Teaser图（建议16:9）拖拽进去。",
            "Abstract_en": "💡Tip: Paste the abstract here. 👉 Drag and drop the Teaser image into the Image cell.",
            # 给出各个链接的占位符，没有的链接用户只需留空即可
            "Link_Paper": "https://arxiv.org/abs/xxxx",
            "Link_Code": "https://github.com/cdi-lv-group",
            "Link_Project": "https://cdi-lv-group.github.io",
            "Link_Video": "https://youtube.com"
        }


class PositionsTableSchema(BaseTableSchema):
    @property
    def table_name(self): 
        return "招聘与招生"
        
    @property
    def fields(self):
        return [
            {"field_name": "Title_zh", "type": 1}, 
            {"field_name": "Title_en", "type": 1},
            {"field_name": "Count_zh", "type": 1}, 
            {"field_name": "Count_en", "type": 1},
            {"field_name": "Dept_zh", "type": 1}, 
            {"field_name": "Dept_en", "type": 1}, 
            
            # 填入 Emoji 作为图标
            {"field_name": "Icon", "type": 1},
            
            # 🚀 核心升级：增加 slate 兜底配色，严格对齐前端 Tailwind CSS 变量
            {
                "field_name": "Theme", 
                "type": 3, 
                "property": {
                    "options": [
                        {"name": "blue", "color": 0}, 
                        {"name": "cyan", "color": 1}, 
                        {"name": "green", "color": 2}, 
                        {"name": "indigo", "color": 3}, 
                        {"name": "orange", "color": 4},
                        {"name": "slate", "color": 5}
                    ]
                }
            },
            
            {"field_name": "Desc_zh", "type": 1}, 
            {"field_name": "Desc_en", "type": 1},
            
            # 使用普通文本，但通过提示规范分隔符
            {"field_name": "Tags_zh", "type": 1}, 
            {"field_name": "Tags_en", "type": 1}, 
            
            # 15 代表超链接类型
            {"field_name": "Link", "type": 15}
        ]
        
    @property
    def sample_record(self):
        return {
            "Title_zh": "博士生 (Ph.D.) - 示例", 
            "Title_en": "Ph.D. Candidates",
            "Count_zh": "1-2名/年", 
            "Count_en": "1-2 per year",
            "Dept_zh": "上海自主智能无人系统科学中心 / 设计创意学院", 
            "Dept_en": "SISTUS / College of Design and Innovation",
            "Icon": "🎓", 
            "Theme": "blue",
            "Desc_zh": "💡提示：在这里填写要求与福利。比如：提供全额奖学金，要求扎实的数学基础与编程能力（PyTorch/C++）。",
            "Desc_en": "💡Tip: Write position requirements and benefits here...",
            
            # 🚀 强提示：指导填表人如何格式化标签，以便后续拉取脚本一键 split
            "Tags_zh": "计算机视觉,具身智能 (💡提示：如果有多个标签，请务必用【逗号】隔开)", 
            "Tags_en": "Computer Vision,Embodied AI",
            
            # 超链接如果没有具体的申请网址，可以填 # 或者留空
            "Link": "https://example.com/apply"
        }

class ResearchTableSchema(BaseTableSchema):
    @property
    def table_name(self): 
        return "研究方向"
        
    @property
    def fields(self):
        return [
            # 填入 Emoji 作为方向图标
            {"field_name": "Icon", "type": 1}, 
            
            # 🚀 核心升级：17 代表附件类型。支持直接拖拽上传卡片的高清背景配图！
            {"field_name": "Image", "type": 17}, 
            
            {"field_name": "Title_zh", "type": 1}, 
            {"field_name": "Title_en", "type": 1},
            {"field_name": "Desc_zh", "type": 1}, 
            {"field_name": "Desc_en", "type": 1},
            
            # 使用普通文本，但通过提示规范换行符作为数组的分隔符
            {"field_name": "Points_zh", "type": 1}, 
            {"field_name": "Points_en", "type": 1}
        ]
        
    @property
    def sample_record(self):
        return {
            "Icon": "👁️", 
            "Title_zh": "3D感知与空间理解 (示例)", 
            "Title_en": "3D Perception & Understanding",
            "Desc_zh": "💡提示：在这里填写该大方向的简介。👉 【Image】列请直接将好看的背景配图拖拽进去。",
            "Desc_en": "💡Tip: Write a brief description here...",
            
            # 🚀 强提示：指导填表人如何排版列表项 (Points)，以便后续脚本一键 split('\n')
            "Points_zh": "全天候 3D 场景下的稳定目标追踪\n多源异构传感器的动态数据融合与校准\n(💡提示：如果有多个研究细分点，请务必按 Alt+Enter 进行换行)", 
            "Points_en": "Stable 3D object tracking in all-weather conditions\nDynamic data fusion and calibration"
        }

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