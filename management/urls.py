"""management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

from accounts.views import (
    login_view,
    logout_view,
    register_view,
)

from .views import home_view
from meals.views import meal_queue_toggle_view
from search.views import search_view

urlpatterns = [
    #Home
    path('', home_view),
    #Admin
    path('admin/', admin.site.urls),
    #Accounts
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
    #Articles
    path('articles/', include('articles.urls')),
    #Meals
    path('meal-toggle/<int:recipe_id>', meal_queue_toggle_view, name='meal-toggle'),
    #Recipes
    path('pantry/recipes/', include('recipes.urls')),
    #Search
    path('search/', search_view, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
