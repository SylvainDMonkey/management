# 1. Create-update view
```
{% extends 'base.html' %}

{% block content %}
  {% if message %}
    <p>{{ message }}</p>
  {% endif %}
  <div style="margin-top:30px;">
    <form action="." method="post">
      {% csrf_token %}
      {{ form.as_p }}

      {% if form_2 %}
        <h3>Ingredients</h3>
        {{ form_2.as_p }}
      {% endif %}
      <button type="submit">Save</button>
    </form>
  </div>
{% endblock %}
```