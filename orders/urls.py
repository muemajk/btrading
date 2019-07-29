from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('orders/<str:company>/<int:price>/', views.orders, name='orders'),
    path('ordercatch/<str:company>/', views.ordercatch, name='ordercatch'),

]
