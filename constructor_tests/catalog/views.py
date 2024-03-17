from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView


from main.models import Categories, Result, Questions, Tests
from main.views import menu, pageNotFound


class TestsCatalog(ListView):
    model = Tests
    template_name = 'catalog/catalog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_category'] = Categories.objects.all()
        context['category_selected'] = 0
        context['title'] = 'Каталог тестов'
        return context

    def get_queryset(self):  # Отвечает за отображение только опубликованных тестов.
        return Tests.objects.filter(is_published=True)


class Test(DetailView):
    model = Tests
    template_name = 'catalog/test.html'
    pk_url_kwarg = 'test_id'


def category(request, category_id):
    object_list = Tests.objects.filter(category_key=category_id)
    list_category = Categories.objects.all()

    if len(object_list) == 0:
        raise Http404()
    context = {
        'object_list': object_list,
        'list_category': list_category,
        'menu': menu,
        'title': "Тесты по категориям",
        'category_selected': category_id,
    }
    return render(request, 'catalog/catalog.html', context=context)
