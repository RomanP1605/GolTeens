from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.name} ({self.id})'


# Create your models here.
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)

class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Title:{self.title} Id:{self.id} Content={self.content},  Created={self.created}'


