from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.



#Each category has its own products
class ProductCatergory(models.Model):
    Catergory = models.CharField(max_length=200)
    Catergory_summary = models.TextField(max_length=2000)
    class Meta:
        verbose_name_plural = 'Product Catergories'


class Product(models.Model):
    pid = models.IntegerField(primary_key=True, default=1)
    name = models.CharField(max_length=254, default='')
    Brand_Name = models.CharField(max_length=254, default='')
    Product_Catergory = models.CharField(max_length=254, default='Medicine')
    description = models.TextField(max_length=2000)
    origin = models.CharField(max_length=254, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='product_images')
    stock = models.IntegerField()
    Unit = models.CharField(max_length=254, default='grams')
    biosupplierid = models.ForeignKey(User, default=1, verbose_name = "User", on_delete = models.SET_DEFAULT, related_name='biotech_supplier')
    Packaging = models.CharField(max_length=254, default='')
    Active = models.BooleanField(default=False)


    def __str__(self):
        return str(self.name)


class Cart(models.Model):
    count = models.IntegerField()
    Product_name = models.CharField(max_length=254, default='')
    Product_description = models.TextField(max_length=2000,  default='' )
    price = models.DecimalField(max_digits=6, decimal_places=2,  default= 100)
    User_ID = models.ForeignKey(User, default=1, verbose_name = "User", on_delete = models.SET_DEFAULT)
    ProductID = models.ForeignKey(Product, default=1, verbose_name = "Product", on_delete = models.SET_DEFAULT)
    date_created = models.DateField(default=now )
    last_modified = models.DateField(default=now)

    class Meta:
        verbose_name_plural = 'Carts'
