from django.conf import settings
from django.db import models

from recipes.models import Recipe


User = settings.AUTH_USER_MODEL

class MealStatus(models.TextChoices):
    PENDING = 'p', 'Pending'
    COMPLETED = 'c', 'Completed'
    EXPIRED = 'e', 'Expired'
    ABORTED = 'a', 'Aborted'

#Class MealStatus remplace cette liste de choix mais a une manière de coder différente (ex: eturn self.filter(status=MealStatus.PENDING) serait return self.filter(status='a'))
MEAL_CHOICES = [
    ('a', 'Aborted'),
    ('c', 'Completed'),
    ('e', 'Expired'),
    ('p'), 'Pending'
]

class MealQuerySet(models.QuerySet):
    def by_user_id(self, user_id):
        return self.filter(user_id=user_id)
    
    def by_userMeal(self, userMeal):
        return self.filter(userMeal=userMeal)
    
    def pending(self):
        return self.filter(status=MealStatus.PENDING)
    
    def completed(self):
        return self.filter(status=MealStatus.COMPLETED)
    
    def expired(self):
        return self.filter(status=MealStatus.EXPIRED)
    
    def aborted(self):
        return self.filter(status=MealStatus.ABORTED)
    
class MealManager(models.Manager):
    def get_queryset(self):
        return MealQuerySet(self.model, using=self._db)

class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=MealStatus.choices, default=MealStatus.PENDING)
    
    objects = MealManager()