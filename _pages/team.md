---
permalink: /team/
title: "团队成员"
author_profile: true
---

## 负责人

<div class="people-grid people-grid--leader">
  {% include member-card.html person=site.data.members.leader %}
</div>

<p class="compact-links"><a href="{{ '/cv/' | relative_url }}">个人简历</a><a href="{{ '/contact/' | relative_url }}">联系方式</a></p>

{% if site.data.members.current_students and site.data.members.current_students != empty %}
## 在读学生

<div class="people-grid">
{% for person in site.data.members.current_students %}
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

<p class="section-note">成员信息将随着课题组建设逐步补充；没有内容的分组不会显示。</p>
