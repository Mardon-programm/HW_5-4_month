from django.views.generic import ListView, DetailView
from .models import News

# Главная страница — список новостей
class NewsListView(ListView):
    model = News
    template_name = 'index.html'
    context_object_name = 'news'

# Страница с детальной информацией о новости
class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news'


