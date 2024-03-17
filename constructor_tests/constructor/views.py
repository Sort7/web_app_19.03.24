from django.http import HttpResponse
from django import forms
from django.shortcuts import redirect, render
from django.views.generic import FormView

from .forms import AddQuestionsForm, AddTestsForm
from main.views import menu


def tests_add(request):
    if request.method == 'POST':  # Проверка заполенния в форме
        form = AddTestsForm(request.POST)  # Возврат внесенных данных ползователем обратно в форму, если данные не были отпавлены
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect ('add_questions')  # Адрес страницы перенаправления после успешного заполенния формы
    else:
        form = AddTestsForm()
    data = {'form': form,
            'menu': menu,
            'title': 'Создание теста!!!'
            }
    return render(request, 'constructor/constructor.html', context=data)



# def tests_add (request, test_id):
#      return HttpResponse('Создание теста')


# class QuestionsFormView(FormView):
#     form_class = AddQuestionsForm
#     template_name = "constructor/add-questions.html"
#     success_url = "constructor/add-answers.html"
#
#     def get_initial(self):
#         return {'tests': self.kwagrs['question_id']}



# def add_questions (request):
#     if request.method == 'POST':  # Проверка заполенния в форме
#         form = AddQuestionsForm(request.POST)  # Возврат внесенных данных ползователем обратно в форму, если данные не были отпавлены
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#             return redirect ('add_questions')  # Адрес страницы перенаправления после успешного заполенния формы
#     else:
#         form = AddQuestionsForm()
#     data = {'form': form,
#             'menu': menu,
#             'title': 'Добавление вопросов теста!!!',
#             }
#     return render(request, 'constructor/add-questions.html', context=data)


# def add_questions (request, test_id):
#     return HttpResponse("Страница вопросов %s." % test_id)

# def add_questions (request):
#      return HttpResponse('Создание вопроса')


def add_answers (request):
    return HttpResponse('Создание ответа')

