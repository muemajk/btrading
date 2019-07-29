from django.shortcuts import render
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from Flintwood.models import Product,  ProductCatergory, FlintCart
from Users.models import Client
from orders.models import FlintwoodOrders
from django.utils import timezone
from django.urls import reverse
from decimal import Decimal
import string
from random import *
import json
from .forms import  Checkoutform, Productnumber
from adminstrator.models import freightRate


# Create your views here.
def index(request):
    template = loader.get_template('members/Userdetails.html')


    return HttpResponse(template.render(context,request))

#this view is for the homepage. it contains the product catalog
def store_page(request):
    if request.user.is_authenticated:
        currentUser = request.user
        userid = currentUser.id
        by_client = Client.objects.filter(user=userid)
        priv = ""
        for client in by_client:
            priv = client.privilege
        if priv == 'flintwood' or priv == 'all':
            request.session['userID']= userid
        else:
            return   redirect('/Users/login/')
    else:
         return   redirect('/Users/login/')
    usez = None
    context = {
        'user_content':  Product.objects.filter(Active=True),
        'user_name': usez,
        'times' : timezone.now(),
        'img': 'none',
        'comp': 'FLINTWOOD',
        'user': Client.objects.filter(user=request.user),
    }
    pic=''
    photo =  Product.objects.all()
    for pho in photo:
        pic = str(pho.image)
        print(pic)
    if request.user.is_authenticated:
        username = request.user.username
        context['user_content'] =  Product.objects.filter(Active=True)
        context['user_name']= username
        context['img'] = pic
    template = loader.get_template('products/flintstore.html')


    return HttpResponse(template.render(context,request))



#this view is for the individual product picked. it contains the product information
def product_page(request, pk):
    if request.user.is_authenticated:
        currentUser = request.user
        userid = currentUser.id
        by_client = Client.objects.filter(user=userid)
        priv = ""
        for client in by_client:
            priv = client.privilege
        if priv == 'flintwood' or priv == 'all':
            request.session['userID']= userid
        else:
            return   redirect('/Users/login/')
    else:
         return   redirect('/Users/login/')
    user_name= None
    prod = get_object_or_404(Product,pid=pk)
    #for pro in prod:
    cat = prod.Product_Catergory
    print(cat)
    #prodcat= ProductCatergory.objects.filter(id=pro)
    prodcat = get_object_or_404(ProductCatergory, id=cat.id)
    form = Productnumber(request.POST or None)
    context = {
        'info' : prod,
        'cat' : prodcat.Catergory,
        'user': 4,
        'form': Productnumber(),
        'prod_count': 1,
        'user_name':request.user.username,
        'times' : timezone.now(),
        'comp': 'FLINTWOOD',
    }
    if form.is_valid():
        size = form.cleaned_data.get('size')
        context['prod_count']= size
    currentUser =request.session['userID']
    print(currentUser)
    context['user'] =  currentUser

    template = loader.get_template('products/flintinfo.html')
    return HttpResponse(template.render(context,request))


def addtoFlintCart(request, pk, size):
    if request.user.is_authenticated:
        currentUser = request.user
        userid = currentUser.id
        by_client = Client.objects.filter(user=userid)
        priv = ""
        for client in by_client:
            priv = client.privilege
        if priv == 'flintwood' or priv == 'all':
            request.session['userID']= userid
        else:
            return   redirect('/Users/login/')
    else:
         return   redirect('/Users/login/')
    #get user info
    currentUser = request.session['userID']

    #get product info
    pdo = Product.objects.get(pid=pk)
    Product_name = pdo.name
    #get Member info

    descr = pdo.description
    descr = descr[:375]

    newdes = descr + '...'
    bp = FlintCart(User_ID=request.user,Product_name=Product_name, Product_description=newdes, price=pdo.price , count =size, ProductID=pdo)
    bp.save()
    return redirect('/Flintwood/FlintCart/')


def FlintCart_view(request):
    if request.user.is_authenticated:
        currentUser = request.user
        userid = currentUser.id
        by_client = Client.objects.filter(user=userid)
        priv = ""
        for client in by_client:
            priv = client.privilege
        if priv == 'flintwood' or priv == 'all':
            request.session['userID']= userid
        else:
            return   redirect('/Users/login/')
    else:
         return   redirect('/Users/login/')
    currentUser = request.session['userID']
    #usern =request.session['Usern']
    form = Productnumber(request.POST or None)
    #usern = Users.objects.get(id= currentUser)
    #print(usern)
    #print(currentUser)

    FlintCartprods = FlintCart.objects.filter(User_ID=currentUser)

    Vat= {'KE': 0.875, 'UG': 0.965, 'NAM' : 0.905}
    context = {
        'FlintCart_content': '',
        'Userid': 4,
        'total_price': 0,
        'Vat':0,

        'memid': 0,
        'form': form,
        'user_name':request.user.username,
        'times' : timezone.now(),
        'comp': priv,
        'user': Client.objects.filter(user=request.user),
    }
    total = 0.0
    total = Decimal(total)


    value = 0
    finaltotal= 0
    counter = 0
    VaT = 0
    finalcost=0
    for flintcart in FlintCartprods:
        product_value = flintcart.price * flintcart.count
        rates = freightRate.objects.filter(Product_types='fresh_food')
        for rate in rates:
            VaT = rate.Total_cost
            if flintcart.count >= rate.MiniQuantitySent & flintcart.count <= rate.MaxQuantityRecieved:
                finalcost = VaT
        total = total + product_value
        total = round(total,2)
        context['Vat']= VaT
        counter= counter + 1

    context['final_price']= int(total + finalcost)
    if form.is_valid():
        newnum = form.cleaned_data.get('size')
        newid =  request.POST.get('ip')
        #newid =  form.cleaned_data.get('ip')
        print(newid)
        FlintCart.objects.filter(id=newid).update(count=newnum)
        return redirect('/Flintwood/FlintCart/')
    print(total)
    context['FlintCart_content'] = FlintCart.objects.filter(User_ID=currentUser)
    context['Userid'] =  currentUser
    context['total_price']=  int(total)


    context['memid'] = currentUser
    template = loader.get_template('products/flintcart.html')

    return HttpResponse(template.render(context,request))



def calculate_FlintCart(request):

    return redirect('/Flintwood/FlintCart/')

def delete_from_FlintCart(request, pk):
    FlintCart.objects.filter(id=pk).delete()
    return redirect('/Flintwood/FlintCart/')




def clear_whole_FlintCart(request, pk):
    FlintCart.objects.filter(User_ID=pk).delete()
    return redirect('/Flintwood/FlintCart/')




#this view is for the product checkout. it contains the product on 'add to FlintCart' checkout details
def checkout(request, pk):
    if request.user.is_authenticated:
        currentUser = request.user
        userid = currentUser.id
        by_client = Client.objects.filter(user=userid)
        priv = ""
        for client in by_client:
            priv = client.privilege
        if priv == 'flintwood' or priv == 'all':
            request.session['userID']= userid
        else:
            return   redirect('/Users/login/')
    else:
         return   redirect('/Users/login/')
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
    'comp': 'FLINTWOOD',
    }
    form = Checkoutform(request.POST or None)
    min_char = 10
    max_char = 12
    allchar = string.ascii_letters + string.digits

    #get prices and FlintCart info
    to_buy = FlintCart.objects.filter(User_ID=pk)
    size_to_buy = 0
    Vat= {'KE': 0.875, 'UG': 0.965, 'NAM' : 0.905}
    total = 0.0
    total = Decimal(total)
    VaT =Vat['KE']
    VaT = Decimal(VaT)
    finaltotal= 0.0
    for flintcart in to_buy:
        size_to_buy =size_to_buy+flintcart.count
        value_of_FlintCart = flintcart.price * flintcart.count
        total = total + value_of_FlintCart
        value = flintcart.count * VaT

    if total>0:
        finaltotal = total + value
        finaltotal = round(finaltotal,2)
    else:
        finaltotal = 0

    #get memeber info
    by_client = Client.objects.filter(user=pk)
    for client in by_client:
        context['phone_num']=client.phonenumber
        context['add_prod']= client.physical_address
    context['num_prod']= size_to_buy
    context['price_prod']=finaltotal
    context['serialCode'] = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    context['form'] = Checkoutform()
    context['product_list'] = to_buy
    template = loader.get_template('products/flintcheckout.html')
    return HttpResponse(template.render(context,request))


def flintordercatch(request):
    if request.user.is_authenticated:
        currentUser = request.user
        userid = currentUser.id
        by_client = Client.objects.filter(user=userid)
        priv = ""
        for client in by_client:
            priv = client.privilege
        if priv == 'flintwood' or priv == 'all':
            request.session['userID']= userid
        else:
            return   redirect('/Users/login/')
    else:
         return   redirect('/Users/login/')

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
