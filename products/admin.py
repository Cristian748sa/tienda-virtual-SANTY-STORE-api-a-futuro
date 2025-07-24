from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):

    fields = ('title', 'description', 'price', 'has_discount', 'discount', 'image')

  
    list_display = ('__str__', 'slug', 'created_at', 'has_discount', 'discount')

    list_filter = ('has_discount',)

admin.site.register(Product, ProductAdmin)
