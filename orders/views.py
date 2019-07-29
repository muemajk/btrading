from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import loader
from orders.models import FlintwoodOrders, BiotechOrders, TktitanOrders
from django.utils import timezone
from adminstrator.models import freightRate
from decimal import Decimal
import string
from random import *
from Biotech.models import Cart, Product as bioprod
from Flintwood.models import FlintCart, Product as flintprod
from TKTitan.models import TKCart
from TKTitan.models import Product as tkprod
from Users.models import Client
from TKTitan.forms import Checkoutform
from django.utils.html import strip_tags
from django.core.mail import EmailMessage
from .price import cart, rates
from django.core.mail import send_mail
import socket


# this page view will display all orders made
def index(request):
    template = loader.get_template('ecommerce/members/Userdetails.html')

    return HttpResponse(template.render(context, request))


def orders_view(request):
    currentUser = request.session['userID']
    try:
        memeber = Client.objects.filter(Userid=currentUser)
        for mem in memeber:
            meme = mem.id
            memphone = mem.phone_number
            memcountry = mem.country
            memphysical_address = mem.physical_address
            mempriv = mem.privilege
    except AttributeError:
        return redirect('/ecommerce/logout/')
        print(error)
    form = Checkoutform(request.POST or None)

    if mempriv == "flintwood":
        pass
    ordercart = Cart.objects.filter(Member_ID=meme)

    context = {
        'phone': memphone,
        'country': memcountry,
        'address': memphysical_address,
        'form': form,
        'ordersize': 0,
        'user': Client.objects.filter(user=request.user),
    }

    if form.is_valid():
        username = form.cleaned_data.get("cardcode")

    sizeord = len(ordercart)
    context['ordersize'] = sizeord

    template = loader.get_template('ecommerce/products/cart.html')
    return HttpResponse(template.render(context, request))


def orders(request, company, price):
    context = {}
    if request.user.is_authenticated:
        currentUser = request.user
        userid = currentUser.id
        by_client = Client.objects.filter(user=userid)
        pk = ""
        for client in by_client:
            pk = client.id
    else:
        return redirect('/Users/login/')

    form = Checkoutform(request.POST or None)
    min_char = 10
    max_char = 12
    allchar = string.ascii_letters + string.digits
    print(company)
    # get prices and TKCart info
    if company == 'bttitan':
        linkback = 'TkTitan:TKCart_view'
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
            'user': Client.objects.filter(user=request.user), 'linkback': linkback
        }

        to_buy = TKCart.objects.filter(User_ID=userid)
        by_client = Client.objects.filter(user=userid)
        brand = ''
        destination = ''
        source = ''
        vals = 0

        for client in by_client:
            destination = client.Country
            context['phone_num'] = client.phonenumber
            context['add_prod'] = client.physical_address

            context['serialCode'] = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
            context['form'] = Checkoutform()
            context['product_list'] = to_buy

        total_price = cart(company, userid, destination)
        context['price_prod'] = total_price['price']
        context['num_prod'] = total_price['size']
        template = loader.get_template('products/checkout.html')
        return HttpResponse(template.render(context, request))

    elif company == 'biotec':
        linkback = 'Biotech:cart_view'
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
            'comp': 'biotech',
            'user': Client.objects.filter(user=request.user), 'linkback': linkback
        }
        to_buy = Cart.objects.filter(User_ID=userid)
        brand = ''
        destination = ''
        source = ''
        vals = 0

        for client in by_client:
            destination = client.Country
            context['phone_num'] = client.phonenumber
            context['add_prod'] = client.physical_address

            context['serialCode'] = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
            context['form'] = Checkoutform()
            context['product_list'] = to_buy

        total_price = cart("biotech", userid, destination)
        context['price_prod'] = total_price['price']
        context['num_prod'] = total_price['size']
        template = loader.get_template('products/checkout.html')
        return HttpResponse(template.render(context, request))


    elif company == 'flintwood':
        linkback = 'Flintwood:FlintCart_view'
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
            'comp': 'flintwood',
            'user': Client.objects.filter(user=request.user), 'linkback': linkback,
        }
        to_buy = FlintCart.objects.filter(User_ID=userid)
        brand = ''
        destination = ''
        source = ''
        vals = 0

        for client in by_client:
            destination = client.Country
            context['phone_num'] = client.phonenumber
            context['add_prod'] = client.physical_address

            context['serialCode'] = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
            context['form'] = Checkoutform()
            context['product_list'] = to_buy

        total_price = cart(company, userid, destination)
        context['price_prod'] = total_price['price']
        context['num_prod'] = total_price['size']
        template = loader.get_template('products/checkout.html')
        return HttpResponse(template.render(context, request))


def ordercatch(request, company):
    if request.user.is_authenticated:
        currentUser = request.user
        userid = currentUser.id
        by_client = Client.objects.filter(user=userid)

    else:
        return redirect('/Users/login/')

    if company == 'flintwood':
        cartorders = FlintCart.objects.filter(User_ID=userid)
        ordlist = []
        ordval = ''
        count = 1
        for orders in cartorders:
            ordval = orders.Product_name + '(' + str(orders.count) + " units),"
            count += 1
            ordlist.append(ordval)

        # print(ordlist)

        min_char = 10
        max_char = 12
        allchar = string.ascii_letters + string.digits
        serialcode = "".join(choice(allchar) for x in range(randint(min_char, max_char)))

        products_ordered = ''.join(ordlist)

        print(products_ordered)
        neword = FlintwoodOrders(OrderID=serialcode, OrderDate=timezone.now(), OrderList=products_ordered,
                                 Order_Payment=False, user=currentUser)
        neword.save()

        adminsent = sendAdminEmail(request, company, neword)
        buyersent = sendClientEmail(request, company, currentUser, neword)
        print(adminsent)
        if adminsent is True and buyersent is True:
            data = {
                'sendnotify': "Thank you. An Email has been sent to :" + request.user.email
            }
        else:
            data = {
                'sendnotify': str(buyersent)
            }
        return JsonResponse(data)


    elif company == 'biotech':
        cartorders = Cart.objects.filter(User_ID=userid)
        ordlist = []
        ordval = ''
        count = 1
        neword = ''
        for orders in cartorders:
            ordval = orders.Product_name + '(' + str(orders.count) + " units),"
            count += 1
            ordlist.append(ordval)

        # print(ordlist)

        min_char = 10
        max_char = 12
        allchar = string.ascii_letters + string.digits
        serialcode = "".join(choice(allchar) for x in range(randint(min_char, max_char)))

        products_ordered = ''.join(ordlist)

        neword = BiotechOrders(OrderID=serialcode, OrderDate=timezone.now(), OrderList=products_ordered,
                               Order_Payment=False, user=currentUser)

        neword.save()

        adminsent = sendAdminEmail(request, company, neword)
        print("SENT TO ADMIN")
        print(adminsent)
        print("SENT TO ADMIN")
        buyersent = sendClientEmail(request, company, currentUser, neword)
        if adminsent is True and buyersent is True:
            data = {
                'sendnotify': "Thank you. An Email has been sent to :" + request.user.email
            }
        else:
            data = {
                'sendnotify': str(adminsent)
            }
        return JsonResponse(data)


    elif company == 'bttitan':
        cartorders = TKCart.objects.filter(User_ID=userid)
        ordlist = []
        ordval = ''
        count = 1
        for orders in cartorders:
            ordval = orders.Product_name + '(' + str(orders.count) + " units),"
            count += 1
            ordlist.append(ordval)

        # print(ordlist)

        min_char = 10
        max_char = 12
        allchar = string.ascii_letters + string.digits
        serialcode = "".join(choice(allchar) for x in range(randint(min_char, max_char)))

        products_ordered = ''.join(ordlist)

        print(products_ordered)
        neword = TktitanOrders(OrderID=serialcode, OrderDate=timezone.now(), OrderList=products_ordered,
                               Order_Payment=False, user=currentUser)
        neword.save()

        adminsent = sendAdminEmail(request, company, neword)
        buyersent = sendClientEmail(request, company, currentUser, neword)
        if adminsent is True and buyersent is True:
            data = {
                'sendnotify': "<p><small>Thank you. An Email has been sent to :" + request.user.email + "</p></small>"
            }
        else:
            data = {
                'sendnotify': str(buyersent)
            }
        return JsonResponse(data)

    else:
        data = {
            'sendnotify': "An unexpected error has occured please try again!"
        }
        return JsonResponse(data)


def sendAdminEmail(request, company, neword):
    currentUser = request.user
    if company == "flintwood":
        # to send email to administrator
        mail_subject = "[ALERT!]An Order has been made on flintwood."
        message = strip_tags(loader.render_to_string("orders/confirmorder.html", {
            'user': currentUser,
            'order': neword
        }))
        from_email = 'btproducts4u@gmail.com'
        to_email = ["btproducts4u@gmail.com"]

        try:
            print(to_email)

            if send_mail(mail_subject, message,from_email,to_email,fail_silently=False):
                return True
            else:
                return False

        except socket.gaierror as error:
            return error


    elif company == "bttitan":
        # to send email to administrator
        mail_subject = "[ALERT!]An Order has been made on Bttitan."
        message = strip_tags(loader.render_to_string("orders/confirmorder.html", {
            'user': currentUser,
            'order': neword
        }))
        from_email = ["Kennedy@btradingresources.com"]
        to_email = ['btproducts4u@gmail.com']
        try:

            if send_mail(mail_subject, message,from_email,to_email,fail_silently=False):
                return True
            else:
                return False

        except socket.gaierror as error:
            return error


    elif company == "biotech":
        # to send email to administrator
        mail_subject = "[ALERT!]An Order has been made on Biotec."
        message = strip_tags(loader.render_to_string("orders/confirmorder.html", {
            'user': currentUser,
            'order': neword
        }))
        from_email = ["Yael@btradingresources.com"]
        to_email = ['btproducts4u@gmail.com']
        try:

            if send_mail(mail_subject, message,from_email,to_email,fail_silently=False):
                return True
            else:
                return False

        except socket.gaierror as error:
            return error


def sendClientEmail(request, company, currentUser, neword):
    if company == "flintwood":
        # to send email to administrator
        mail_subject = "An Order has been made on flintwood."
        message = strip_tags(loader.render_to_string("orders/confirmorder.html", {
            'user': currentUser,
            'order': neword
        }))
        from_email = 'btproducts4u@gmail.com'
        mails = str(request.user.email)
        to_email = [mails]

        try:

            if send_mail(mail_subject, message,from_email,to_email,fail_silently=False): # EmailMessage(mail_subject, message, to_email).send(fail_silently=False):
                return True
            else:
                return False
        except socket.gaierror as error:
            return error


    elif company == "bttitan":
        # to send email to administrator
        mail_subject = "An Order has been made on Bttitan."
        message = strip_tags(loader.render_to_string("orders/confirmorder.html", {
            'user': currentUser,
            'order': neword
        }))
        from_email = 'btproducts4u@gmail.com'
        mails = str(request.user.email)
        to_email = [mails]

        try:

            if send_mail(mail_subject, message,from_email,to_email,fail_silently=False):
                return True
            else:
                return False

        except socket.gaierror as error:
            return error

    elif company == "biotech":
        # to send email to administrator
        mail_subject = "An Order has been made on Biotec."
        message = strip_tags(loader.render_to_string("orders/confirmorder.html", {
            'user': currentUser,
            'order': neword
        }))
        from_email = 'btproducts4u@gmail.com'
        mails = str(request.user.email)
        to_email = [mails]

        try:

            if send_mail(mail_subject, message,from_email,to_email,fail_silently=False):
                return True
            else:
                return False

        except socket.gaierror as error:
            return error
