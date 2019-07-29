"""btresources URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
	path('', include(('ecommerce.urls', 'ecommerce'), namespace='ecommerce')),
	path('admin/', admin.site.urls),
	path('Flintwood/', include(('Flintwood.urls','Flintwood'), namespace='Flintwood')),
	path('TKTitan/', include(('TKTitan.urls','TKTitan'), namespace='TKTitan')),
	path('Biotec/', include(('Biotech.urls','Biotech'), namespace='Biotech')),
	path('orders/', include(('orders.urls','orders'), namespace='orders')),
	path('Users/', include('Users.urls')),
	path('Supplier/', include(('Supplier.urls','Supplier'), namespace='Supplier')),
	path('FlintwoodSupplier/', include(('FlintSupplier.urls','FlintSupplier'), namespace='FlintSupplier')),
	path('BiotecSupplier/', include(('BiotechSupplier.urls','BiotecSupplier'), namespace='BiotecSupplier')),
	path('BTTitanSupplier/', include(('TitanSupplier.urls','BTTitanSupplier'), namespace='BTTitanSupplier')),
	path('adminstrator/', include(('adminstrator.urls','adminstrator'), namespace='adminstrator')),		
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)