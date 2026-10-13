---
permalink: /team/
title: "团队成员"
author_profile: false
---

## 负责人

<div class="people-grid people-grid--leader">
  {% include member-card.html person=site.data.members.leader %}
</div>

<p class="compact-links"><a href="{{ '/cv/' | relative_url }}">个人简历</a><a href="{{ '/contact/' | relative_url }}">联系方式</a></p>

{% assign graduate_students = site.data.members.graduate_students %}
{% assign undergraduate_students = site.data.members.undergraduate_students %}
{% if graduate_students != empty %}
## 研究生

<div class="people-grid">
{% for person in graduate_students %}
  {% include member-card.html person=person %}
{% endfor %}
</div>
{% endif %}
{% if undergraduate_students != empty %}
## 本科生

<div class="people-grid">
{% for person in undergraduate_students %}
  {% include member-card.html person=person %}
{% endfor %}
</div>
{% endif %}
{% if site.data.members.alumni and site.data.members.alumni != empty %}
## 毕业成员

<div class="people-grid">
{% for person in site.data.members.alumni %}
  {% include member-card.html person=person %}
{% endfor %}
</div>
{% endif %}
{% comment %}End of team listing.{% endcomment %}
