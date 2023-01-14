from django.contrib.auth import get_user_model
from django.contrib import admin

# Register your models here.
from .models import Recipe, RecipeIngredient

User = get_user_model()
    
class RecipeIngredientInline(admin.StackedInline):
    #StackedInline has three fields by default; extra allow to add a object by clicking on a + button
    model = RecipeIngredient
    extra = 0
    readonly_fields = ['quantity_as_float', 'as_mks', 'as_imperial']
    #fields = ["name", "description", "quantity", "unit", "directions"]

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ["name", "user"]
    readonly_fields = ['timestamp', 'updated']
    raw_id_fields = ["user"]

admin.site.register(Recipe,RecipeAdmin)