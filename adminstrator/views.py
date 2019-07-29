from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils import timezone
from .forms import FrieghtForm, RegisterForm
from .models import freightRate
from Users.models import Client
from django.contrib.auth.models import User
from Biotech.models import Product as bioproducts
from Flintwood.models import Product as flintproducts
from TKTitan.models import Product as btproducts
from orders.models import FlintwoodOrders,BiotechOrders,TktitanOrders

# Create your views here.
def freight_view(request):
	if request.user.is_authenticated:
		currentUser = request.user
		userid = currentUser.id
		by_client = Client.objects.filter(user=userid)
		priv = ""
		for client in by_client:
			priv = client.role
		if priv == 'Admin':
			request.session['userID']= userid
		else:
			return   redirect('/Users/login/')

	else:
		return redirect('/Users/login/')

	template = loader.get_template('admin/freight.html')
	fform = FrieghtForm(request.POST or None)


	context ={

	    'user_name': currentUser.username,
        'times' : timezone.now(),
        'fform' : fform,
		'user': Client.objects.filter(user=request.user)


	}

	if fform.is_valid():
		ptype = fform.cleaned_data.get('Product_types')
		source = fform.cleaned_data.get('Origin')
		desti = fform.cleaned_data.get('Destination_Country')
		means = fform.cleaned_data.get('Port_freight')
		sourcemeans = fform.cleaned_data.get('From_source_to_Port_freight')
		desmeans = fform.cleaned_data.get('From_port_to_destination_freight')
		metric = fform.cleaned_data.get('Metric')
		minsent = fform.cleaned_data.get('Minimum_Quantity_Sent')
		maxsent = fform.cleaned_data.get('Maximum_Quantity_Sent')
		minrecieve = fform.cleaned_data.get('Minimum_Quantity_Recieved')
		maxrecieve = fform.cleaned_data.get('Maximum_Quantity_Recieved')
		orgagent = fform.cleaned_data.get('Origin_Clearing_Agent')
		destagent = fform.cleaned_data.get('Destination_Clearing_Agent')
		tcost = fform.cleaned_data.get('Total_cost')
		ucost = fform.cleaned_data.get('Unit_cost')
		markup = fform.cleaned_data.get('Mark_up_Rate')
		stax = fform.cleaned_data.get('Source_tax')
		dtax = fform.cleaned_data.get('Destination_tax')
		sotax = fform.cleaned_data.get('Source_Other_tax')
		dotax = fform.cleaned_data.get('Destination_Other_tax')




		newrate = freightRate(Source=source, Destination=desti,Port_freight= means,From_source_to_Port_freight=sourcemeans,From_port_to_destination_freight=desmeans,metric=metric, MiniQuantitySent=minsent,MaxQuantitySent=maxsent, MiniQuantityRecieved=minrecieve,MaxQuantityRecieved=maxrecieve, Total_cost= tcost, Unit_cost  = ucost,Sourcetax=stax, Destinationtax= dtax,Sourceothertax= sotax,Destinationothertax= dotax,MarkupRate=markup,Product_types=ptype, DestinAgent=destagent, OriginAgent=orgagent,  )
		newrate.save()
		return HttpResponseRedirect('/adminstrator/freightrate/')
	return HttpResponse(template.render(context,request))

usr = get_user_model()
def freight(request):
	if request.user.is_authenticated:
		currentUser = request.user
		userid = currentUser.id
		by_client = Client.objects.filter(user=userid)
		priv = ""
		for client in by_client:
			priv = client.role
		if priv == 'Admin':
			request.session['userID']= userid
		else:
			return   redirect('/Users/login/')

	else:
	    return redirect('/Users/login/')

	template = loader.get_template('admin/freightview.html')
	fform = FrieghtForm(request.POST or None)


	context ={

	    'user_name': currentUser.username,
        'times' : timezone.now(),
		'user': Client.objects.filter(user=request.user),
        'freightrate_content': freightRate.objects.all()

	}


	return HttpResponse(template.render(context,request))



def product_view(request):

	if request.user.is_authenticated:
		currentUser = request.user
		userid = currentUser.id
		by_client = Client.objects.filter(user=userid)
		priv = ""
		for client in by_client:
			priv = client.role
		if priv == 'Admin':
			request.session['userID']= userid
		else:
			return   redirect('/Users/login/')
	else:
		return redirect('/Users/login/')
	print(flintproducts.objects.filter() )
	context={'user': Client.objects.filter(user=request.user),'flintproducts': flintproducts.objects.filter(Active=True),'user_name': currentUser.username,'times' : timezone.now(),'bioproducts': bioproducts.objects.filter(Active=True),'btproducts': btproducts.objects.filter(Active=True)}
	template = loader.get_template('admin/products.html')
	return HttpResponse(template.render(context,request))
def suppliers_view(request):
	pass


usr = get_user_model()
def buyers_view(request):
	if request.user.is_authenticated:
		currentUser = request.user
		userid = currentUser.id
		by_client = Client.objects.filter(user=userid)
		priv = ""
		for client in by_client:
			priv = client.role
		if priv == 'Admin':
			request.session['userID']= userid
		else:
			return   redirect('/Users/login/')

	else:
	    return redirect('/Users/login/')

	template = loader.get_template('admin/users.html')
	fform = FrieghtForm(request.POST or None)
	Userz =User.objects.all()
	print(Userz)
	context ={

	    'user_name': currentUser.username,
        'times' : timezone.now(),
        'usr' : User.objects.all(),
        'user_content': Client.objects.all(),
		'user': Client.objects.filter(user=request.user)

	}
	return HttpResponse(template.render(context,request))
def order_view(request):
	if request.user.is_authenticated:
		currentUser = request.user
		userid = currentUser.id
		by_client = Client.objects.filter(user=userid)
		priv = ""
		for client in by_client:
			priv = client.role
		if priv == 'Admin':
			request.session['userID']= userid
		else:
			return   redirect('/Users/login/')

	else:
	    return redirect('/Users/login/')

	template = loader.get_template('admin/orders.html')

	context ={

	    'user_name': currentUser.username,
        'times' : timezone.now(),
		'user': Client.objects.filter(user=request.user),
        'flordertomake': FlintwoodOrders.objects.filter(Order_Payment=False),
		'biordertomake': BiotechOrders.objects.filter(Order_Payment=False),
		'tkordertomake': TktitanOrders.objects.filter(Order_Payment=False),

	}


	return HttpResponse(template.render(context,request))

def finalied_order_view(request):
	if request.user.is_authenticated:
		currentUser = request.user
		userid = currentUser.id
		by_client = Client.objects.filter(user=userid)
		priv = ""
		for client in by_client:
			priv = client.role
		if priv == 'Admin':
			request.session['userID']= userid
		else:
			return   redirect('/Users/login/')

	else:
	    return redirect('/Users/login/')

	template = loader.get_template('admin/finaliseorders.html')

	context ={

	    'user_name': currentUser.username,
        'times' : timezone.now(),
		'user': Client.objects.filter(user=request.user),
        'flordertomake': FlintwoodOrders.objects.filter(Order_Payment=True),
		'biordertomake': BiotechOrders.objects.filter(Order_Payment=True),
		'tkordertomake': TktitanOrders.objects.filter(Order_Payment=True),

	}


	return HttpResponse(template.render(context,request))





def delete_user_view(request, pk,pk2):
	User.objects.filter(username=pk).delete()
	Client.objects.filter(id=pk2).delete()
	return HttpResponseRedirect('/adminstrator/users/')


def delete_frieght_view(request,pk):
	freightRate.objects.filter(id=pk).delete()
	return HttpResponseRedirect('/adminstrator/freightrate/')


Users = get_user_model()
def create_admin(request):
    if request.user.is_authenticated:
    	currentUser = request.user
    	userid = currentUser.id
    	by_client = Client.objects.filter(user=userid)
    	priv = ""
    	for client in by_client:
    		priv = client.role
    	if priv == 'Admin':
    		request.session['userID']= userid
    	else:
    		return   redirect('/Users/login/')

    else:
    	return redirect('/Users/login/')


    form = RegisterForm(request.POST or None)
    template = loader.get_template('members/register.html')
    context = {
        'form' : form,
		'user': Client.objects.filter(user=request.user)
    }
    if form.is_valid():

        user_name = form.cleaned_data.get("username")
        firstname = form.cleaned_data.get("firstname")
        lastname = form.cleaned_data.get("lastname")
        emailad = form.cleaned_data.get("email")
        phone = form.cleaned_data.get("phone")
        altphone = form.cleaned_data.get("Whatsapp_phone_number")
        skype = form.cleaned_data.get("Skype")
        wechat = form.cleaned_data.get("We_Chat")
        physical_address = form.cleaned_data.get("physical_address")
        country = form.cleaned_data.get("country")
        passwords = form.cleaned_data.get("password")
        priv = "all"
        role = "Admin"

        new_user = Users.objects.create_user(user_name, emailad, passwords)
        new_user.last_name = lastname
        new_user.first_name = firstname

        new_user.save()

        #print(role)
        user = authenticate(request, username=user_name, password=passwords)
        if user is not None:
            request.session['userID'] = ''
            #print(role)

            #user_logged_in.send(user.__class__, instance=user, request = request)
            if user is not None:
                currentUser = request.user
                new_client = Client(user=currentUser,physical_address=physical_address,role= role,privilege=priv,Country=country,phonenumber=phone, Alternate_phonenumber =altphone, WeChat=wechat , Skype= skype )
                new_client.save()

                if role == 'Admin':
                    return redirect('/adminstrator/users/')


                login(request,user)
                print(user)







    return HttpResponse(template.render(context,request))




def verify_product(request):
	if request.user.is_authenticated:
		currentUser = request.user
		userid = currentUser.id
		by_client = Client.objects.filter(user=userid)
		priv = ""
		for client in by_client:
			priv = client.role
		if priv == 'Admin':
			request.session['userID']= userid
		else:
			return   redirect('/Users/login/')
	else:
		return redirect('/Users/login/')
	print(flintproducts.objects.filter() )
	context={'user': Client.objects.filter(user=request.user),'flintproducts': flintproducts.objects.filter(Active=False),'user_name': currentUser.username,'times' : timezone.now(),'bioproducts': bioproducts.objects.filter(Active=False),'btproducts': btproducts.objects.filter(Active=False)}
	template = loader.get_template('admin/verifyproducts.html')
	return HttpResponse(template.render(context,request))




def verify(request, comp,pk):
	if comp == "Mineral":
		bt = btproducts.objects.get(pid=pk)
		bt.Active = True
		bt.save(update_fields=['Active'])
		return redirect('/adminstrator/Verifyproduct/')
	elif comp == "fresh_food":
		bt=flintproducts.objects.get(pid=pk)
		bt.Active = True
		bt.save(update_fields=['Active'])
		return redirect('/adminstrator/Verifyproduct/')
	elif comp == "Medicine":
		bioproducts.objects.get(pid=pk)
		bt.Active = True
		bt.save(update_fields=['Active'])
		return redirect('/adminstrator/Verifyproduct/')


def finalise_order(request, comp,pk):
	if comp == "Mineral":
		bt = TktitanOrders.objects.get(OrderID=pk)
		bt.Order_Payment = True
		bt.save(update_fields=['Order_Payment'])
		return redirect('/adminstrator/orders/')
	elif comp == "fresh_food":
		bt=FlintwoodOrders.objects.get(OrderID=pk)
		bt.Order_Payment = True
		bt.save(update_fields=['Order_Payment'])
		return redirect('/adminstrator/orders/')
	elif comp == "Medicine":
		bt = BiotechOrders.objects.get(OrderID=pk)
		bt.Order_Payment = True
		bt.save(update_fields=['Order_Payment'])
		return redirect('/adminstrator/orders/')


def unverify(request, comp,pk):
	if comp == "Mineral":
		bt = btproducts.objects.get(pid=pk)
		bt.Active = False
		bt.save(update_fields=['Active'])
		return redirect('/adminstrator/products/')
	elif comp == "fresh_food":
		bt=flintproducts.objects.get(pid=pk)
		bt.Active = False
		bt.save(update_fields=['Active'])
		return redirect('/adminstrator/products/')
	elif comp == "Medicine":
		bioproducts.objects.get(pid=pk)
		bt.Active = False
		bt.save(update_fields=['Active'])
		return redirect('/adminstrator/products/')




def delete_verified_product(request,comp,pk):
	if comp == "Mineral":
		btproducts.objects.filter(pid=pk).delete()
		return redirect('/adminstrator/products/')
	elif comp == "fresh_food":
		flintproducts.objects.filter(pid=pk).delete()
		return redirect('/adminstrator/products/')
	elif comp == "Medicine":
		bioproducts.objects.filter(pid=pk).delete()
		return redirect('/adminstrator/products/')



def delete_product(request,comp,pk):
	if comp == "Mineral":
		btproducts.objects.filter(pid=pk).delete()
		return redirect('/adminstrator/Verifyproduct/')
	elif comp == "fresh_food":
		flintproducts.objects.filter(pid=pk).delete()
		return redirect('/adminstrator/Verifyproduct/')
	elif comp == "Medicine":
		bioproducts.objects.filter(pid=pk).delete()
		return redirect('/adminstrator/Verifyproduct/')



def delete_order(request, comp,pk):
	if comp == "Mineral":
		bt = TktitanOrders.objects.get(OrderID=pk).delete()
		return redirect('/adminstrator/orders/')
	elif comp == "fresh_food":
		bt=FlintwoodOrders.objects.get(OrderID=pk).delete()
		return redirect('/adminstrator/orders/')
	elif comp == "Medicine":
		BiotechOrders.objects.get(OrderID=pk).delete()
		return redirect('/adminstrator/orders/')
