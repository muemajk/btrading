from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('store/', views.store_page, name = 'store_page'),
    path('Ordering/', views.boiordercatch, name = 'boiordercatch'),
    path('product/<int:pk>/', views.product_page, name = 'product_page'),
    path('Cart/<int:pk>/<int:size>/', views.addtoCart, name='addtoCart'),
    path('Cart/', views.cart_view, name='cart_view'),
    path('Deletecart/<int:pk>/', views.delete_from_cart, name='delete_from_cart'),
    path('Updatecart/', views.calculate_cart, name='calculate_cart'),
    path('Clearcart/<int:pk>/', views.clear_whole_cart, name='clear_whole_cart'),
    path('checkout/<int:pk>/', views.checkout, name = 'checkout'),

]