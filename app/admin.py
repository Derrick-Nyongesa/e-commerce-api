from django.contrib import admin
from .models import Customer, Products, Category_One, Category_Two, Cart, Orders, Feedback

# Register your models here.
admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(Category_One)
admin.site.register(Category_Two)
admin.site.register(Cart)
admin.site.register(Orders)
admin.site.register(Feedback)
