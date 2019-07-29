from django.contrib import admin

# Register your models here.
from .models import FlintwoodOrders, BiotechOrders, TktitanOrders

admin.site.register(FlintwoodOrders)
admin.site.register(BiotechOrders)
admin.site.register(TktitanOrders)