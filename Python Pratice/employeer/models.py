from django.db import models

# Create your models here.
from django.db import models
class Person(models.Model):
    frist_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
