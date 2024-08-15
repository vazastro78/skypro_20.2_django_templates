from django.contrib import admin

from dealer.models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product_name', 'description', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('product_name', 'description',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk' , 'category_name')

