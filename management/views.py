from django.http import HttpResponse
from django.template.loader import render_to_string

from articles.models import Article

import random

def home_view(request, *args, **kwargs):
    """
    Take in a request 
    Return HTML response
    """
    print(id)
    #Hard coded
    name = "Sylvain"
    #Pseudo random
    random_id = random.randint(1, 3)
    #From databases
    article_obj = Article.objects.get(id=random_id)
    article_queryset = Article.objects.all()
    context = {
        "object_list": article_queryset,
        "object" : article_obj,
        "content": article_obj.content,
        "id": article_obj.id,
        "title": article_obj.title,
    }
    #Django Templates
    HTML_STRING = render_to_string("home-view.html", context=context)
    return HttpResponse(HTML_STRING)