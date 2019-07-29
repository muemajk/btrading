from django.http import HttpResponse
from adminstrator.models import freightRate
from Biotech.models import Cart
from Flintwood.models import FlintCart
from TKTitan.models import TKCart
from Biotech.models import Product as bioprod
from Flintwood.models import Product as flintprod

from TKTitan.models import Product as tkprod



# this function gets the current frieght rate of the product purchased
def rates(brand, destination, source):
    if brand and destination and source:
        try:
            rate = freightRate.objects.get(Product_types=brand, Destination=destination, Source=source)

            return float(rate)
        except (TypeError, ValueError, OverflowError, freightRate.DoesNotExist):
            val=350
            return float(val)
    else:
        return None


# this function gets relevant information regarding the cart
def cart(company, userid, destination):
    if company and userid:
        if company == "bttitan":
            try:
                to_buy = TKCart.objects.filter(User_ID=userid)
                cartz = {}
                cartz['size'] = 0
                cartz['size'] = 0
                cartz['price']=0.0
                cartz['vat']=0
                cartz['before_vat_price']=0
                print(to_buy)
                for val in to_buy:
                    print(val)
                    vals = val.ProductID.pid

                    try:
                        prod = tkprod.objects.get(pid=vals)
                        source = prod.origin
                        brand = prod.Brand_Name
                    except (TypeError, tkprod.DoesNotExist, ValueError, OverflowError) as error:
                        return HttpResponse(error)

                    cartz['count'] = val.count
                    vat = rates(brand, destination, source)
                    cartz['price'] = float(cartz['price']) + ((float(val.price) * val.count)+vat)
                    cartz['before_vat_price'] = float(cartz['before_vat_price']) + (float(val.price) * val.count)
                    cartz['vat'] = cartz['vat'] + vat
                    cartz['size'] = cartz['size']+1
                return cartz
            except TKCart.DoesNotExist:
                return None
        if company == "biotech":
            try:
                to_buy = Cart.objects.filter(User_ID=userid)
                cartz = {}
                cartz['size'] = 0
                cartz['price']=0.0
                cartz['vat']=0
                cartz['before_vat_price']=0
                print(to_buy)
                for val in to_buy:
                    print(val)
                    vals = val.ProductID.pid

                    try:
                        prod = bioprod.objects.get(pid=vals)
                        source = prod.origin
                        brand = prod.Brand_Name
                    except (TypeError, bioprod.DoesNotExist, ValueError, OverflowError) as error:
                        return HttpResponse(error)

                    cartz['count'] = val.count
                    vat = rates(brand, destination, source)
                    cartz['price'] = float(cartz['price']) + ((float(val.price) * val.count)+vat)
                    cartz['before_vat_price'] = float(cartz['before_vat_price']) + (float(val.price) * val.count)
                    cartz['vat'] = cartz['vat'] + vat
                    cartz['size'] = cartz['size']+1
                return cartz
            except Cart.DoesNotExist:
                return None
        elif company == "flintwood":
            try:
                to_buy = FlintCart.objects.filter(User_ID=userid)
                cartz = {}
                cartz['size'] = 0
                cartz['price']=0.0
                cartz['vat']=0
                cartz['before_vat_price']=0
                print(to_buy)
                for val in to_buy:
                    print(val)
                    vals = val.ProductID.pid

                    try:
                        prod = flintprod.objects.get(pid=vals)
                        source = prod.origin
                        brand = prod.Brand_Name
                    except (TypeError, flintprod.DoesNotExist, ValueError, OverflowError) as error:
                        return HttpResponse(error)

                    cartz['count'] = val.count
                    vat = rates(brand, destination, source)
                    cartz['price'] = float(cartz['price']) + ((float(val.price) * val.count)+vat)
                    cartz['before_vat_price'] = float(cartz['before_vat_price']) + (float(val.price) * val.count)
                    cartz['vat'] = cartz['vat'] + vat
                    cartz['size'] = cartz['size']+1
                return cartz
            except FlintCart.DoesNotExist:
                return None
        else:
            return None
    else:
        return None
