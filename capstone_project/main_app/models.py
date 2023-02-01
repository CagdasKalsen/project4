from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


CATEGORY_CHOICES = (
    ('New_Arrivals', 'New Arrivals'),
    ('Best_Sellers', 'Best Sellers'),
    ('m', 'Man'),
    ('w', 'Women'),)


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.CharField(max_length=250)
    description = models.TextField(max_length=250)
    # category = models.ForeignKey(
    #     Category, on_delete=models.CASCADE, default=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)

    def __str__(self):
        return self.name
