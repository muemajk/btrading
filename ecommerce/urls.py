from django.urls import include, path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('logout/', views.logout_view, name='logout_view'),
  	path('admin/',views.admin_page, name = 'admin_page'),
    path('membership/', views.membership_view, name = 'membership_view'),
    path('Company/', views.company_view, name='company_view'),
    path('Biotec/', views.biotec_view, name='biotec_view'),
    path('Flint/', views.flint_view, name='flint_view'),
    path('Tktitan/', views.tk_view, name='tk_view'),
    path('AboutUs/', views.about_view, name='about_view'),
]
