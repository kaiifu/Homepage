---
permalink: /research/
title: "研究方向"
author_profile: true
---

课题组以“人工智能算法赋能的电磁器件设计”为主线，当前聚焦天线设计与优化，并逐步向射频器件、智能 EDA 和领域大语言模型拓展。

## 当前重点

<ul class="research-list">
{% for item in site.data.research.current %}
  <li>
    <strong>{{ item.title }}</strong>
    <span class="section-note">{{ item.label_en }}</span><br>
    {{ item.description }}
  </li>
{% endfor %}
</ul>

## 后续拓展

<ul class="research-list">
{% for item in site.data.research.future %}
  <li>
    <strong>{{ item.title }}</strong>
    {{ item.description }}
  </li>
{% endfor %}
</ul>

研究方向会随课题进展和团队积累逐步扩展；尚处于规划阶段的内容与当前研究重点分开列出。
