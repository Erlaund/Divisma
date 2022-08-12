from django.urls import URLPattern, path
from .views import *


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('shop/', ShopPage.as_view(), name='shop'),
    path('shop/category/<str:slug>/', ProductByCategory.as_view(), name='category'),
    path('shop/brand/<str:slug>/', ProductByBrand.as_view(), name='brand' ),
    path('shop/product/<str:slug>/', ViewProduct.as_view(), name='product'),

]