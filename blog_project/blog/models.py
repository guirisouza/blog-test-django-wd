from django.db import models


class Post(models.Model):
    slug = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    slug = models.CharField(max_lenght=60)
    title = models.CharField(max_lenght=60)