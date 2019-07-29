from django.shortcuts import render
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,  JsonResponse
from django.template import loader
from TKTitan.models import Product, ProductCatergory, TKCart
from Users.models import Client
from django.utils import timezone
from django.urls import reverse
from decimal import Decimal
import string
from random import *
from orders.addtocart import addcart
from .forms import Checkoutform, Productnumber
from adminstrator.models import freightRate
from orders.price import cart
from django.template.loader import render_to_string


# Create your views here.
def index(request):
    template = loader.get_template('members/Userdetails.html')

    return HttpResponse(template.render(context, request))


# this view is for the homepage. it contains the product catalog
def store_page(request):
    if request.user.is_authenticated:
        currentUser = request.user
        userid = currentUser.id
        by_client = Client.objects.filter(user=userid)
        priv = ""
        for client in by_client:
            priv = client.privilege
        if priv == 'bttitan' or priv == 'all':
            request.session['userID'] = userid
        else:
            return redirect('/')
    else:
        return redirect('/Users/login/')
    usez = None
    comp = 'bttitan'
    context = {
        'user_content': Product.objects.filter(Active=True),
        'user_name': usez,
        'times': timezone.now(),
        'img': 'none',
        'comp': 'bttitan',
        'company': comp,
        'user': Client.objects.filter(user=request.user),
        'freightrate': freightRate.objects.all(),
        'productinfo':'TkTitan:product_page',

    }
    photo = Product.objects.all()
    pic = ''
    for pho in photo:
        pic = str(pho.image)
        print(pic)
    if request.user.is_authenticated:
        username = request.user.username
        context['user_content'] = Product.objects.filter(Active=True)
        context['user_name'] = username
        context['img'] = pic
    template = loader.get_template('products/store.html')

    return HttpResponse(template.render(context, request))


# this view is for the individual product picked. it contains the product information
def product_page(request, pk):
    if request.user.is_authenticated:
        currentUser = request.user
        userid = currentUser.id
        by_client = Client.objects.filter(user=userid)
        priv = ""
        for client in by_client:
            priv = client.privilege
        if priv == 'bttitan' or priv == 'all':
            request.session['userID'] = userid
        else:
            return redirect('/Users/login/')
    else:
        return redirect('/Users/login/')

    user_name = None
    prod = get_object_or_404(Product, pid=pk)
    # for pro in prod:
    cat = prod.Product_Catergory
    print(cat)
    # prodcat= ProductCatergory.objects.filter(id=pro)
    companylink = 'TkTitan:store_page'
    form = Productnumber(request.POST or None)
    context = {
        'info': prod,
        'user': Client.objects.filter(user=request.user),
        'userzz': 4,
        'form': Productnumber(),
        'prod_count': 1,
        'user_name': request.user.username,
        'times': timezone.now(),
        'comp': 'bttitan',
        'companylink': companylink, 'company':'bttitan', 'supplier': prod.tksupplierid,
    }
    if form.is_valid():
        size = form.cleaned_data.get('size')
        context['prod_count'] = size
    currentUser = request.session['userID']
    print(currentUser)

    template = loader.get_template('products/info.html')
    return HttpResponse(template.render(context, request))


def addtoTKCart(request, pk, size):
    if request.user.is_authenticated:
        currentUser = request.user
        userid = currentUser.id
        by_client = Client.objects.filter(user=userid)
        priv = ""
        for client in by_client:
            priv = client.privilege
        if priv == 'bttitan' or priv == 'all':
            request.session['userID'] = userid
        else:
            return redirect('/Users/login/')
    else:
        return redirect('/Users/login/')

    company = 'bttitan'
    userid = currentUser
    prodname = addcart(userid, company, pk, size)
    if prodname is None:
        template = render_to_string('products/responses/addcart.html', {'prodname': "Error! Try again. Nothing "})
    else:
        template = render_to_string('products/responses/addcart.html', {'prodname': prodname})

    data = {
        'add_cart': template
     }
    return JsonResponse(data)


def TKCart_view(request):
    if request.user.is_authenticated:
        currentUser = request.user
        userid = currentUser.id
        by_client = Client.objects.filter(user=userid)
        priv = ""
        country = ""
        for client in by_client:
            priv = client.privilege
            country = client.Country
        if priv == 'bttitan' or priv == 'all':
            request.session['userID'] = userid
        else:
            return redirect('/Users/login/')
    else:
        return redirect('/Users/login/')
    currentUser = request.session['userID']

    form = Productnumber(request.POST or None)
    company = 'bttitan'
    destination = country
    page = 'TkTitan:store_page'
    clearcart = 'TkTitan:clear_whole_TKCart'
    recalculate = 'TkTitan:calculate_TKCart'
    deletebtn = 'TkTitan:delete_from_TKCart'
    cartinfo = cart(company, userid, destination)
    context = {'Cart_content': TKCart.objects.filter(User_ID=currentUser), 'Userid': currentUser,
               'total_price': int(cartinfo['before_vat_price']), 'Vat': cartinfo['vat'],
               'freightrate': cartinfo['vat'], 'final_price': int(cartinfo['price']),
               'memid': currentUser, 'form': form, 'user_name': request.user.username, 'times': timezone.now(),
               'comp': 'bttitan', 'user': Client.objects.filter(user=request.user), 'button': page,   'clearcartlink':clearcart, 'recalculate': recalculate, 'deletebtn': deletebtn}

    template = loader.get_template('products/cart.html')
    if form.is_valid():
        newnum = form.cleaned_data.get('size')
        newid = request.POST.get('ip')
        print(newid)
        TKCart.objects.filter(id=newid).update(count=newnum)
        return redirect('/BTTitan/TKCart/')
    return HttpResponse(template.render(context, request))


def calculate_TKCart(request):
    return redirect('/BTTitan/TKCart/')


def delete_from_TKCart(request, pk):
    TKCart.objects.filter(id=pk).delete()
    return redirect('/BTTitan/TKCart/')


def clear_whole_TKCart(request, pk):
    TKCart.objects.filter(User_ID=pk).delete()
    return redirect('/BTTitan/TKCart/')


# this view is for the product checkout. it contains the product on 'add to TKCart' checkout details
def checkout(request, pk):
    if request.user.is_authenticated:
        currentUser = request.user
        userid = currentUser.id
        by_client = Client.objects.filter(user=userid)
        priv = ""
        for client in by_client:
            priv = client.privilege
        if priv == 'bttitan' or priv == 'all':
            request.session['userID'] = userid
        else:
            return redirect('/Users/login/')
    else:
        return redirect('/Users/login/')
    context = {
        'userz': currentUser,
        'num_prod': 'num_prod',
        'add_prod': 'add_prod',
        'phone_num': 'phone_num',
        'serialCode': '213312weeqw',
        'price_prod': 'price',
        'product_list': 'prod',
        'times': timezone.now(),
        'form': 'ghf',
        'user_name': request.user.username,
        'comp': 'bttitan',
    }
    form = Checkoutform(request.POST or None)
    min_char = 10
    max_char = 12
    allchar = string.ascii_letters + string.digits

    # get prices and TKCart info
    to_buy = TKCart.objects.filter(User_ID=pk)
    size_to_buy = 0
    Vat = {'KE': 0.875, 'UG': 0.965, 'NAM': 0.905}
    total = 0.0
    total = Decimal(total)
    VaT = Vat['KE']
    VaT = Decimal(VaT)
    finaltotal = 0.0
    for cart in to_buy:
        size_to_buy = size_to_buy + cart.count
        value_of_TKCart = cart.price * cart.count
        total = total + value_of_TKCart
        value = cart.count * VaT

    if total > 0:
        finaltotal = total + value
        finaltotal = round(finaltotal, 2)
    else:
        finaltotal = 0

    # get memeber info
    by_client = Client.objects.filter(user=pk)
    for client in by_client:
        context['phone_num'] = client.phonenumber
        context['add_prod'] = client.physical_address
    context['num_prod'] = size_to_buy
    context['price_prod'] = finaltotal
    context['serialCode'] = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    context['form'] = Checkoutform()
    context['product_list'] = to_buy
    template = loader.get_template('products/tkcheckout.html')
    return HttpResponse(template.render(context, request))
