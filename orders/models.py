from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.


class FlintwoodOrders(models.Model):
	 OrderID = models.CharField(max_length=100, primary_key=True)
	 OrderDate = models.DateField()
	 OrderList = models.CharField(max_length=2000)
	 Order_Payment = models.BooleanField(default= False)
	 user = models.ForeignKey(User, on_delete=models.CASCADE, default= 1)


class BiotechOrders(models.Model):
	 OrderID = models.CharField(max_length=100, primary_key=True)
	 OrderDate = models.DateField()
	 OrderList = models.CharField(max_length=2000)
	 Order_Payment = models.BooleanField(default= False)
	 user = models.ForeignKey(User, on_delete=models.CASCADE,  default= 1)

class TktitanOrders(models.Model):
	 OrderID = models.CharField(max_length=100, primary_key=True)
	 OrderDate = models.DateField()
	 OrderList = models.CharField(max_length=2000)
	 Order_Payment = models.BooleanField(default= False)
	 user = models.ForeignKey(User, on_delete=models.CASCADE,  default= 1)
