# Old Version class ArticleManager(models.Manager):
```
class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)
    def search(self, query=None):
        if query is not None or query == "":
            return self.get_queryset().none() #Return Article.objects.none() => []
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        #return Article.objects.filter(lookups)    
        return self.get_queryset().filter(lookups)
```