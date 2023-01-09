# 1. Override UserAdmin
```
User = get_user_model()
admin.site.unregister(User)

class RecipeInline(admin.StackedInline):
    #StackedInline has three fields by default; xtra allow to add a object by clicking on a + button
    model = Recipe
    extra = 0

class UserAdmin(admin.ModelAdmin):
    inlines = [RecipeInline]
    list_display = ['username']

admin.site.register(User, UserAdmin)
```
# 2. RecipeInline
```
class RecipeInline(admin.StackedInline):
    #StackedInline has three fields by default, extra allow to add a object by clicking on a + button
    model = Recipe
    extra = 0
```

# 2. Old version RecipeIngredientInline -> With a different visaul from admin
```
class RecipeIngredientInline(admin.TabularInline):
     model = RecipeIngredient
     fields = ["name", "quantity", "unit", "directions"]

admin.site.register(RecipeIngredient)
```