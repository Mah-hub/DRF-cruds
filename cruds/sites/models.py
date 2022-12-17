from django.db import models
from items.models import Item

# Create your models here.
class Site(models.Model):
    code        = models.CharField(max_length=255,primary_key=True)
    country     = models.CharField(max_length=255)
    state       = models.CharField(max_length=255,blank=True)
    items       = models.ManyToManyField(Item)

    def __str__(self):
        return (self.code)