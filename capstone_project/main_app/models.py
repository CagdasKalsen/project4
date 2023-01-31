from django.db import models

# Create your models here.

CATEGORY_CHOICES = (
    ('NA', 'New Arrivals'),
    ('BS', 'Best Sellers'),
    ('M', 'Man'),
    ('W', 'Women'), )


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.CharField(max_length=250)
    description = models.TextField(max_length=250)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)

    def __str__(self):
        return self.name
