from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    PRIORITY_CHOICES = [
        ('L','low'),
        ('M','medium'),
        ('H','high')
    ]
    priority = models.CharField(choices=PRIORITY_CHOICES, default='medium')
    due_date = models.DateTimeField(default=timezone.now)
    STATUS_CHOICES = [
        ('P','pending'),
        ('IP','in-progress'),
        ('D','done')
    ]
    status = models.CharField(choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title

    