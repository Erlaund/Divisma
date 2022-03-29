from django.urls import URLPattern, path
from .views import *


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('shop', ShopPage.as_view()),
    path('category/<str:slug>', ProductByCategory.as_view(), name='category')

]