from django.contrib import admin
from .models import additem,Profile,OrderItem,sizes,Order,delivery

admin.site.register(additem)
admin.site.register(Profile)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(sizes)
admin.site.register(delivery)