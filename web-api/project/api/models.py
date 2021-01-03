from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class Calculation(models.Model):
    result = ArrayField(models.IntegerField())
    time_in_s = models.FloatField()
    max_memory_in_MB = models.FloatField()

    def __init__(self, result, time_in_s, max_memory_in_MB):
        self.result = result
        self.time_in_s = time_in_s
        self.max_memory_in_MB = max_memory_in_MB


class Info(models.Model):
    n = models.IntegerField()
    m = models.IntegerField()
    points = ArrayField(models.CharField(max_length=10))
