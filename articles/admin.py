from django.contrib import admin

# Register your models here.
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'timestamp', 'updated']
    search_fields = ['title', 'id']

admin.site.register(Article, ArticleAdmin)