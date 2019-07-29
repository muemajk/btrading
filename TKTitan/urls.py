from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('store/', views.store_page, name = 'store_page'),
    path('Ordering/', views.tkordercatch, name = 'tkordercatch'),
    path('product/<int:pk>/', views.product_page, name = 'product_page'),
    path('TKCart/<int:pk>/<int:size>/', views.addtoTKCart, name='addtoTKCart'),
    path('TKCart/', views.TKCart_view, name='TKCart_view'),
    path('DeleteTKCart/<int:pk>/', views.delete_from_TKCart, name='delete_from_TKCart'),
    path('UpdateTKCart/', views.calculate_TKCart, name='calculate_TKCart'),
    path('ClearTKCart/<int:pk>/', views.clear_whole_TKCart, name='clear_whole_TKCart'),
    path('checkout/<int:pk>/', views.checkout, name = 'checkout'),

]