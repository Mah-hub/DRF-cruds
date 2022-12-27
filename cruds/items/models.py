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
