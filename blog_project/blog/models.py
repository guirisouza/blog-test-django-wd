from django.db import models


class Category(models.Model):
    slug = models.CharField(max_length=60)
    title = models.CharField(max_length=60)

class Post(models.Model):
    slug = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    content = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)