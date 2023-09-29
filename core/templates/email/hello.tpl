{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ name }}
{% endblock %}

{% block html %}
This is an <strong>html</strong> message.
<img src='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fphotos%2Fnature&psig=AOvVaw3PD0gBn-GS7GxEmWOojGwN&ust=1696082387293000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCKi0oLT9z4EDFQAAAAAdAAAAABAE'>
{% endblock %}