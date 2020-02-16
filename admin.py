from django.contrib import admin
from .models import Product,Fridge,Buyer,User1,Seller,SellerStock,Order,Fridgetemp,Fridgehumidity


# Register your models here.
admin.site.register(Product)
admin.site.register(Fridge)
admin.site.register(User1)
admin.site.register(Buyer)
admin.site.register(Seller)
admin.site.register(SellerStock)
admin.site.register(Order)
admin.site.register(Fridgehumidity)
admin.site.register(Fridgetemp)

