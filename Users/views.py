from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from Users.models import Client
from django.utils import timezone
from orders.models import FlintwoodOrders, BiotechOrders, TktitanOrders



from decimal import Decimal
import string
from random import *

from .forms import  LoginForm, RegisterForm , addressUpdateform, phoneUpdateform, passwordupdateform, emailform, AltphoneUpdateform, Privilegeform, roleform
# Create your views here.
def admin_page(request):
    return redirect('/admin')



#this form is used by registered users to sign in
def login_page(request):
    logout(request)
    form = LoginForm(request.POST or None)

    template = loader.get_template('members/login.html')
    context = {
        'form' : form,

    }
    print('User logged in')

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            #user_logged_in.send(user.__class__, instance=user, request = request)
            context['form'] = LoginForm()
            if request.user.is_authenticated:
                currentUser = request.user
                userid = currentUser.id
                request.session['userID'] = userid
                request.session['Usern']= currentUser.username

                print(request.session['userID'])
                return redirect('/')

        else:

            print("Error!")
    return HttpResponse(template.render(context,request))



#this form is to sign up new users
Users = get_user_model()
def register_page(request):
    logout(request)
    form = RegisterForm(request.POST or None)
    template = loader.get_template('members/register.html')
    context = {
        'form' : form,
        
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
        priv = form.cleaned_data.get('privilege')
        role = form.cleaned_data.get('role')

        new_user = Users.objects.create_user(user_name, emailad, passwords)
        new_user.last_name = lastname
        new_user.first_name = firstname

        new_user.save()

        #print(role)
        user = authenticate(request, username=user_name, password=passwords)
        if user is not None:
            request.session['userID'] = ''
            #print(role)
            login(request,user)
            #user_logged_in.send(user.__class__, instance=user, request = request)
            if request.user.is_authenticated:
                currentUser = request.user
                #print(currentUser.id)
                print(role)
                request.session['userID'] = currentUser.id
                request.session['Usern']= currentUser.username
                print(request.session['Usern'])
                new_client = Client(user=currentUser,physical_address=physical_address,role= role,privilege=priv,Country=country,phonenumber=phone, Alternate_phonenumber =altphone, WeChat=wechat , Skype= skype )
                new_client.save()

                return redirect('/')

                login(request,user)
                print(user)







    return HttpResponse(template.render(context,request))





User = get_user_model()
def profile_view(request):
    if request.user.is_authenticated:
        currentUser = request.user
    else:
        return redirect('/Users/login/')

    template = loader.get_template('members/Profile.html')
    userid = currentUser.id
    emailforms = emailform(request.POST or None)
    passforms =  passwordupdateform(request.POST or None)
    addforms = addressUpdateform(request.POST or None)
    aphoneforms = AltphoneUpdateform(request.POST or None)
    mphoneforms = phoneUpdateform(request.POST or None)
    privforms = Privilegeform(request.POST or None)
    by_client = Client.objects.filter(user=userid)
    biorder = BiotechOrders.objects.filter(user=userid)
    tkorder = TktitanOrders.objects.filter(user=userid)
    florder = FlintwoodOrders.objects.filter(user=userid)
    clientinfo= ""
    for client in by_client:
        clientinfo = client


    context = {
        'useracc': currentUser,
        'user_name': currentUser.username,
        'times' : timezone.now(),
        'flintorders': florder,
        'biotech': biorder,
        'tkorder': tkorder,
        'clientinf': clientinfo,
        'emailform':emailform(),
        'passforms':passwordupdateform(),
        'addform':addressUpdateform(),
        'aphoneform':AltphoneUpdateform(),
        'mphoneform':phoneUpdateform(),
        'privform':Privilegeform(),
        'user': Client.objects.filter(user=request.user),
    }
    print(clientinfo.role)
    if addforms.is_valid():
        newadd = addforms.cleaned_data.get('physical_address')
        cli = Client.objects.get(user=userid)
        cli.physical_address =newadd

        cli.save(update_fields=['physical_address'])
        return redirect('/Users/profile/')


    if emailforms.is_valid():
        newemail = emailforms.cleaned_data.get('email')
        user = User.objects.get(id=userid)
        user.email =newemail
        user.save(update_fields=['email'])
        return redirect('/Users/profile/')

    if passforms.is_valid():
        newpass = passforms.cleaned_data.get('New_password')
        #oldpass = passforms.cleaned_data.get('Current_password')
        user = User.objects.get(id=userid)
        user.password =newpass
        user.save(update_fields=['password'])
        return redirect('/Users/profile/')

    if aphoneforms.is_valid():
        altphon = aphoneforms.cleaned_data.get('phone')
        cli = Client.objects.get(user=userid)
        cli.Alternate_phonenumber =altphon

        cli.save(update_fields=['Alternate_phonenumber'])
        return redirect('/Users/profile/')


    if mphoneforms.is_valid():
        mphone = mphoneforms.cleaned_data.get('phone')
        cli = Client.objects.get(user=userid)
        cli.phonenumber =mphone

        cli.save(update_fields=['phonenumber'])
        return redirect('/Users/profile/')

    if privforms.is_valid():
        newpriv =  privforms.cleaned_data.get("privilege")
        cli = Client.objects.get(user=userid)
        cli.privilege =newpriv

        cli.save(update_fields=['privilege'])
        return redirect('/Users/profile/')

    return HttpResponse(template.render(context,request))


def delete_from_user(request,pk):
    Users.objects.filter(id=pk).delete()
    return redirect('/Users/logout/')

def update_phone_to_user(request,pk):
    Users.objects.filter(id=pk).delete()
    return redirect('/Users/profile/')

def update_password_to_user(request,pk):
    Users.objects.filter(id=pk).delete()
    return redirect('/Users/profile/')

def update_address_to_user(request,pk):
    Users.objects.filter(id=pk).delete()
    return redirect('/Users/profile/')

def update_email_to_user(request,pk):
    Users.objects.filter(id=pk).delete()
    return redirect('/Users/profile/')









def logout_view(request):
    logout(request)
    try:
        del request.session['member_id']
        del request.session['userID']
    except KeyError:
        pass
    return redirect('/')
