# Writing and Redaing Data via models in Django

### 1. Install Dataclass
```
pip install dataclasses
```

### 2. Data in a pyhon class
```
python
from dataclasses import dataclass
```

```
@dataclass
... class BlogPost:
...     title: str
...     content: str
... 
>>> obj =  BlogPost(title="Hello World", content="This is cool")
```

### 3. Data in a Django Model Class
```
from django.db import models

class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
```
### Writing
```
obj = Article(title="This is my first title", content="Hello world") 
obj.save()
print(obj.id)
```
or
```
obj2 = Article.objects.create(title="This is my other title", content="Hello again")
print(obj.id)
```
### Reading
```
a = Articles.objects.get(id=3)
```

### 4. Data in original home view
```
from django.http import HttpResponse
from articles.models import Article
import random

def home_view(request):
    """
    Take in a request 
    Return HTML response
    """
    #Hard coded
    name = "Sylvain"
    #Pseudo random
    random_id = random.randint(1, 3)
    #From databases
    article_obj = Article.objects.get(id=random_id)

    context = {
        "content": article_obj.content,
        "id": article_obj.id,
        "title": article_obj.title,
    }
    #Django Templates
    HTML_STRING = """<h1>{title} {id}</h1>
    <p>{content}</p>""".format(**context)
    return HttpResponse(HTML_STRING)
```