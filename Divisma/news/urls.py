from django.urls import path

from .views import *

urlpatterns = [
    path('news', HomeNews.as_view(), name='NewsHome'),
    path('news/category/<int:category_id>/', NewsByCategory.as_view(), name='NewsCategory'),
    path('news/<int:pk>/', ViewNews.as_view(), name='DetailNews'),
    #path('news', index, name='NewsHome'),
    #path('news/category/<int:category_id>/', get_category, name='NewsCategory'),
    #path('news/<int:news_id>/', view_news, name='DetailNews'),

]
