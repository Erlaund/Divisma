from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import News, Category


class HomeNews(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.filter(is_published=True)

class NewsByCategory(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.filter(category_id = self.kwargs['category_id'], is_published=True)

class ViewNews(DetailView):
    model = News
    template_name = 'news/news_item.html'
    context_object_name = 'news_item'
    #pk_url_kwarg = 'news_id'

#def index(request):
#    news = News.objects.all()
#    context = {
#        'news': news,
#        'title': 'Список новостей',
#   }
#    return render(request, template_name='news/index.html', context=context)

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)

    return render(request, 'news/category.html', {'news': news,  'category': category})

def view_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/news_item.html', {'news_item': news_item})