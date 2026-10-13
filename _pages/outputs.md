---
permalink: /outputs/
title: "研究成果"
author_profile: true
---

以下成果按年份整理。后续可以继续补充论文链接、代码、项目和学生成果。

## 期刊论文

{% assign journal_groups = site.data.outputs.journals | group_by: 'year' %}
{% for group in journal_groups %}
### {{ group.name }}

<ol class="bibliography">
{% for item in group.items %}
  <li>
    <strong>{{ item.title }}</strong>
    <span class="publication-meta">{{ item.authors }} · <em>{{ item.venue }}</em></span>
  </li>
{% endfor %}
</ol>
{% endfor %}

## 会议论文

{% assign conference_groups = site.data.outputs.conferences | group_by: 'year' %}
{% for group in conference_groups %}
### {{ group.name }}

<ol class="bibliography">
{% for item in group.items %}
  <li>
    <strong>{{ item.title }}</strong>
    <span class="publication-meta">{{ item.authors }} · <em>{{ item.venue }}</em></span>
  </li>
{% endfor %}
</ol>
{% endfor %}

{% if site.data.outputs.projects and site.data.outputs.projects != empty %}
## 项目

<ul class="member-list">
{% for item in site.data.outputs.projects %}
  <li><strong>{{ item.title }}</strong>{{ item.description }}</li>
{% endfor %}
</ul>
{% endif %}

{% if site.data.outputs.student_outputs and site.data.outputs.student_outputs != empty %}
## 学生成果

<ul class="member-list">
{% for item in site.data.outputs.student_outputs %}
  <li><strong>{{ item.title }}</strong>{{ item.description }}</li>
{% endfor %}
</ul>
{% endif %}
