---
permalink: /outputs/
title: "研究成果"
author_profile: false
---

## 期刊论文

{% assign output_index = 0 %}
<ol class="bibliography bibliography--numbered">
{% for item in site.data.outputs.journals %}
  {% assign output_index = output_index | plus: 1 %}
  <li>
    <span class="publication-number">[{{ output_index }}]</span>
    <span class="publication-entry">
      <strong>{{ item.title }}</strong>
      <span class="publication-meta">{{ item.authors }} · <em>{{ item.venue }}</em>{% if item.year %} · {{ item.year }}{% endif %}</span>
    </span>
  </li>
{% endfor %}
</ol>

## 会议论文

<ol class="bibliography bibliography--numbered">
{% for item in site.data.outputs.conferences %}
  {% assign output_index = output_index | plus: 1 %}
  <li>
    <span class="publication-number">[{{ output_index }}]</span>
    <span class="publication-entry">
      <strong>{{ item.title }}</strong>
      <span class="publication-meta">{{ item.authors }} · <em>{{ item.venue }}</em>{% if item.year %} · {{ item.year }}{% endif %}</span>
    </span>
  </li>
{% endfor %}
</ol>

{% if site.data.outputs.projects and site.data.outputs.projects != empty %}
## 项目

<ol class="bibliography bibliography--numbered">
{% for item in site.data.outputs.projects %}
  {% assign output_index = output_index | plus: 1 %}
  <li>
    <span class="publication-number">[{{ output_index }}]</span>
    <span class="publication-entry"><strong>{{ item.title }}</strong>{{ item.description }}</span>
  </li>
{% endfor %}
</ol>
{% endif %}

{% if site.data.outputs.student_outputs and site.data.outputs.student_outputs != empty %}
## 学生成果

<ol class="bibliography bibliography--numbered">
{% for item in site.data.outputs.student_outputs %}
  {% assign output_index = output_index | plus: 1 %}
  <li>
    <span class="publication-number">[{{ output_index }}]</span>
    <span class="publication-entry"><strong>{{ item.title }}</strong>{{ item.description }}</span>
  </li>
{% endfor %}
</ol>
{% endif %}
