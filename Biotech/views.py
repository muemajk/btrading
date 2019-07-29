from django.shortcuts import render
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from Biotech.models import Product,  ProductCatergory, Cart
from Users.models import Client
from orders.models import BiotechOrders
from django.utils import timezone
from django.urls import reverse
from decimal import Decimal
import string
from random import *
from adminstrator.models import freightRate
from .forms import  Checkoutform, Productnumber




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
        if priv == 'biotech' or priv == 'all':
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
        'comp': 'BIOTECH',
        'user': Client.objects.filter(user=request.user)
    }
    photo =  Product.objects.all()
    pic=''
    for pho in photo:
        pic = str(pho.image)
        print(pic)
    if request.user.is_authenticated:
        username = request.user.username
        context['user_content'] =  Product.objects.filter(Active=True)
        context['user_name']= username
        context['img'] = pic
    template = loader.get_template('products/store.html')


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
        if priv == 'biotech' or priv == 'all':
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
        'userss': 4,
        'form': Productnumber(),
        'prod_count': 1,
        'user_name':request.user.username,
        'times' : timezone.now(),
        'comp': 'BIOTECH',
        'user': Client.objects.filter(user=request.user),
    }
    if form.is_valid():
        size = form.cleaned_data.get('size')
        context['prod_count']= size
    currentUser =request.session['userID']
    print(currentUser)
    context['user'] =  currentUser

    template = loader.get_template('products/info.html')
    return HttpResponse(template.render(context,request))


def addtoCart(request, pk, size):
    if request.user.is_authenticated:
        currentUser = request.user
        userid = currentUser.id
        by_client = Client.objects.filter(user=userid)
        priv = ""
        for client in by_client:
            priv = client.privilege
        if priv == 'biotech' or priv == 'all':
            request.session['userID']= userid
        else:
            print('I dont know the privilegess')
            #return   redirect('/Users/login/')
    else:
        print('I dont know the logzzz')
         #return   redirect('/Users/login/')
    #get user info
    currentUser = request.session['userID']

    #get product info
    pdo = Product.objects.get(pid=pk)
    Product_name = pdo.name
    #get Member info

    descr = pdo.description
    descr = descr[:75]

    newdes = descr + '...'
    bp = Cart(User_ID=request.user,Product_name=Product_name, Product_description=newdes, price=pdo.price , count =size, ProductID=pdo)
    bp.save()
    return redirect('/Biotec/Cart/')


def cart_view(request):
    if request.user.is_authenticated:
        currentUser = request.user
        userid = currentUser.id
        by_client = Client.objects.filter(user=userid)
        priv = ""
        for client in by_client:
            priv = client.privilege

        if priv == 'biotech' or priv == 'all':
            request.session['userID']= userid
        else:
            print('I dont know the privilege')
           # return   redirect('/Users/login/')
    else:
        print('I dont know the logs')
         #return   redirect('/Users/login/')
    currentUser = request.session['userID']
    #usern =request.session['Usern']
    form = Productnumber(request.POST or None)
    #usern = Users.objects.get(id= currentUser)
    #print(usern)
    #print(currentUser)

    cartprods = Cart.objects.filter(User_ID=currentUser)

    Vat= {'KE': 0.875, 'UG': 0.965, 'NAM' : 0.905}
    context = {
        'cart_content': '',
        'Userid': 4,
        'total_price': 0,
        'Vat':0,

        'memid': 0,
        'form': form,
        'user_name':request.user.username,
        'times' : timezone.now(),
        'comp': priv,
        'user': Client.objects.filter(user=request.user)

    }
#start

    total = 0.0
    total = Decimal(total)

    VaT=0
    value = 0
    finaltotal= 0
    counter = 0
    for cart in cartprods:
        print(cart.count)
        product_value = cart.price * cart.count
        rates = freightRate.objects.filter(Product_types='Medicine')
        for rate in rates:
            VaT = rate.Total_cost
            if cart.count >= rate.MiniQuantitySent & cart.count <= rate.MaxQuantityRecieved:
                finalcost =VaT
        total = total + product_value
        total = round(total,2)
        context['Vat']= VaT
        counter= counter + 1

    context['final_price']= int(total+finalcost)

    #end

    if form.is_valid():
        newnum = form.cleaned_data.get('size')
        newid =  request.POST.get('ip')
        #newid =  form.cleaned_data.get('ip')
        print(newid)
        Cart.objects.filter(id=newid).update(count=newnum)
        return redirect('/Biotech/Cart/')
    #print(product_value)
    context['cart_content'] = Cart.objects.filter(User_ID=currentUser)
    context['Userid'] =  currentUser
    context['total_price']= int(total)


    context['memid'] = currentUser
    template = loader.get_template('products/cart.html')

    return HttpResponse(template.render(context,request))



def calculate_cart(request):

    return redirect('/Biotec/Cart/')

def delete_from_cart(request, pk):
    Cart.objects.filter(id=pk).delete()
    return redirect('/Biotec/Cart/')




def clear_whole_cart(request, pk):
    Cart.objects.filter(User_ID=pk).delete()
    return redirect('/Biotec/Cart/')




#this view is for the product checkout. it contains the product on 'add to cart' checkout details
def checkout(request, pk):
    if request.user.is_authenticated:
        currentUser = request.user
        userid = currentUser.id
        by_client = Client.objects.filter(user=userid)
        priv = ""
        for client in by_client:
            priv = client.privilege
        if priv == 'biotech' or priv == 'all':
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
    'comp': 'BIOTECH',
    'user': Client.objects.filter(user=request.user),
    }
    form = Checkoutform(request.POST or None)
    min_char = 10
    max_char = 12
    allchar = string.ascii_letters + string.digits

    #get prices and cart info
    to_buy = Cart.objects.filter(User_ID=pk)
    size_to_buy = 0
    Vat= {'KE': 0.875, 'UG': 0.965, 'NAM' : 0.905}
    total = 0.0
    total = Decimal(total)
    VaT =Vat['KE']
    VaT = Decimal(VaT)
    finaltotal= 0.0
    for cart in to_buy:
        size_to_buy =size_to_buy+cart.count
        value_of_cart = cart.price * cart.count
        total = total + value_of_cart
        value = cart.count * VaT

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
    template = loader.get_template('products/checkout.html')
    return HttpResponse(template.render(context,request))




def boiordercatch(request):
    if request.user.is_authenticated:
        currentUser = request.user
        userid = currentUser.id
        by_client = Client.objects.filter(user=userid)
        priv = ""
        for client in by_client:
            priv = client.privilege
        if priv == 'biotech' or priv == 'all':
            request.session['userID']= userid
        else:
            return   redirect('/Users/login/')
    else:
         return   redirect('/Users/login/')

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
