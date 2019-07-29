from django.urls import path

from . import views


urlpatterns = [

    path('freightrate/', views.freight, name='freight'),
  	path('products/',views.product_view, name = 'product_view'),
    path('users/', views.buyers_view, name = 'buyers_view'),
    path('Deleteusers/<str:pk>/<int:pk2>/', views.delete_user_view, name = 'delete_user_view'),
    path('Deletefrieghtrate/<int:pk>/', views.delete_frieght_view, name = 'delete_frieght_view'),
    path('freights/', views.freight_view, name = 'freight_view'),
    path('orders/', views.order_view, name = 'order_view'),
    path('fulfilledorders/', views.finalied_order_view, name = 'finalied_order_view'),
    path('create/', views.create_admin, name = 'create_admin'),
    path('Deleteproduct/<str:comp>/<int:pk>/', views.delete_product, name = 'delete_product'),
    path('DeleteVerifiedproduct/<str:comp>/<int:pk>/', views.delete_verified_product, name = 'delete_verified_product'),
    path('verify/<str:comp>/<int:pk>/', views.verify, name = 'verify'),
    path('unverify/<str:comp>/<int:pk>/', views.unverify, name = 'unverify'),
    path('finaliseorder/<str:comp>/<str:pk>/', views.finalise_order, name = 'finalise_order'),
    path('deleteOrder/<str:comp>/<str:pk>/', views.delete_order, name = 'delete_order'),
    path('Verifyproduct/', views.verify_product, name = 'verify_product'),






]
