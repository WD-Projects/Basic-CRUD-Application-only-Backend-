from django.db import models
class Tasks(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    rating = models.IntegerField()