from django.db import models

from django.utils import timezone

from django.contrib.auth.models import User

from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 100)


    def __str__(self):
        return self.name 


class Post(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_at = models.DateTimeField(default = timezone.now)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.pk])



