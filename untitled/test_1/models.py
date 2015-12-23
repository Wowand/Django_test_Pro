from django.db import models
from django.contrib import admin

# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=100)
    text = models.TextField()


class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)