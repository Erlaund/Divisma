from dataclasses import field
from django.contrib import admin


# Register your models here.

from .models import Product, Category, Color, Brand, SubCategory, Size

class ProductAdmin(admin.ModelAdmin):
    save_on_top = True
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'price', 'is_available', 'category', 'sub_category', 'color', 'brand')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'price')
    list_filter = ('category', 'color', 'brand')
    fields = ('title', 'slug', 'description', 'price', 'is_available', 'is_OnSale', 'size', 'category', 'sub_category', 'color', 'brand', 'image', 'image1', 'image2', 'image3' )

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title')


class ColorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title')

class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title')

class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'category')
    list_display = ('id', 'title')

class SizeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Size, SizeAdmin)







