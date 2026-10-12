# AIFu Lab 学术主页实施计划

## 目标

在 `aifu-lab-redesign` 分支上，将现有单页 HTML5 UP 个人主页重构为可由 GitHub Pages 原生构建的 Jekyll 多页面课题组网站，同时保留旧版图片和可核实的履历、论文与学术链接。

## 实施步骤

### 1. 建立 Jekyll 基础结构

- 新增 `_config.yml`，配置站点名称、URL、`/Homepage` 子路径和默认布局。
- 新增 `_layouts/default.html` 与 `_layouts/page.html`。
- 新增 `_includes/header.html`、`navigation.html`、`footer.html`、`member-card.html`、`output-item.html` 和 `news-item.html`。
- 保留旧版资源文件，不执行删除；新版页面只引用必要资源。

### 2. 建立可维护的数据层

- 新增 `_data/site.yml`，保存品牌、负责人、研究定位和已核实的外部链接。
- 新增 `_data/navigation.yml`，定义八个导航入口。
- 新增 `_data/members.yml`，先配置负责人，学生与毕业成员保持空数组并由模板隐藏。
- 新增 `_data/news.yml`，记录站点升级这一真实动态。
- 新增 `_data/outputs.yml`，迁移现有主页的期刊论文和会议论文。
- 对现单位、大实验室、地址、现邮箱和 CV PDF 路径使用未发布空值，不在页面生成猜测信息。

### 3. 实现视觉系统

- 新增 `assets/css/aifu.css`，实现深色横幅、绿色强调、蓝色导航、浅蓝信息卡和响应式布局。
- 使用 CSS 构建抽象电磁场品牌图形，并明确其为装饰元素，不伪装成科研结果。
- 复用 `images/photo1.jpg` 作为负责人照片，并提供替代文字。
- 新增 `assets/js/aifu.js`，只处理移动端导航开关和当前年份。

### 4. 实现八个栏目

- 重写 `index.html`：品牌、负责人、近期动态。
- 新增 `research.html`：当前研究重点与未来拓展。
- 新增 `team.html`：负责人、在读学生、毕业成员，空分组隐藏。
- 新增 `outputs.html`：论文、项目、学生成果，按年份组织。
- 新增 `teaching.html`：明确当前以毕业设计为主，不宣称已承担课程。
- 新增 `opportunities.html`：保研、毕业设计、期待背景和合作方向。
- 新增 `contact.html`：只呈现已核实的联系方式与外部主页。
- 新增 `cv.html`：迁移可核实的教育与研究经历；仅在配置 PDF 后显示下载按钮。

### 5. 内容真实性与容错

- Liquid 模板对空数组、空链接和缺失图片做条件渲染。
- 不发布虚构学生、项目、机构、地址或邮箱。
- 未来方向统一使用“计划拓展”或“持续探索”措辞。
- 外部链接使用明确文字，并为新窗口链接增加安全属性。

### 6. 验证

- 检查 Ruby/Jekyll 可用性；可用时执行 `bundle exec jekyll build` 或 `jekyll build`。
- 若本机无 Jekyll，使用等效静态检查验证 YAML、Liquid 文件存在性、内部链接和资源路径，并记录限制。
- 启动本地预览服务器，验证首页返回成功状态。
- 在浏览器中检查桌面与移动端首页、研究、成果和招生页面。
- 检查所有导航链接、图片、CV 条件入口、空分组隐藏和 `/Homepage/` 子路径兼容性。
- 运行 Git 差异检查，确保未意外删除或改写旧版图片资源。

## 完成条件

- 八个栏目完整可访问；
- 首页符合已批准的视觉稿；
- 旧主页中可核实的成果已迁移；
- 未确认信息未公开显示；
- Jekyll 或等效验证通过；
- 桌面和移动端预览无关键布局错误；
- 所有改动保留在 `aifu-lab-redesign` 分支，未推送远端。

