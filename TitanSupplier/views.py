from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from Users.models import Client
from django.utils import timezone
from orders.models import FlintwoodOrders, BiotechOrders, TktitanOrders
from .forms import ProductForm, searchForm
from TKTitan.models import Product
import random
import string

User = get_user_model()
def supplier_view(request):
	if request.user.is_authenticated:
	    currentUser = request.user
	else:
	    return redirect('/Users/login/')

	template = loader.get_template('members/Supplier.html')
	pform = ProductForm(request.POST,request.FILES or None)
	sform = searchForm(request.POST or None)
	size = len(Product.objects.filter(tksupplierid= currentUser.id))
	print(size)
	output = "products"
	if size == 1:
		output = str(size)+" product"
	else:
		output = str(size)+" products"
	context ={
		'user_content':  Product.objects.filter(tksupplierid= currentUser.id),
		'num_products' :output,
	    'user_name': currentUser.username,
        'times' : timezone.now(),
        'pform' : pform,
        'sform' : sform,
		'user': Client.objects.filter(user=request.user),

	}


	print('Tumefika pform.is_valid()')
	if pform.is_valid():
		print('Tumefika hapa')
		item = pform.cleaned_data.get('Item_Name')
		brand = pform.cleaned_data.get('Brand_Name')
		unit = pform.cleaned_data.get('Units_in_Kg_litres_or_grams')
		cate = pform.cleaned_data.get('Category')
		pack = pform.cleaned_data.get('Unit_per_pack')
		price = pform.cleaned_data.get('Price_In_USD')
		stock = pform.cleaned_data.get('Stock')
		description = pform.cleaned_data.get('Description')
		origin = pform.cleaned_data.get('Country_of_origin')
		pic = pform.cleaned_data.get('Attach_picture')
		password_characters =string.digits
		ids=int( ''.join(random.choice(password_characters) for i in range(6)))

		new_product = Product(pid=ids,name=item,Brand_Name=brand,
			description=description,origin=origin,price=price,image= pic,stock=stock,Unit=unit,tksupplierid=currentUser, Packaging=pack,Active=False)
		new_product.save()
		return HttpResponseRedirect('/BTTitanSupplier/')

	context['pform']= ProductForm()
	return HttpResponse(template.render(context,request))
