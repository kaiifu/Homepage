---
permalink: /team/
title: "团队成员"
author_profile: true
---

## 负责人

<ul class="member-list">
  <li>
    <strong>{{ site.data.members.leader.name_en }}｜{{ site.data.members.leader.name_zh }}</strong>
    {{ site.data.members.leader.title }}，{{ site.data.members.leader.role }}<br>
    研究兴趣：{{ site.data.members.leader.interests | join: '、' }}
  </li>
</ul>

{% if site.data.members.current_students and site.data.members.current_students != empty %}
## 在读学生

<ul class="member-list">
{% for person in site.data.members.current_students %}
  <li>
    <strong>{{ person.name }}</strong>
    {% if person.role %}{{ person.role }}{% endif %}{% if person.research %} · {{ person.research }}{% endif %}
  </li>
{% endfor %}
</ul>
{% endif %}

{% if site.data.members.alumni and site.data.members.alumni != empty %}
## 毕业成员

<ul class="member-list">
{% for person in site.data.members.alumni %}
  <li>
    <strong>{{ person.name }}</strong>
    {% if person.role %}{{ person.role }}{% endif %}{% if person.destination %} · {{ person.destination }}{% endif %}
  </li>
{% endfor %}
</ul>
{% endif %}

成员信息将随着课题组建设逐步补充；没有内容的分组不会显示。
