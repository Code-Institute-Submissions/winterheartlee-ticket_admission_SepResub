from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.

class Event(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=254)
    starts = models.DateTimeField(null=True, blank=True)
    ends = models.DateTimeField(null=True, blank=True)
    location_name = models.CharField(max_length=254, null=True, blank=True)
    location_postcode = models.CharField(max_length=8, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    ticket_allocation = models.IntegerField()
    # ticket_stock = models.IntegerField(blank=True)
    image = models.ImageField(null=True, blank=True)
    user = models.CharField(max_length=254, blank=True, null=True)
    # user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user