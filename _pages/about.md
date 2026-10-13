---
permalink: /
title: "AI 融合电磁设计课题组"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

AIFu Lab（AI-Fused Electromagnetic Design Group）由 **傅凯副教授**负责，研究人工智能算法在电磁器件设计、优化与发现中的方法和应用。

现阶段的工作集中在 AI 辅助天线设计、参数优化与拓扑优化。我们关心的不只是算法指标，也关注电磁仿真代价、工程约束、可制造性以及方法在真实设计流程中的可用性。

## 当前研究重点

<ul class="research-list">
{% for item in site.data.research.current %}
  <li>
    <strong>{{ item.title }}</strong>
    <span class="section-note">{{ item.label_en }}</span><br>
    {{ item.description }}
  </li>
{% endfor %}
</ul>

[查看完整研究方向]({{ '/research/' | relative_url }})

## 近期动态

<ul class="news-list">
{% for item in site.data.news limit:5 %}
  <li>
    <span class="news-date">{{ item.date }} · {{ item.tag }}</span><br>
    <strong>{{ item.title }}</strong>{% if item.description %} — {{ item.description }}{% endif %}
  </li>
{% endfor %}
</ul>

## 招生与毕业设计

课题组面向保研学生和本科毕业设计学生开放。欢迎具有电磁场、微波、电子信息、计算机、人工智能或优化算法背景的同学联系交流。

[查看招生与合作信息]({{ '/opportunities/' | relative_url }})
