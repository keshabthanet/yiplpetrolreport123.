from django.contrib import admin
from .models import Product,Year,Country,Sales

# Register your models here.
admin.site.register(Product)
admin.site.register(Year)
admin.site.register(Country)
admin.site.register(Sales)
