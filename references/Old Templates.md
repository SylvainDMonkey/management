# 1. ld template recipes/create-update view

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


# 2. Old template recipes/partials/forms.html

<form action="." method="POST" hx-post="." hx-swap="outerHTML">
    {% csrf_token %}
    {% for field in form %}
      <div class="{% if field.field.required %} {{ form.required_css_class }}{% endif %}">
        {{ field.errors }}
        {{ field.label_tag }} {{ field }}
        {% if field.help_text %}
          <p class="help">{{ field.help_text|safe }}</p>
        {% endif %}
      </div>
    {% endfor %} 

    {% if formset %}
      <h3>Ingredients</h3>
      {{ formset.management_form }}
      <div id="ingredient-form-list">
        {% for form in formset  %}
          <div class="ingredient-form">
            {{ form.as_p }}
          </div>
        {% endfor %}
      </div>    
      <div id="empty-form" class="hidden">{{ formset.empty_form.as_p }}</div>
      <button id="add-more" type="button">Add more</button>
    {% endif %}
    <div class="htmx-indicator">Loading...</div>
    <button class="htmx-inverted-indicator" type="submit">Save</button>
    {% if message %}
    <p>{{ message }}</p>
    {% endif %}