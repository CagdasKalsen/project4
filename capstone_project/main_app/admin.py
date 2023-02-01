from django.contrib import admin
from . models import Product
# Register your models here.


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    product_info = ['id', 'name', 'image', 'price', 'category', 'description']
