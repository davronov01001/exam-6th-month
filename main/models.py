from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.


class User(AbstractUser):
    pass


class Category(models.Model):
    title = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title


class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    photo = models.ImageField(upload_to='main_photo', blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    creation_time = models.DateTimeField(auto_now_add=True)
    views = models.BigIntegerField(default=0, blank=True)


