# Academic Group Web Engine

这是一个面向科研课题组的双语、数据驱动型 Jekyll 网站模板。站点内容由 `_data/` 中的 YAML 文件驱动，页面结构与视觉系统集中在 `_layouts/`、`_includes/`、`assets/css/` 和 `assets/js/` 中，飞书同步逻辑位于 `scripts/feishu_sync/`。

当前仓库默认包含一套高质量但虚构的 mock 数据，用于验证页面分支覆盖、视觉密度和模板完整性。

## 快速开始

### 本地预览

```bash
jekyll serve
```

如果 `4000` 端口被占用：

```bash
jekyll serve --host 127.0.0.1 --port 4002
```

### 构建检查

```bash
jekyll build --source . --destination /tmp/jekyll-build
```

### 你最常改的地方

- 改站点文案和页头展示：
  编辑 `_config.yml`
- 改成员、论文、新闻、研究方向、招生信息：
  编辑 `_data/*.yml`
- 改页面结构和组件：
  编辑 `_includes/`、`_layouts/`、`pages/`、`index.md`
- 改视觉和交互：
  编辑 `assets/css/site.css`、`assets/js/site.js`

## 技术栈

- SSG: Jekyll 4
- Data: YAML 1.2
- UI: Tailwind CDN + 自定义 CSS/JS
- Automation: GitHub Actions + Python 同步脚本
- Content Sync: Feishu/Lark Bitable -> YAML

## 目录结构

- `_data/`
  站点内容数据源，当前包含 `groups.yml`、`team.yml`、`research.yml`、`publications.yml`、`news.yml`、`positions.yml`
- `_includes/`
  可复用组件，例如 `page-header.html`、`chapter-intro.html`、`narrative-band.html`、`publication-card.html`、`news-card.html`、`position-card.html`、`team-links.html`
- `_layouts/default.html`
  全站布局骨架、导航、页脚、语言与主题控制
- `assets/css/site.css`
  全站视觉 token、组件样式、动效和响应式规则
- `assets/js/site.js`
  语言切换、主题切换、移动端菜单和 reveal 动效
- `scripts/feishu_sync/`
  飞书同步的模块化实现
- `feishu_config.yml`
  飞书表到 `_data/*.yml` 的映射配置

## 数据文件说明

### `groups.yml`

定义团队分组和视觉色彩，`id` 需要与 `team.yml` 中的 `group_id` 对应。

```yaml
- id: "phd"
  title:
    zh: "博士研究生"
    en: "Ph.D. Students"
  color: "blue"
```

### `team.yml`

成员数据，支持双语姓名、身份、角色、简介、头像、邮箱、社交链接和校友去向。

```yaml
- name:
    zh: "姓名"
    en: "Name"
  group_id: "phd"
  rank: 10
  title:
    zh: "博士生"
    en: "Ph.D. Student"
  role:
    zh: "核心骨干"
    en: "Core Member"
  avatar: "/assets/images/team/default-avatar.svg"
  bio:
    zh: "中文简介"
    en: "English bio"
  email: "name@example.edu"
  destination:
    zh: "校友去向"
    en: "Alumni destination"
  links:
    homepage: "https://..."
    scholar: "https://..."
    github: "https://..."
```

### `research.yml`

研究方向数据，支持图标、双语标题、描述、图片和重点列表。

```yaml
- icon: "🔬"
  title:
    zh: "研究方向"
    en: "Research Area"
  description:
    zh: "中文简介"
    en: "English description"
  image: "/assets/images/research/example.svg"
  points:
    zh: ["细分方向 1", "细分方向 2"]
    en: ["Sub-field 1", "Sub-field 2"]
```

### `publications.yml`

论文数据，按 `year` 分组展示，支持类型、亮点、图片、摘要和资源链接。

```yaml
- title:
    zh: "中文论文标题"
    en: "English Paper Title"
  authors: "Author A, <b>Lab Member</b>*"
  type: "conference"
  venue: "CVPR 2026"
  year: 2026
  highlight: "Oral"
  image: "https://..."
  abstract:
    zh: "中文摘要"
    en: "English abstract"
  links:
    paper: "https://..."
    code: "https://..."
    project: "https://..."
```

### `news.yml`

新闻动态数据，用于首页和新闻页的时间线叙事。

```yaml
- date: "2026.03"
  category:
    zh: "开源项目"
    en: "Open Source"
  title:
    zh: "新闻标题"
    en: "News Title"
  description:
    zh: "中文描述"
    en: "English description"
  link: "https://..."
```

### `positions.yml`

招生与招聘数据，支持主题色、标签、人数和申请链接。

```yaml
- title:
    zh: "博士生 (空间智能方向)"
    en: "Ph.D. Candidates in Spatial Intelligence"
  count:
    zh: "2 名 / 年"
    en: "2 positions per year"
  department:
    zh: "智能系统研究中心"
    en: "Center for Intelligent Systems"
  icon: "🛰️"
  theme: "blue"
  description:
    zh: "岗位描述"
    en: "Position description"
  tags:
    zh: ["3D 视觉", "世界模型"]
    en: ["3D Vision", "World Models"]
  link: "https://..."
```

## 页面配置

页面级展示文案统一在 `_config.yml` 中配置，除了传统的 `hero` 和各页面 header 之外，还支持以下扩展字段：

- `eyebrow_notes`
  页头或首页顶部的小型展示标签
- `facts`
  页头右侧的事实条与辅助说明
- `join_process`
  Join 页面中的申请步骤、邮件主题建议和沟通说明
- `cta_bands`
  页面底部 narrative band 的标题、描述、按钮和侧栏列表
- `stage_tags`
  首页 Hero 视觉舞台中的主题标签

这些配置不会改变 `_data` schema，只负责驱动页面展示层。

## 内容维护速查

### 只想改页面内容

1. 修改 `_data/*.yml` 或 `_config.yml`
2. 运行 `jekyll serve`
3. 检查中英文、深浅色、移动端

### 只想改视觉表现

1. 修改 `assets/css/site.css`
2. 如需交互，再改 `assets/js/site.js`
3. 打开首页、Research、Publications、People、News、Contact 六页回归检查

### 只想改模板结构

1. 优先改 `_includes/` 里的共享组件
2. 再改 `pages/*.md` 和 `index.md`
3. 最后执行一次 `jekyll build`

## 本地开发

安装好本机 Jekyll 环境后，在仓库根目录运行：

```bash
jekyll serve
```

如果默认端口 `4000` 被占用，可以指定端口：

```bash
jekyll serve --host 127.0.0.1 --port 4002
```

构建检查：

```bash
jekyll build --source . --destination /tmp/jekyll-build
```

## 当前内容策略

- `_data/` 里现在是用于页面验证的 mock 数据，不代表真实成员或真实论文
- 页面已经采用展览感设计系统，优先复用共享组件，而不是在页面里重复写结构
- `team.yml` 是正式团队数据文件名，不再使用旧的 `people.yml`

## 飞书同步

飞书同步采用模块化脚本结构：

- `scripts/feishu_sync/config.py`
- `scripts/feishu_sync/reader.py`
- `scripts/feishu_sync/converters.py`
- `scripts/feishu_sync/validators.py`
- `scripts/feishu_sync/pipeline.py`

运行同步前需要准备环境变量：

- `FEISHU_APP_ID`
- `FEISHU_APP_SECRET`
- `FEISHU_APP_TOKEN`

`feishu_config.yml` 现在默认通过 `app_token_env` 读取 `FEISHU_APP_TOKEN`，不再把 app token 明文写进仓库。

### 自动同步

仓库已经内置 GitHub Actions 自动同步工作流 [sync.yml](/Users/wbzuo/Documents/04-Developer/Source-Code/github/cdi-lv-group.github.io/.github/workflows/sync.yml)。

只要你在仓库的 GitHub Secrets 中配置好下面 3 个值：

- `FEISHU_APP_ID`
- `FEISHU_APP_SECRET`
- `FEISHU_APP_TOKEN`

它就会自动执行：

- 每天 1 次从飞书多维表拉取最新数据，当前计划时间约为北京时间 08:00
- 自动更新 `_data/` 和 `assets/images/`
- 数据有变化时自动提交并推送到 `main`
- 你也可以在 GitHub Actions 页面手动点 `Run workflow` 立即同步

如果你当前 `_data/` 里放的是页面验证用 mock 数据，请注意：自动同步会用飞书真实数据覆盖这些文件。

本地运行同步脚本前，请先安装 Python 依赖：

```bash
pip install -r requirements.txt
```

常用入口：

```bash
python scripts/sync_all.py
python scripts/init_feishu_table.py
python scripts/seed_mock_to_feishu.py --yes
```

入口脚本：

- `scripts/sync_all.py`
- `scripts/test.py`
- `scripts/seed_mock_to_feishu.py`

表名、输出文件与 converter 映射在 `feishu_config.yml` 中维护。当前团队数据的正式输出文件名为 `_data/team.yml`，不再使用旧的 `people.yml` 命名。

### 单独把 mock 数据写入飞书

如果你想单独用仓库里的模拟数据回填飞书表，而不是从飞书拉取真实数据，可以使用：

```bash
python scripts/seed_mock_to_feishu.py --yes
```

这条命令会：

- 读取 [feishu_seed.yml](/Users/wbzuo/Documents/04-Developer/Source-Code/github/cdi-lv-group.github.io/mock_data/feishu_seed.yml) 中的独立 mock 数据
- 清空当前受管飞书表中的现有记录
- 为每张表重新写入 1 条示例行和整套 mock 记录

注意：

- 这条命令会改写飞书表中的现有内容，所以必须显式加 `--yes`
- 当前版本会尝试把 mock 数据里的本地图片和远程图片上传到飞书附件字段；如果单张图片下载或上传失败，会跳过该附件，但仍继续写入文本字段
- `positions` 里的 `cyan` 主题会自动回退为 `blue`，以兼容现有飞书选项配置
- 运行前仍然需要配置 `FEISHU_APP_ID`、`FEISHU_APP_SECRET`、`FEISHU_APP_TOKEN`

### 直接通过 GitHub Actions 写入 mock 数据

如果你不想在本地跑脚本，也可以直接通过 GitHub Actions 执行：

1. 打开仓库的 `Actions`
2. 选择 `Seed Mock Data to Feishu`
3. 点击 `Run workflow`
4. 在 `confirm` 输入框里填写：`SEED_MOCK_TO_FEISHU`
5. 保持默认的 `data_file=mock_data/feishu_seed.yml`，或者换成你自己的 mock 文件

对应工作流文件是 [seed-mock-to-feishu.yml](/Users/wbzuo/Documents/04-Developer/Source-Code/github/cdi-lv-group.github.io/.github/workflows/seed-mock-to-feishu.yml)。

这条 Action 只会：

- 读取仓库里的 mock 数据文件
- 调用 [seed_mock_to_feishu.py](/Users/wbzuo/Documents/04-Developer/Source-Code/github/cdi-lv-group.github.io/scripts/seed_mock_to_feishu.py)
- 直接改写飞书多维表内容，并尝试同步 `Avatar` / `Image` 附件

它不会提交 Git 仓库内容，也不会替代现在每天自动运行的 [sync.yml](/Users/wbzuo/Documents/04-Developer/Source-Code/github/cdi-lv-group.github.io/.github/workflows/sync.yml)。

## 设计系统说明

当前前端采用一套展览感视觉系统，核心组件包括：

- `stage`
  主舞台式内容容器，用于首页 Hero、Research 章节、精选论文和核心岗位
- `panel`
  轻量信息面板，用于补充事实、摘要和次级说明
- `rail`
  纵向信息强调条，用于章节、年份或去向信息
- `band`
  叙事型 CTA 横幅，用于页面尾部的承接与转化
- `chip`
  元信息标签，用于类型、分类、角色和小型状态信息

## 建议流程

### 直接维护 YAML

1. 修改 `_data/*.yml`
2. 本地运行 `jekyll serve`
3. 验证中英文、深浅色、移动端布局
4. 提交变更

### 通过飞书维护

1. 在飞书多维表中维护内容
2. 配置 `feishu_config.yml`
3. 运行同步脚本生成 `_data/*.yml`
4. 再执行 `jekyll build` 或 `jekyll serve` 验证页面

## 备注

- 当前仓库可能处于脏工作区，请在提交前确认哪些改动属于你本次要保留的内容
- `_site/`、`.jekyll-cache/`、`.DS_Store` 已加入 `.gitignore`
- mock 数据仅用于页面验证，不代表真实实验室成员与成果

## License

MIT
