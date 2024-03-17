from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.core.exceptions import ObjectDoesNotExist

from main.models import Categories, Result, Questions, Tests #Answers
from main.views import menu, pageNotFound


# menu = ['Главная', 'О сайте', 'Каталог тестов', 'Добавить тест']


class TestsCatalog (ListView):
    model = Tests
    template_name = 'catalog/catalog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_category'] = Categories.objects.all()
        context['category_selected'] = 0
        context['title'] = 'Каталог тестов'
        return context

    def get_queryset(self): # Отвечает за отображение только опубликованных тестов.
        return Tests.objects.filter(is_published=True)


# def catalog (request):
#     tests_list = Tests.objects.all()
#     list_category = Categories.objects.all()
#     context = {
#         'tests_list': tests_list,
#         'list_category': list_category,
#         'menu': menu,
#         'title': "Каталог тестов",
#         'category_selected': 0,
#     }
#     return render(request, 'catalog/catalog.html', context=context)

# def test (request, test_id):
#     return HttpResponse (f"Отображение статити с id = {test_id}")

class Test (DetailView):
    model = Tests
    template_name = 'catalog/test.html'
    pk_url_kwarg = 'test_id'




def category (request, category_id):
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


# def test_execution(request, test_id):
#     quest = get_object_or_404(Questions, pk=test_id)
#     # # quest = get_object_or_404(Questions, test=test_id, question_ordinal=1)
#     # quest = test.questions_set.get(question_ordinal=1)
#     # iid = quest.pk
#     # vid = Answers.objects.filter(question=iid)
#
#
#     try:
#         scoring_points = quest.answers_set.get(pk=request.POST['answers'])
#     except (KeyError, Answers.DoesNotExist):
#         # Повторно отобразите форму для голосования по вопросу.
#         return render(request, 'catalog/test-execution.html', {
#             'quest': quest,
#             'test': test,
#             'menu': menu,
#             'error_message': "Вы не выбирали вариант.",
#         })
#     else:
#         # scoring_points.answers_weight +=1
#         # scoring_points.save()
#
#         new_result = Result.objects.create(user='Ivan2', result=0, the_best_result=0, test=test)
#         new_result.result += scoring_points.answers_weight
#         new_result.save()
#
#         # Всегда возвращайте HttpResponseRedirect после успешной обработки
#         #  # с данными POST. Это предотвращает повторную отправку данных, если пользователь
#         #  # нажимает кнопку "Назад".
#         return HttpResponseRedirect(reverse('test_execution', args=(quest.id,)))
#


# def test_execution (request, test_id):
#     return HttpResponse (f"Отображение статити с id = {test_id}")