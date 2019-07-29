from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('store/', views.store_page, name = 'store_page'),
    path('Ordering/', views.flintordercatch, name = 'flintordercatch'),
    path('product/<int:pk>/', views.product_page, name = 'product_page'),
    path('FlintCart/<int:pk>/<int:size>/', views.addtoFlintCart, name='addtoFlintCart'),
    path('FlintCart/', views.FlintCart_view, name='FlintCart_view'),
    path('DeleteFlintCart/<int:pk>/', views.delete_from_FlintCart, name='delete_from_FlintCart'),
    path('UpdateFlintCart/', views.calculate_FlintCart, name='calculate_FlintCart'),
    path('ClearFlintCart/<int:pk>/', views.clear_whole_FlintCart, name='clear_whole_FlintCart'),
    path('checkout/<int:pk>/', views.checkout, name = 'checkout'),

]