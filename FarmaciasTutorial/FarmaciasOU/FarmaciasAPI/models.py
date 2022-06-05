from statistics import mode
from django.db import models

class Farmacia(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=75)
