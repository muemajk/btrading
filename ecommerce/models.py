from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session
from django.db.models.signals import pre_save, post_save

from .signals import user_logged_in
#from .signals import object_viewed_signal
#from .utils import get_client_ip



# Create your models here.

user = get_user_model()
class Member(models.Model):
    phone_number = models.CharField(max_length=15)
    country = models.CharField(max_length=200,default='Kenya')
    physical_address =  models.CharField(max_length=200, default='Nairobi')
    privilege = models.CharField(max_length=10, default="Customer")
    Userid = models.ForeignKey(user, default=1, verbose_name = "UserID", on_delete = models.SET_DEFAULT)


    def __int__(self):
        return self.id

#Companies hold and sell diffent product type/category
class ProductCompany(models.Model):
    Company = models.CharField(max_length=200)
    Company_summary = models.TextField(max_length=2000)

    class Meta:
        verbose_name_plural = 'Product Companies'


#Each category has its own products
class ProductCatergory(models.Model):
    Catergory = models.CharField(max_length=200)
    Catergory_summary = models.TextField(max_length=2000)
    Product_company = models.ForeignKey(ProductCompany, default=1, verbose_name = "Company", on_delete = models.SET_DEFAULT)
    class Meta:
        verbose_name_plural = 'Product Catergories'


class Product(models.Model):
    pid = models.IntegerField(primary_key=True, default=1)
    name = models.CharField(max_length=254, default='')
    Product_Company = models.ForeignKey(ProductCompany,default=1,verbose_name = "Company", on_delete = models.SET_DEFAULT)
    Product_Catergory = models.ForeignKey(ProductCatergory,default=1,verbose_name = "Catergory", on_delete = models.SET_DEFAULT)
    description = models.TextField(max_length=2000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='product_images')
    stock = models.IntegerField()


    def __str__(self):
        return str(self.name)



class Cart(models.Model):
    Cart_slug = models.SlugField(max_length=50)
    count = models.IntegerField()
    Product_name = models.CharField(max_length=254, default='')
    Product_description = models.TextField(max_length=2000,  default='' )
    price = models.DecimalField(max_digits=6, decimal_places=2,  default= 100)
    Member_ID = models.ForeignKey(Member, default=1, verbose_name = "Member", on_delete = models.SET_DEFAULT)
    ProductID = models.ForeignKey(Product, default=1, verbose_name = "Product", on_delete = models.SET_DEFAULT)
    date_created = models.DateField(default=now )
    last_modified = models.DateField(default=now)

    class Meta:
        verbose_name_plural = 'LargeCart'


class UserSession(models.Model):
    Activeuser = models.ForeignKey(user, default=1, blank=True, null=True, on_delete = models.SET_DEFAULT)
    ip_address = models.CharField(max_length=220, blank=True, null=True)
    session_key = models.CharField(max_length= 100, blank = True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    ended = models.BooleanField(default=False)

    def end_session(self):
        session_key= self.session_key
        ended = self.ended
        try:
            Session.objects.get(pk=session_key).delete()
            self.active = False
            self.ended = True
            self.save()
        except:
            pass
        return self.ended

#def post_save_session_receiver(sender, instance, request, *args, **kwargs):
 #   if created:
 #       ps = UserSession.objects.filter(user=instance.user).exclude(id=instance.id)
 #       for i in qs:
 #           i.end_session()

#post_save.connect(post_save_session_receiver, sender = UserSession)

def user_logged_in_receiver(sender, instance, request, *args, **kwargs):
    print(instance)
    ip_address = "14.14"
    user = instance
    session_key = request.session.session_key
    UserSession.objects.create(
        Activeuser=user,
        ip_address=ip_address,
        session_key=session_key
        )

user_logged_in.connect(user_logged_in_receiver)

