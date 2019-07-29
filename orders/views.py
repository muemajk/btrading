from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from orders.models import FlintwoodOrders, BiotechOrders, TktitanOrders
from django.utils import timezone
from adminstrator.models import freightRate
from decimal import Decimal
import string
from random import *
from Biotech.models import Cart
from Flintwood.models import FlintCart
from TKTitan.models import TKCart
from Users.models import Client
from TKTitan.forms import  Checkoutform



#this page view will display all orders made
def index(request):
    template = loader.get_template('ecommerce/members/Userdetails.html')


    return HttpResponse(template.render(context,request))


def orders_view(request):
    currentUser = request.session['userID']
    try:
        memeber = Member.objects.filter(Userid=currentUser)
        for mem in memeber:
            meme = mem.id
            memphone = mem.phone_number
            memcountry = mem.country
            memphysical_address = mem.physical_address
            mempriv = mem.privilege
    except  AttributeError as error:
        return redirect('/ecommerce/logout/')
        print(error)
    form = Checkoutform(request.POST or None)

    if mempriv == "flintwood":
        pass
    ordercart = Cart.objects.filter(Member_ID=meme)

    context = {
        'phone': memphone,
        'country': memcountry,
        'address':  memphysical_address,
        'form': form,
        'ordersize': 0,
        'user': Client.objects.filter(user=request.user),
    }

    if form.is_valid():
        username = form.cleaned_data.get("cardcode")

    for order in ordercart:
        sizeord = len(ordercart)
        context['ordersize'] = sizeord

    template = loader.get_template('ecommerce/products/cart.html')
    return HttpResponse(template.render(context,request))




def orders(request, company, price):
    if request.user.is_authenticated:
        currentUser = request.user
        userid = currentUser.id
        by_client = Client.objects.filter(user=userid)
        pk = ""
        for client in by_client:
            pk = client.id
    else:
         return   redirect('/Users/login/')

    form = Checkoutform(request.POST or None)
    min_char = 10
    max_char = 12
    allchar = string.ascii_letters + string.digits

    #get prices and TKCart info
    if company == 'tktitan':
        print(pk)
        context = {
            'userz': currentUser,
            'num_prod': 'num_prod',
            'add_prod': 'add_prod',
            'phone_num': 'phone_num',
            'serialCode': '213312weeqw',
            'price_prod': 'price',
            'product_list': 'prod',
            'times' : timezone.now(),
            'form': 'ghf',
            'user_name':request.user.username,
            'comp': 'TKTITAN',
            'user': Client.objects.filter(user=request.user),
        }
        to_buy = TKCart.objects.filter(User_ID=userid)
        size_to_buy = 0
        total = 0.0
        total = Decimal(total)
        print(to_buy)
        for cart in to_buy:
            size_to_buy =size_to_buy+cart.count
            value_of_TKCart = cart.price * cart.count
            rates = freightRate.objects.filter(Product_types='Mineral')

            for rate in rates:
                print(cart.count)
                if cart.count >= rate.MiniQuantitySent & cart.count <= rate.MaxQuantityRecieved:
                    finalcost =rate.Total_cost
                    by_client = Client.objects.filter(user=userid)
                    for client in by_client:
                        context['phone_num']=client.phonenumber
                        context['add_prod']= client.physical_address
                    context['num_prod']= size_to_buy

                    context['serialCode'] = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
                    context['form'] = Checkoutform()
                    context['product_list'] = to_buy
                total= total + value_of_TKCart
        context['price_prod']=total + finalcost
        template = loader.get_template('products/tkcheckout.html')
        return HttpResponse(template.render(context,request))

    elif company == 'biotech':
        context = {
            'userz': currentUser,
            'num_prod': 'num_prod',
            'add_prod': 'add_prod',
            'phone_num': 'phone_num',
            'serialCode': '213312weeqw',
            'price_prod': 'price',
            'product_list': 'prod',
            'times' : timezone.now(),
            'form': 'ghf',
            'user_name':request.user.username,
            'comp': 'TKTITAN',
            'user': Client.objects.filter(user=request.user),
        }
        to_buy = Cart.objects.filter(User_ID=userid)
        size_to_buy = 0
        total = 0.0
        total = int(total)
        for cart in to_buy:
            size_to_buy =size_to_buy+cart.count
            value_of_bioCart = cart.price * cart.count
            rates = freightRate.objects.filter(Product_types='Medicine')
            for rate in rates:
                if cart.count >= rate.MiniQuantitySent & cart.count <= rate.MaxQuantityRecieved:
                    finalcost = rate.Total_cost
                    by_client = Client.objects.filter(user=userid)
                    for client in by_client:
                        context['phone_num']=client.phonenumber
                        context['add_prod']= client.physical_address
                    context['num_prod']= size_to_buy

                    context['serialCode'] = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
                    context['form'] = Checkoutform()
                    context['product_list'] = to_buy
                total= total + value_of_bioCart
        context['price_prod']=total + finalcost
        template = loader.get_template('products/checkout.html')
        return HttpResponse(template.render(context,request))


    elif company == 'flintwood':
        context = {
            'userz': currentUser,
            'num_prod': 'num_prod',
            'add_prod': 'add_prod',
            'phone_num': 'phone_num',
            'serialCode': '213312weeqw',
            'price_prod': 'price',
            'product_list': 'prod',
            'times' : timezone.now(),
            'form': 'ghf',
            'user_name':request.user.username,
            'comp': 'TKTITAN',
            'user': Client.objects.filter(user=request.user)
        }
        to_buy = FlintCart.objects.filter(User_ID=userid)
        size_to_buy = 0
        total = 0.0
        total = int(total)
        for cart in to_buy:

            size_to_buy =size_to_buy+cart.count
            value_of_flCart = cart.price * cart.count
            rates = freightRate.objects.filter(Product_types='fresh_food')
            for rate in rates:
                if cart.count >= rate.MiniQuantitySent & cart.count <= rate.MaxQuantityRecieved:
                    finalcost = rate.Total_cost
                    print('Niko hapa')
                    by_client = Client.objects.filter(user=userid)
                    for client in by_client:
                        context['phone_num']=client.phonenumber
                        context['add_prod']= client.physical_address
                    context['num_prod']= size_to_buy

                    context['serialCode'] = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
                    context['form'] = Checkoutform()
                    context['product_list'] = to_buy
                total= total + value_of_flCart
        context['price_prod']=total + finalcost
        template = loader.get_template('products/flintcheckout.html')
        return HttpResponse(template.render(context,request))








def ordercatch(request , company):
    if request.user.is_authenticated:
        currentUser = request.user
        userid = currentUser.id
        by_client = Client.objects.filter(user=userid)

    else:
         return   redirect('/Users/login/')

    if company=='flintwood':
        cartorders= FlintCart.objects.filter(User_ID = userid)
        ordlist = []
        ordval = ''
        count = 1
        for orders in cartorders:

            ordval = str(count)+').'+ orders.Product_name +'('+str(orders.count)+ "),"
            count += 1
            ordlist.append(ordval)

        #print(ordlist)

        min_char = 10
        max_char = 12
        allchar = string.ascii_letters + string.digits
        serialcode = "".join(choice(allchar) for x in range(randint(min_char, max_char)))

        products_ordered = ''.join(ordlist)



        print(products_ordered)
        neword = FlintwoodOrders(OrderID=serialcode,OrderDate= timezone.now(),OrderList=products_ordered,Order_Payment=False,user=currentUser)
        neword.save()
        return   redirect('/Users/profile/')

    if company=='biotech':
        cartorders= Cart.objects.filter(User_ID = userid)
        ordlist = []
        ordval = ''
        count = 1
        for orders in cartorders:

            ordval = str(count)+').'+ orders.Product_name +'('+str(orders.count)+ "),"
            count += 1
            ordlist.append(ordval)

        #print(ordlist)

        min_char = 10
        max_char = 12
        allchar = string.ascii_letters + string.digits
        serialcode = "".join(choice(allchar) for x in range(randint(min_char, max_char)))

        products_ordered = ''.join(ordlist)



        print(products_ordered)
        neword = BiotechOrders(OrderID=serialcode,OrderDate= timezone.now(),OrderList=products_ordered,Order_Payment=False,user=currentUser)
        neword.save()
        return   redirect('/Users/profile/')

    if company=='tktitan':
        cartorders= TKCart.objects.filter(User_ID = userid)
        ordlist = []
        ordval = ''
        count = 1
        for orders in cartorders:

            ordval = str(count)+').'+ orders.Product_name +'('+str(orders.count)+ "),"
            count += 1
            ordlist.append(ordval)

        #print(ordlist)

        min_char = 10
        max_char = 12
        allchar = string.ascii_letters + string.digits
        serialcode = "".join(choice(allchar) for x in range(randint(min_char, max_char)))

        products_ordered = ''.join(ordlist)



        print(products_ordered)
        neword = TktitanOrders(OrderID=serialcode,OrderDate= timezone.now(),OrderList=products_ordered,Order_Payment=False,user=currentUser)
        neword.save()
        return   redirect('/Users/profile/')
