---
permalink: /research/
title: "研究方向"
author_profile: false
---

课题组以“人工智能算法赋能的电磁器件设计”为主线，当前聚焦天线设计与优化，并逐步向射频器件、智能 EDA 和领域大语言模型拓展。

## 当前重点

<div class="research-accordion">
{% for item in site.data.research.current %}
  <details class="research-card"{% if forloop.first %} open{% endif %}>
    <summary>
      <span class="research-card__index" aria-hidden="true">0{{ forloop.index }}</span>
      <span class="research-card__heading">
        <strong>{{ item.title }}</strong>
        {% if item.label_en %}<span>{{ item.label_en }}</span>{% endif %}
      </span>
      <span class="research-card__toggle" aria-hidden="true">+</span>
    </summary>
    <div class="research-card__body">
      <p>{{ item.description }}</p>
    </div>
  </details>
{% endfor %}
</div>

## 后续拓展

<div class="research-accordion research-accordion--future">
{% for item in site.data.research.future %}
  <details class="research-card research-card--future">
    <summary>
      <span class="research-card__index" aria-hidden="true">0{{ forloop.index }}</span>
      <span class="research-card__heading">
        <strong>{{ item.title }}</strong>
        {% if item.label_en %}<span>{{ item.label_en }}</span>{% endif %}
      </span>
      <span class="research-card__toggle" aria-hidden="true">+</span>
    </summary>
    <div class="research-card__body">
      <p>{{ item.description }}</p>
    </div>
  </details>
{% endfor %}
</div>
