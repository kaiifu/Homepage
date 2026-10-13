---
permalink: /
title: "AI融合电磁设计课题组 (AIFuEM Group)"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

AIFuEM Group 由 **傅楷 副研究员** 负责，聚焦人工智能在电磁器件设计、优化与发现中的方法和应用。

<!-- ## 研究邻域

<ul class="research-list">
{% for item in site.data.research.current %}
  <li>
    <strong>{{ item.title }}</strong>
    <span class="section-note">{{ item.label_en }}</span><br>
    {{ item.description }}
  </li>
{% endfor %}
</ul>

[查看完整研究方向]({{ '/research/' | relative_url }}){: .aifu-link} -->

## 近期动态 Recent News
{: .home-accent-heading}

<ul class="news-list">
{% for item in site.data.news limit:5 %}
  <li>
    <span class="news-date">{{ item.date }} · {{ item.tag }}</span><br>
    <strong>{{ item.title }}</strong>{% if item.description %} — {{ item.description }}{% endif %}
  </li>
{% endfor %}
</ul>

## 加入我们 Join Us
{: .home-accent-heading}

课题组面向 **直博/申博**、**保研/考研** 和 **本科毕设** 学生开放。

欢迎对<u>AI 算法、大模型、AI Agents 在微波、电磁、集成电路、EDA、柔性电子等领域的应用</u>感兴趣的同学与我联系。

[查看招生与合作信息]({{ '/opportunities/' | relative_url }}){: .aifu-link}
