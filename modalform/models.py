from django.db import models
from django.db.models.deletion import SET_NULL

class Category(models.Model):
    name = models.CharField('Category Name', max_length=50)


class Post(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=SET_NULL)