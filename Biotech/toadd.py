
#This view handles products added to the cart
Users = get_user_model()
def addtoCart(request, pk, size):
    #get user info
    currentUser = request.session['userID']
    usern= Users.objects.get(id= currentUser)
    #get product info
    pdo = Product.objects.get(pid=pk)
    Product_name = pdo.name
    #get Member info
    try:
        memeber = Member.objects.filter(Userid=currentUser)
        for mem in memeber:
            meme = mem.id
    except  AttributeError as error:
       # return redirect('/ecommerce/logout/')
        print(error)
    descr = pdo.description
    descr = descr[:75]

    newdes = descr + '...'
    bp = Cart(Cart_slug = "the-46-year-old-virgin",Member_ID=mem,Product_name=Product_name, Product_description=newdes, price=pdo.price , count =size, ProductID=pdo)
    bp.save()
    return redirect('/ecommerce/Cart/')    



def cart_view(request):

    currentUser = request.session['userID']
    #usern =request.session['Usern']
    form = Productnumber(request.POST or None)
    usern = Users.objects.get(id= currentUser)
    print(usern)
    #print(currentUser)
    memeber = get_object_or_404(Member, Userid=currentUser)
    meme = memeber.id
    cartprods = Cart.objects.filter(Member_ID=meme)

    Vat= {'KE': 0.875, 'UG': 0.965, 'NAM' : 0.905}
    context = {   
        'cart_content': '',
        'Userid': 4,
        'total_price': 0,
        'Vat':0,
        'user': usern.username,
        'memid': 0,
        'form': form
    }
    total = 0.0
    total = Decimal(total)
    counter = 0
    for cart in cartprods:
        VaT =Vat['KE']    
        VaT = Decimal(VaT)
        product_value = cart.price * cart.count
        value = cart.count * VaT 
        total = total + product_value
        total = round(total,2)
        context['Vat']= VaT
        counter= counter + 1

    finaltotal = total + value
    finaltotal = round(finaltotal,2)
    context['final_price']= finaltotal
    if form.is_valid():
        newnum = form.cleaned_data.get('size')
        Cart.objects.filter(Member_ID=meme).update(count=newnum)
        return redirect('/ecommerce/Cart/')
    print(total)
    context['cart_content'] = Cart.objects.filter(Member_ID=meme)
    context['Userid'] =  currentUser
    context['total_price']= total
    
    
    context['memid'] = meme
    template = loader.get_template('ecommerce/products/cart.html')

    return HttpResponse(template.render(context,request))



def calculate_cart(request):
    
    return redirect('/ecommerce/Cart/')

def delete_from_cart(request, pk):
    Cart.objects.filter(id=pk).delete()
    return redirect('/ecommerce/Cart/')




def clear_whole_cart(request, pk):
    Cart.objects.filter(Member_ID=pk).delete()
    return redirect('/ecommerce/Cart/')


#this view is for the product checkout. it contains the product on 'add to cart' checkout details 
def checkout(request, pk):
    context = {
    'userz': request.session['Usern'],
    'num_prod': 'num_prod',
    'add_prod': 'add_prod',
    'phone_num': 'phone_num',
    'serialCode': '213312weeqw',
    'price_prod': 'price',
    'product_list': 'prod',
    'times' : timezone.now(),
    'form': 'ghf'
    }
    form = Checkoutform(request.POST or None)
    min_char = 10
    max_char = 12
    allchar = string.ascii_letters + string.digits

    #get prices and cart info
    to_buy = Cart.objects.filter(Member_ID=pk)
    size_to_buy = len(to_buy)
    Vat= {'KE': 0.875, 'UG': 0.965, 'NAM' : 0.905}
    total = 0.0
    total = Decimal(total)
    for cart in to_buy:
        
        total = total + cart.price 
    VaT =Vat['KE']    
    VaT = Decimal(VaT)
    if total>0:   
        finaltotal = total + VaT
    else:
        finaltotal = 0

    #get memeber info
    by_member = Member.objects.filter(id=pk)
    for member in by_member:
        context['phone_num']=member.phone_number
        context['add_prod']= member.physical_address
    context['num_prod']= size_to_buy  
    context['price_prod']=finaltotal
    context['serialCode'] = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    context['form'] = Checkoutform()
    context['product_list'] = to_buy
    template = loader.get_template('ecommerce/products/checkout.html')
    return HttpResponse(template.render(context,request))









  path('checkout/<int:pk>/', views.checkout, name = 'checkout'),
    path('Cart/<int:pk>/<int:size>/', views.addtoCart, name='addtoCart'),
    path('Cart/', views.cart_view, name='cart_view'),
    path('Deletecart/<int:pk>/', views.delete_from_cart, name='delete_from_cart'),
    path('Updatecart/', views.calculate_cart, name='calculate_cart'),
    path('Clearcart/<int:pk>/', views.clear_whole_cart, name='clear_whole_cart'),
  