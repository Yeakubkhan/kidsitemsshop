from django.contrib import admin
from .models import Product, ProductImage
from .models import Order

class ProductImageInline(admin.TabularInline):  
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phone',
        'address',
        'city',
        'district',
        'product',
        'quantity',
        'color',
        'total_price',
        'time'
    )
    
    search_fields = ('name', 'phone')
    list_filter = ('city', 'district', 'product', 'color')


