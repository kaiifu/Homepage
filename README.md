# AIFu Lab Homepage

AIFu Lab（AI 融合电磁设计课题组）主页，基于开源的
[Academic Pages](https://github.com/academicpages/academicpages.github.io)
模板构建。

## 内容维护

- 站点信息与负责人资料：`_config.yml`、`_data/site.yml`
- 导航：`_data/navigation.yml`
- 新闻：`_data/news.yml`
- 团队：`_data/members.yml`
- 研究方向：`_data/research.yml`
- 论文、项目与学生成果：`_data/outputs.yml`
- 页面正文：`_pages/`

## GitHub Pages

推送到 `main` 后，由仓库现有的 GitHub Pages 分支发布流程自动构建并部署。
主题中的 Sass 已保持与该构建环境兼容。

## 学校主页上传包

在 GitHub Actions 中手动运行 **Build school upload ZIP**。完成后下载
`AIFuLab-school-upload` 构建产物，其中的
`AIFuLab-school-upload.zip` 根目录包含学校系统要求的 `index.html`。

## License

主题沿用 Academic Pages / Minimal Mistakes 的 MIT License，许可证文本见
`LICENSE`。
