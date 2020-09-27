#!/usr/bin/env python3
# coding: utf-8

FLAGS=dict(
  cz=u"🇨🇿",
  de=u"🇩🇪",
  fr=u"🇫🇷",
  uk=u"🇬🇧",
  us=u"🇺🇸",
  id=u"🇮🇩",
  www=u"🌐",
)

TEMPLATE="""<html>
<head>
  <title>{{ title }}</title>
  <link rel="stylesheet" href="index.css">
  <meta charset="UTF-8">
</head>
<body>
  <div class="main">
    <table>
      <tr><td class="header" colspan="3">{{ title }}</td></tr>
      <tr><td class="details" colspan="3">Note: while some session are delivered in Indonesian, slides are always in English.</td></tr>

      {% if coming_soon %}
        <tr><td class="title" colspan="3">Coming soon</td></tr>

        {% for item in coming_soon %}
          <tr>
            <td>{{ item.flag }} {{ item.title }}</td>
            <td>{% if item.slides %}<a class="slides" href="{{ item.slides }}" />{% endif %}</td>
            <td>{% if item.attend %}<a class="attend" href="{{ item.attend }}" />
            {% else %}
              <p class="details">{{ item.status }}</p>
            {% endif %}</td>
          </tr>
          <tr>
            <td class="details">Scheduled {{ item.prettydate }} at {{ item.event }} in {{item.city }}.</td>
          </tr>
        {% endfor %}
      {% endif %}

      {% if recorded_workshops %}
        <tr><td class="title" colspan="3">Recorded session</td></tr>

        {% for item in recorded_workshops %}
          <tr>
            <td>{{ item.title }}</td>
            <td><a class="slides" href="{{ item.slides }}" /></td>
            <td><a class="video" href="{{ item.video }}" /></td>
          </tr>
          <tr>
            <td class="details">Delivered {{ item.prettydate }} at {{ item.event }} in {{item.city }}.</td>
          </tr>
        {% endfor %}
      {% endif %}

      {% if self_paced_golang %}
        <tr><td class="title" colspan="3">Golang</td></tr>
        {% for item in self_paced_golang %}
          <tr>
            <td>{{ item.flag }} {{ item.title }}</td>
            <td><a class="slides" href="{{ item.slides }}" /></td>
            <td>{% if item.video %}<a class="video" href="{{ item.video }}" />{% endif %}</td>
          </tr>
        {% endfor %}
      {% endif %}

      {% if self_paced_docker %}
        <tr><td class="title" colspan="3">Docker</td></tr>
        {% for item in self_paced_docker %}
          <tr>
            <td>{{ item.flag }} {{ item.title }}</td>
            <td><a class="slides" href="{{ item.slides }}" /></td>
          </tr>
        {% endfor %}
      {% endif %}

      <tr><td class="spacer"></td></tr>

      <tr>
        <td class="footer">
          Maintained by Imam Kurniawan and Forked from <a href="https://github.com/jpetazzo/container.training/tree/master/slides">J.Petazzo's Container Training</a>.
        </td>
      </tr>
    </table>
  </div>
</body>
</html>"""

import datetime
import jinja2
import yaml

items = yaml.safe_load(open("index.yaml"))


def prettyparse(date):
    months = [
      "January", "February", "March", "April", "May", "June",
      "July", "August", "September", "October", "November", "December"
    ]
    month = months[date.month-1]
    suffix = {
            1: "st", 2: "nd", 3: "rd",
            21: "st", 22: "nd", 23: "rd",
            31: "st"}.get(date.day, "th")
    return date.year, month, "{}{}".format(date.day, suffix)


# Items with a date correspond to scheduled sessions.
# Items without a date correspond to self-paced content.
# The date should be specified as a string (e.g. 2018-11-26).
# It can also be a list of two elements (e.g. [2018-11-26, 2018-11-28]).
# The latter indicates an event spanning multiple dates.
# The event will be considered "current" (shown in the list of
# upcoming events) until the second date.

for item in items:
    if "date" in item:
        date = item["date"]
        if type(date) == list:
            date_begin, date_end = date
        else:
            date_begin, date_end = date, date
        y1, m1, d1 = prettyparse(date_begin)
        y2, m2, d2 = prettyparse(date_end)
        if (y1, m1, d1) == (y2, m2, d2):
            # Single day event
            pretty_date = "{} {}, {}".format(m1, d1, y1)
        elif (y1, m1) == (y2, m2):
            # Multi-day event within a single month
            pretty_date = "{} {}-{}, {}".format(m1, d1, d2, y1)
        elif y1 == y2:
            # Multi-day event spanning more than a month
            pretty_date = "{} {}-{} {}, {}".format(m1, d1, m2, d2, y1)
        else:
            # Event spanning the turn of the year (REALLY???)
            pretty_date = "{} {}, {}-{} {}, {}".format(m1, d1, y1, m2, d2, y2)
        item["begin"] = date_begin
        item["end"] = date_end
        item["prettydate"] = pretty_date
    item["flag"] = FLAGS.get(item.get("country"),"")
    item["cat"] = item.get("category")

today = datetime.date.today()
coming_soon = [i for i in items if i.get("date") and i["end"] >= today]
coming_soon.sort(key=lambda i: i["begin"])
self_paced_golang = [i for i in items if not i.get("date") and i["cat"] == "golang"]
self_paced_docker = [i for i in items if not i.get("date") and i["cat"] == "docker"]
recorded_workshops = [i for i in items if i.get("video")]

template = jinja2.Template(TEMPLATE)
with open("index.html", "w") as f:
    f.write(template.render(
    	title="ISAT Dev Training",
    	coming_soon=coming_soon,
    	self_paced_golang=self_paced_golang,
    	self_paced_docker=self_paced_docker,
    	recorded_workshops=recorded_workshops
    	))
