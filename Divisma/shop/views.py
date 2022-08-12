import imp
from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Product, Category

# Create your views here.

class HomePage(ListView):
    model = Product
    template_name = 'shop/index.html'
    context_object_name = 'product'

    def get_queryset(self):
        return Product.objects.filter(is_available=True)

class ShopPage(ListView):
    model = Product
    template_name = 'shop/shop.html'
    context_object_name = 'product'

    def get_queryset(self):
        return Product.objects.filter(is_available=True)


class ProductByCategory(ListView):
    template_name = 'shop/shop.html'
    context_object_name = 'product'
    allow_empty = True

    def get_queryset(self):
        return Product.objects.filter(category__slug = self.kwargs['slug'],  is_available=True)

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug = self.kwargs['slug'])
        return context

class ProductByBrand(ListView):
    template_name = 'shop/shop.html'
    context_object_name = 'product'
    allow_empty = True

    def get_queryset(self):
        return Product.objects.filter(brand__slug = self.kwargs['slug'], is_available=True)


class ViewProduct(DetailView):
    model = Product
    context_object_name = 'product_item'
    template_name = 'shop/product_item.html'


def index(request):
    pass
#    product = Product.objects.all()
#    return render(request, 'shop/index.html', {'product': product} )

def ShopCategory(request):
    pass
    #categories = Category.objects.all()
    #context = {
    #    'categories': categories,
    #}
    #return render(request, template_name='shop/shop.html', context = context)


