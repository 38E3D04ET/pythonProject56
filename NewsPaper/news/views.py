from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import News

class NewsList(ListView):
    model = News
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = News.objects.order_by('-data')

    # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон. В возвращаемом словаре context будут храниться все переменные. Ключи этого словаря и есть переменные, к которым мы сможем потом обратиться через шаблон
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context[
            'value1'] = None  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        return context

class Whole_newsDetail(DetailView):
    model = News
    template_name = 'Whole_news.html'
    context_object_name = 'Whole_news'
    data = 'Whole_news.data'
    name = 'Whole_news.name'
