from django.urls import path

from . import views


urlpatterns = [
   
    path('logout/', views.logout_view, name='logout_view'),
    path('profile/', views.profile_view, name='profile_view'),
    #path('supplier/', views.supplier_view, name='supplier_view'),
  	path('admin/',views.admin_page, name = 'admin_page'),
    path('login/', views.login_page, name = 'login_page'),

    path('register/', views.register_page, name = 'register_page'),

    path('DeleteUser/<int:pk>/', views.delete_from_user, name = 'delete_from_user'),
    path('UpdateUserpassword/<int:pk>/', views.update_password_to_user, name = 'update_password_to_user'),
    path('UpdateUserphone/<int:pk>/', views.update_phone_to_user, name = 'update_phone_to_user'),
    path('UpdateUseraddress/<int:pk>/', views.update_address_to_user, name = 'update_address_to_user'),
    path('UpdateUseremail/<int:pk>/', views.update_email_to_user, name = 'update_email_to_user'),
        
    
    

]