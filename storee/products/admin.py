from django.contrib import admin

# Register your models here.
from products.models import Basket, Product, ProductCategory

admin.site.register(Product)
admin.site.register(ProductCategory)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', ('price', 'quantity'), ' stripe_product_price_id', 'category', 'image')
    readonly_fields = ('description', )
    search_fields = ('name',)
    ordering = ('name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity')
    extra = 0