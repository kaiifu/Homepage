<<<<<<< ours
# AIFu Lab Homepage

AIFu Lab（AI-Fused Electromagnetic Design Group）课题组主页，使用 Jekyll 构建并部署在 GitHub Pages。

## 内容维护

日常更新主要修改 `_data/` 中的数据文件：

- `_data/site.yml`：学校、学院、大实验室、地址、邮箱、负责人和外部链接；
- `_data/members.yml`：负责人、在读学生和毕业成员；
- `_data/news.yml`：近期动态；
- `_data/research.yml`：当前研究重点和未来拓展；
- `_data/outputs.yml`：期刊、会议、项目和学生成果；
- `_data/navigation.yml`：顶部导航。

各栏目正文位于仓库根目录的同名 HTML 文件中。所有空数组和空字段都会由模板自动隐藏。

## 首次发布前需要补充

在 `_data/site.yml` 中确认并填写：

- 现任学校与学院；
- 隶属的大实验室；
- 办公地址；
- 现用工作邮箱；
- CV PDF 路径（如需提供下载）。

在 `_data/members.yml` 中补充已获得公开授权的学生信息。负责人照片目前沿用旧主页中的 `images/photo1.jpg`，建议后续替换为近期正式肖像，并保持原文件路径或同步修改数据配置。

## 本地构建

安装 Ruby、Bundler 与 Jekyll 后，在仓库根目录运行：

```shell
jekyll serve --baseurl /Homepage
```

GitHub Pages 会使用 `_config.yml` 原生构建。站点已按 `/Homepage/` 子路径配置，不要把内部链接改成未经 `relative_url` 处理的根路径。

## 校验

源码静态检查：

```shell
python scripts/validate_site.py
```

在没有 Ruby/Jekyll 的机器上，`scripts/build_preview.py` 可配合 `python-liquid` 生成仅用于视觉 QA 的临时预览；生产发布仍以 GitHub Pages 的 Jekyll 构建为准。

## 旧版资源

旧版 HTML5 UP 样式、脚本和相册图片暂时保留在仓库中，但新版页面不再引用它们。确认新版稳定后，可另行归档清理。
=======
# Homepage
>>>>>>> theirs
