---
permalink: /team/
title: "团队成员"
author_profile: true
---

## 负责人

<article class="archive__item">
  <h3 class="archive__item-title">{{ site.data.members.leader.name_en }} <span lang="zh-CN">{{ site.data.members.leader.name_zh }}</span></h3>
  <p class="page__meta">{{ site.data.members.leader.title }} · AIFu Lab {{ site.data.members.leader.role }}</p>
  <p class="archive__item-excerpt"><strong>研究方向：</strong>{{ site.data.members.leader.interests | join: '、' }}</p>
  <p class="compact-links"><a href="{{ '/cv/' | relative_url }}">个人简历</a><a href="{{ '/contact/' | relative_url }}">联系方式</a></p>
</article>

{% if site.data.members.current_students and site.data.members.current_students != empty %}
## 在读学生

{% for person in site.data.members.current_students %}
<article class="archive__item">
  <h3 class="archive__item-title">{{ person.name }}</h3>
  {% if person.role %}<p class="page__meta">{{ person.role }}</p>{% endif %}
  {% if person.research %}<p class="archive__item-excerpt"><strong>研究方向：</strong>{{ person.research }}</p>{% endif %}
</article>
{% endfor %}
{% endif %}

{% if site.data.members.alumni and site.data.members.alumni != empty %}
## 毕业成员

{% for person in site.data.members.alumni %}
<article class="archive__item">
  <h3 class="archive__item-title">{{ person.name }}</h3>
  {% if person.role %}<p class="page__meta">{{ person.role }}</p>{% endif %}
  {% if person.destination %}<p class="archive__item-excerpt"><strong>毕业去向：</strong>{{ person.destination }}</p>{% endif %}
</article>
{% endfor %}
{% endif %}

<p class="section-note">成员信息将随着课题组建设逐步补充；没有内容的分组不会显示。</p>
