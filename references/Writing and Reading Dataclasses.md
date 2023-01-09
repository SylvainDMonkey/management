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

### 3. Data in User Class with
```
from articles.models import Article
qs = Article.objects.filter(user__username='admin')
```
or
```
qs = Article.objects.filter(user__username__icontains='admin')