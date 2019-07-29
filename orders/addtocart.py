from Biotech.models import Cart
from Flintwood.models import FlintCart
from TKTitan.models import TKCart
from Biotech.models import Product as bioprod
from Flintwood.models import Product as flintprod
from django.http import HttpResponse
from TKTitan.models import Product as tkprod


def addcart(userid, company, pk, size):
    if company == "flintwood":
        pdo = flintprod.objects.get(pid=pk)
        Product_name = pdo.name
        descr = pdo.description
        descr = descr[:375]
        newdes = descr + '...'
        bp = FlintCart(User_ID=userid, Product_name=Product_name, Product_description=newdes, price=pdo.price,
                       count=size, ProductID=pdo)
        bp.save()
        return Product_name
    elif company == "biotech":
        pdo = bioprod.objects.get(pid=pk)
        Product_name = pdo.name
        descr = pdo.description
        descr = descr[:375]
        newdes = descr + '...'
        bp = Cart(User_ID=userid, Product_name=Product_name, Product_description=newdes, price=pdo.price,
                  count=size, ProductID=pdo)
        bp.save()
        return Product_name
    elif company == "bttitan":
        pdo = tkprod.objects.get(pid=pk)
        Product_name = pdo.name
        descr = pdo.description
        descr = descr[:375]
        newdes = descr + '...'
        bp = TKCart(User_ID=userid, Product_name=Product_name, Product_description=newdes, price=pdo.price,
                    count=size, ProductID=pdo)
        bp.save()
        return Product_name
    else:
        return None
