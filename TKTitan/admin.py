from django.contrib import admin

# Register your models here.
from .models import Product, ProductCatergory 

admin.site.register(Product)
admin.site.register(ProductCatergory)