# Old version def article_search_view(request)
```
#from django.db.models import Q
def article_search_view(request):
    query_dict = request.GET #This is a dictionnary
    query = query_dict.get("query") #<input type="text" name="query" />
    query = request.GET.get("query")
    try:
        query = int(query_dict.get("query"))
        query = query_dict.get("query")
    except:
        query = None
    print(query)
    article_obj = None
    qs  =Article.objects.all()
    if query is not None:
        article_obj = Article.objects.get(id=query)
        qs = Article.objects.filter(title__icontains = query)
        lookups = Q(title__icontains = query) | Q(content__icontains = query)
        qs = Article.objects.filter(lookups)
        qs = Article.objects.search(query)
    context = {
        "object": article_obj,
        "object_list": qs,
    }
    return render(request, 'articles/search.html', context=context)
```

# Old version def article_create_view(request):
```
 @login_required
 def article_create_view(request):
     form = ArticleForm()
     context = {
         "form": ArticleForm()
     }
     if request.method == 'POST':
         form = ArticleForm(request.POST)
         context['form'] = form
         if form.is_valid():   
             title = form.cleaned_data.get("title")
             content = form.cleaned_data.get("content")
             article_object = Article.objects.create(title = title, content = content)
             context['object'] = article_object
             context['created'] = True
     return render(request, "articles/create.html", context=context)
```