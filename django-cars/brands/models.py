from django.db import models
from django.core import validators as v
from .validators import validate_date

class Brand(models.Model):
    name=models.CharField(max_length=200, blank=False, unique=True)


class Car(models.Model):
    name=models.CharField(max_length=200, blank=False, unique=True)
    year=models.IntegerField(blank=False, validators=[validate_date])
    brand=models.ForeignKey(Brand, null=False, on_delete=models.CASCADE, related_name="cars")
# Create your models here.
