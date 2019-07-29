from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from Users.models import Client
from django.utils import timezone
from orders.models import FlintwoodOrders, BiotechOrders, TktitanOrders
from .forms import ProductForm, searchForm

from TKTitan.models import Product


User = get_user_model()
def supplier_view(request):
	if request.user.is_authenticated:
	    currentUser = request.user
	else:
	    return redirect('/Users/login/')

	template = loader.get_template('members/Supplier.html')
	pform = ProductForm(request.POST or None)
	sform = searchForm(request.POST or None)

	context ={
		'user_content':  Product.objects.all(),
	    'user_name': currentUser.username,
        'times' : timezone.now(),
        'pform' : pform,
        'sform' : sform,
		'user': Client.objects.filter(user=request.user),

	}
	return HttpResponse(template.render(context,request))
