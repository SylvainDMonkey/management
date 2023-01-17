from django.conf import settings
from django.db import models
from django.db.models import Q
from django.urls import reverse

from .utils import number_str_to_float
from .validators import validate_unit_of_measure

import pint

# Create your models here.

class RecipeQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()
        lookups = (
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(directions__icontains=query)
            )
        return self.filter(lookups)
    
class RecipeManager(models.Manager):
    def get_queryset(self):
        return RecipeQuerySet(self.model, using=self._db)
    
    def search(self, query=None):
        return self.get_queryset().search(query=query)

class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    directions = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    objects = RecipeManager()
    
    @property
    def title(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("recipes:detail", kwargs={"id": self.id})
    
    def get_absolute_hx_url(self):
        return reverse("recipes:hx-detail", kwargs={"id": self.id})
    
    def get_delete_url(self):
        return reverse("recipes:delete", kwargs={"id": self.id})
    
    def get_edit_url(self):
        return reverse("recipes:update", kwargs={"id": self.id})
    
    def get_ingredients_children(self):
        return self.recipeingredient_set.all()
    
    
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    quantity = models.CharField(max_length=50)
    quantity_as_float = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=50, validators=[validate_unit_of_measure])
    directions = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def get_absolute_url(self):
        return self.recipe.get_absolute_url()
    
    def get_delete_url(self):
        kwargs = {
            "parent_id": self.recipe.id,
            "id": self.id,
        }
        return reverse("recipes:ingredient-delete", kwargs=kwargs)
    
    def get_hx_edit_url(self):
        kwargs = {
            "parent_id": self.recipe.id,
            "id": self.id,
        }
        return reverse("recipes:hx-ingredient-update", kwargs=kwargs)
    
    def convert_to_system(self, system="mks"):
        if self.quantity_as_float is None:
            return None
        ureg = pint.UnitRegistry(system=system)
        measurement = self.quantity_as_float * ureg[self.unit]
        return measurement
    
    def to_grams(self):
        grams = self.convert_to_system()
        return grams.to('grams')
    
    def as_mks(self):
        #meter, kilogram, second
        measurement = self.convert_to_system(system="mks")
        return measurement.to_base_units()
        
    def as_imperial(self):
        #miles, pounds, seconds
        measurement = measurement = self.convert_to_system(system="imperial")
        return measurement.to_base_units()
    
    def save(self, *args, **kwargs):
        qty = self.quantity
        qty_as_float, qty_as_float_success = number_str_to_float(qty)
        if qty_as_float_success:
            self.quantity_as_float = qty_as_float
        else:
            self.quantity_as_float = None
        super().save(*args, **kwargs)
        

# class RecipeImage():
#     recipe = models.ForeignKey(Recipe)