from django import template
from shop.models import Category, Color, Brand, SubCategory

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.simple_tag()
def get_brands():
    return Brand.objects.all()

@register.simple_tag()
def get_colors():
    return Color.objects.all()

@register.simple_tag()
def get_subCategories():
    return SubCategory.objects.all()

@register.filter(name='getSizesFromProduct')
def getSizesFromProduct(dictinary):
    list = dictinary.values()
    result = []
    for i in list:
        result.append(i.get('title'))
    return result

@register.filter(name='getSubCategories')
def getSubCategories(dictinary):
    list = dictinary.values()
    result = []
    for i in list:
        result.append(i.get('title'))
    return result

    