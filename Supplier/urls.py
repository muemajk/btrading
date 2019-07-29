from django.urls import path

from . import views


urlpatterns = [
   
    path('', views.supplier_view, name='supplier_view'),
    
]