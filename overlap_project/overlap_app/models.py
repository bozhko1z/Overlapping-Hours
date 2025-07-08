from django.db import models

class WorkingHours(models.Model):
    day = models.CharField(max_length=20)
    start = models.CharField(max_length=20)
    end = models.CharField(max_length=20)

    def __str__(self):
        return self.day


