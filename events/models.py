from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=254)
    starts = models.DateTimeField()
    ends = models.DateTimeField()
    location_name = models.CharField(max_length=254, null=True, blank=True)
    location_postcode = models.CharField(max_length=8, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available_tickets = models.IntegerField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name