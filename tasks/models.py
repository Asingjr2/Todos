from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel

from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Category(BaseModel):
    cat_name = models.CharField(max_length=100)

    def __str__(self):
        return self.cat_name


class Task(BaseModel):
    task_name = models.CharField(max_length=254)
    category = models.ForeignKey(Category, related_name='task_cat', on_delete=models.CASCADE)
    importance = models.IntegerField(default=1)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_name

