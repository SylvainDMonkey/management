# 1. Old version def article_search_view(request)
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

# 2. Old version def article_create_view(request):
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

### 3. Data in original home view
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


# 4. Update view :
```
@login_required
def recipe_update_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    form = RecipeForm(request.POST or None, instance=obj)
    form_2 = RecipeIngredientForm(request.POST or None)
    context = {
        "form": form,
        "form_2": form_2,
        "object": obj
    }
    if all([form.is_valid(), form_2.is_valid()]):
        parent = form.save(commit=False)
        parent.save()
        child = form_2.save(commit=False)
        child.recipe = parent #If not indicated an error message shows up with NOT NULL constraint failed
        child.save()
        context['message'] = 'Data saved.'
    return render(request, "recipes/create-update.html", context)
```
@login_required
def recipe_update_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    form = RecipeForm(request.POST or None, instance=obj)
    form_2 = RecipeIngredientForm(request.POST or None)
    #obj.recipeingredient_set.all()
    ingredient_forms = []
    for ingredient_obj in obj.recipeingredient_set.all():
        ingredient_forms.append(
            RecipeIngredientForm(request.POST or None, instance=ingredient_obj)
        )
    context = {
        "form": form,
        "ingredient_forms": ingredient_forms,
        "object": obj
    }
    my_forms = all([form.is_valid() for form in ingredient_forms])
    if my_forms and form.is_valid():
        parent = form.save(commit=False)
        parent.save()
        for form_2 in ingredient_forms:
            child = form_2.save(commit=False)
            child.recipe = parent #If not indicated an error message shows up with NOT NULL constraint failed
            child.save()
        context['message'] = 'Data saved.'
    return render(request, "recipes/create-update.html", context) 
```