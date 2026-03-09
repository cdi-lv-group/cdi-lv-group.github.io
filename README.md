---

# 🎓 Academic Group Web Engine (Bilingual & Data-Driven)

这是一个面向科研课题组（Research Groups）设计的**数据驱动型**静态网站模板。它通过“数据与代码分离”的架构，支持通过 **飞书 (Feishu/Lark)** 等云端平台同步更新，自动生成专业且美观的中英双语学术主页。

## 🛠️ 技术栈 (Tech Stack)

* **SSG**: Jekyll / Hugo (支持 GitHub Pages / Vercel 自动部署)
* **Data**: YAML 1.2 (位于 `_data/` 目录，全站单一事实来源)
* **Automation**: GitHub Actions + Python API Sync (支持多平台同步)
* **UI**: Tailwind CSS / Bootstrap (响应式设计，学术风格)

---

## 📝 数据维护手册 (Data Dictionary & Templates)

全站内容由 `_data/` 目录下的六个核心 YAML 文件驱动。更新时请确保所有**必填字段**完整。

### 1. 团队分类字典 (`team_groups.yml`)

定义全站的身份分组与视觉色彩。`id` 必须与成员表中的 `group_id` 严格对应。

```yaml
# 模板示例
- id: "phd"                  # [必填] 唯一标识符，关联 people.yml
  title:                     # [必填] 双语分组标题
    zh: "博士研究生"
    en: "Ph.D. Students"
  color: "blue"              # [选填] 绑定颜色：indigo, purple, blue, cyan, green, orange, gray

```

### 2. 团队成员 (`people.yml`)

用于展示老师、学生及校友。

```yaml
# 模板示例
- name: { zh: "姓名", en: "Name" }      # [必填] 双语姓名
  group_id: "phd"                      # [必填] 对应 team_groups 中的 id
  rank: 10                             # [选填] 排序权重，越小越靠前
  title: { zh: "博士生", en: "Ph.D. Student" } # [必填] 身份/年级描述
  role: { zh: "核心骨干", en: "Core Member" } # [选填] 实验室职务
  avatar: "/assets/images/team/x.jpg"  # [选填] 头像路径，建议 1:1 正方形
  bio:                                 # [选填] 个人简介
    zh: "中文简介内容..."
    en: "English biography..."
  email: "xxx@tongji.edu.cn"           # [选填] 邮箱地址
  destination:                         # [仅校友选填] 毕业去向
    zh: "🎓 毕业于：XX大学/公司"
    en: "🎓 Joined XX Univ/Co."
  links:                               # [选填] 社交/学术链接图标
    homepage: "https://..."
    scholar: "https://..."
    github: "https://..."
    linkedin: "https://..."
    zhihu: "https://..."

```

### 3. 学术论文 (`publications.yml`)

系统会自动提取 `year` 字段进行年度聚类，并按发表时间排序。

```yaml
# 模板示例
- title: 
    zh: "中文论文标题"
    en: "English Paper Title"
  authors: "Author A, <b>Wenbin Zuo</b>*" # [必填] 核心成员加粗 <b>，通讯作者加 *
  type: "conference"                      # [必填] conference/journal/preprint
  venue: "CVPR 2026"                      # [必填] 发表场所（会议/期刊名）
  year: 2026                              # [必填] 纯数字年份，用于分组
  highlight: "Oral"                       # [选填] 荣誉徽标（如 Oral/Spotlight）
  image: "/assets/img/pub/teaser.jpg"     # [选填] 效果图/Teaser，建议 16:9
  abstract:                               # [选填] 简短摘要
    zh: "这是一段中文摘要介绍..."
    en: "This is a short English abstract..."
  links:                                  # [选填] 资源链接矩阵
    paper: "https://..."                  # PDF/arXiv 链接
    code: "https://..."                   # GitHub 仓库
    project: "https://..."                 # 项目主页
    video: "https://..."                   # 视频讲解

```

### 4. 新闻动态 (`news.yml`)

驱动首页的时间轴展示。

```yaml
# 模板示例
- date: "2026.03"             # [必填] 日期，建议使用 YYYY.MM 格式
  category:                   # [必填] 新闻分类
    zh: "荣誉奖项"
    en: "Awards"
  title:                      # [必填] 新闻标题
    zh: "实验室获得某某优秀奖"
    en: "Lab wins the Best Award"
  description:                # [选填] 详细描述
    zh: "详细描述内容..."
    en: "Detailed description..."
  link: "#"                   # [选填] 详情链接，若无则设为 "#"

```

### 5. 招聘与招生 (`positions.yml`)

用于发布实验室人才招募信息。

```yaml
# 模板示例
- title: { zh: "职位名称", en: "Position Title" } # [必填]
  count: { zh: "1-2名", en: "1-2 seats" }         # [必填] 招录人数/频率
  department: { zh: "同济大学", en: "TJ Univ" }    # [必填] 依托单位
  icon: "🚀"                                     # [必填] 展示 Emoji 图标
  theme: "blue"                                  # [必填] 视觉主题色（见视觉字典）
  description:                                   # [必填] 详细要求与福利
    zh: "职位要求描述..."
    en: "Position requirements..."
  tags:                                          # [选填] 核心关键词标签
    zh: ["深度学习", "视觉感知"]
    en: ["Deep Learning", "Vision"]
  link: "#"                                      # [选填] 申请链接或详情页

```

### 6. 研究方向 (`research.yml`)

实验室核心科研能力的展示板块。

```yaml
# 模板示例
- icon: "🔬"                               # [必填] 核心图标
  title: { zh: "研究方向", en: "Research Area" } # [必填]
  image: "https://..."                    # [选填] 背景配图 URL
  description:                            # [必填] 宏观方向描述
    zh: "中文简介..."
    en: "English description..."
  points:                                 # [选填] 细分研究点列表
    zh: ["细分方向 1", "细分方向 2"]
    en: ["Sub-field 1", "Sub-field 2"]

```

---

## 🚀 部署与更新说明 (Deployment Guide)

### 方案 A：直接修改文件 (开发者推荐)

1. Fork 本仓库并开启 GitHub Pages。
2. 修改 `_data/` 下的 `.yml` 文件并提交。
3. GitHub Actions 会自动触发构建。

### 方案 B：云端表单管理 (实验室成员推荐)

1. 关联飞书多维表格（Bitable）。
2. 使用本项目提供的 `sync_all.py` 脚本，将表格数据一键拉取并转换为 YAML。
3. 实现“填表即更新”的极简体验。

---

## 📸 图片托管建议

为了保证网站加载性能：

* **头像:** 建议正方形，压缩至 500px 以内。
* **论文图:** 建议 16:9，宽度不超过 800px。
* **托管方案:** 可使用本地路径 `/assets/images/`，或利用 GitHub Issues/图床获取永久 URL。

---

## 🤝 贡献与定制

本模板致力于成为最懂学术圈的网页模板。如果你有更好的 UI 设计或功能建议，欢迎提交 Issue 或 Pull Request。

**License:** MIT

**Maintainer:** [Wenbin Zuo/LV Group]

---


## 🗓️ 后续计划 (Future Roadmap)

* **飞书 CMS 集成**: 支持通过飞书多维表格（Bitable）在线更新数据，实现“填表即发布”。
* **更多主题支持**: 增加多种学术风格的主题配色。
* **BibTeX 支持**: 自动从 BibTeX 文件生成 `publications.yml` 数据。

