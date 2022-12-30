from django.db import models

# Create your models here.

class Item(models.Model):
    project = models.CharField(max_length=255,blank=True)
    code    = models.CharField(max_length=255,blank=False)
    price   = models.FloatField(blank=False)

    # In this class Meta, we defined the two fields that should be primary together.
    # which are the project and code.
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['project', 'code'], name='unique_migration_host_combination'
            )
        ]
        
    def __str__(self):
            return (self.code)

class Site(models.Model):
    code        = models.CharField(max_length=255,primary_key=True)
    country     = models.CharField(max_length=255)
    state       = models.CharField(max_length=255,blank=True)
    items       = models.ManyToManyField(Item)

    def __str__(self):
        return (self.code)

class ItemSite(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['item', 'site'], name='unique_migration_host'
            )
        ]

    


