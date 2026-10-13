---
permalink: /contact/
title: "联系我们"
author_profile: true
---

## AIFu Lab

**AI 融合电磁设计课题组**  
AI-Fused Electromagnetic Design Group

{% assign profile = site.data.site %}
{% if profile.parent_lab %}**隶属实验室：** {{ profile.parent_lab }}  {% endif %}
{% if profile.department %}**院系：** {{ profile.department }}  {% endif %}
{% if profile.institution %}**学校：** {{ profile.institution }}  {% endif %}
{% if profile.address %}**地址：** {{ profile.address }}  {% endif %}
{% if profile.email %}**邮箱：** [{{ profile.email }}](mailto:{{ profile.email }})  {% endif %}

{% if profile.links and profile.links != empty %}
## 学术主页

<p class="compact-links">
{% for link in profile.links %}
  <a href="{{ link.url }}" rel="noopener noreferrer">{{ link.label }}</a>
{% endfor %}
</p>
{% endif %}

如咨询保研或毕业设计，请在来信中简要说明专业背景、感兴趣的方向、已有课程或项目经验，以及希望开展研究的时间安排。
