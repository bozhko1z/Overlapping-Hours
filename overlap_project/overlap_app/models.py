from django.contrib.auth.models import User
from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shops')

    def __str__(self):
        return self.name


class WorkingHours(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='working_hours')
    day = models.CharField(max_length=20)
    start = models.TimeField()
    end = models.TimeField()

    def __str__(self):
        return self.day
