from dataclasses import field
from django.contrib import admin


# Register your models here.

from .models import Product, Category, Color, Brand

class ProductAdmin(admin.ModelAdmin):
    save_on_top = True
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'price', 'is_available', 'category', 'color', 'brand' )
    list_display_links = ('id', 'title')
    search_fields = ('title', 'price')
    list_filter = ('category', 'color', 'brand')
    fields = ('title', 'slug', 'descriptioin', 'price', 'is_available', 'size', 'category', 'color', 'brand', 'image')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class ColorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Brand, BrandAdmin)






