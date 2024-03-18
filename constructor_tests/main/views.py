from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import DetailView, ListView, UpdateView

from .forms import QuestionsForm, ChoiceForm, AddTestsForm, AddValuationForm
from .models import Choice, Result, Tests, Questions, Valuation


menu = [{'title': 'ГЛАВНАЯ', 'url_name': 'index'},
        {'title': 'О САЙТЕ', 'url_name': 'about'},
        {'title': 'КАТАЛОГ ТЕСТОВ', 'url_name': 'catalog'},
        {'title': 'ДОБАВИТЬ ТЕСТ', 'url_name': 'add_tests'},
]



# def index(request):
#     latest_test_list = Tests.objects.all
#     context = {
#         'latest_test_list': latest_test_list,
#         'menu': menu,
#         'title': "Вы попали на страницу списка опросов."
#     }
#     return render(request, 'main/index.html', context)

# class IndexView(generic.ListView):
#     template_name = 'main/index.html'
#     context_object_name = 'latest_question_list'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['menu'] = menu
#         context['title'] = 'Вы попали на страницу списка опросов!!!'
#         return context
#
#     def get_queryset(self):
#         """Верните последние пять опубликованных вопросов."""
#         return Quest.objects.order_by('-pub_date')[:5]

def detail(request, test_id, question_id):
    test = get_object_or_404(Tests, pk=test_id)
    question = test.questions_set.get(pk=question_id)
    context = {
        'test_id': test_id,
        'question_id': question_id,
        'question': question,
        'test': test,
        'menu': menu,
        'title': "Страница опроса"
    }
    return render(request, 'main/detail.html', context)

# class DetailView(generic.DetailView):
#     model = Quest
#     template_name = 'main/detail.html'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['menu'] = menu
#         context['title'] = 'Опрос!!!'
#         return context

def vote(request, test_id, question_id):
    test = get_object_or_404(Tests, pk=test_id)
    question = test.questions_set.get(pk=question_id)
    first_question = test.questions_set.get(question_ordinal=1)
    first_question_id = first_question.id
    key = question.test_key
    new_question_id = question_id + 1
    number_of_questions = test.number_of_questions
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Повторно отобразите форму для голосования по вопросу.
        return render(request, 'main/detail.html', {
            'test_id': test_id,
            'question_id': question_id,
            'test': test,
            'question': question,
            'error_message': "Вы не выбирали вариант.",
        })
    else:
        new_result = Result.objects.filter(test_key=key).exists()
        if new_result:
            new_result = Result.objects.get(test_key=key)
            new_result.result += selected_choice.ball
            new_result.save()
            if question_id == first_question_id + number_of_questions -1:
                return HttpResponseRedirect(reverse('results', kwargs={'test_id': test.id,}))
            else:
                return HttpResponseRedirect(reverse('detail', kwargs={'test_id': test.id, 'question_id': new_question_id, }))
        else:
            new_result = Result.objects.create(user=request.user, result=0, the_best_result=0, test_key=key)
            new_result.result += selected_choice.ball
            new_result.save()
        # Всегда возвращайте HttpResponseRedirect после успешной обработки
        #  # с данными POST. Это предотвращает повторную отправку данных, если пользователь
        #  # нажимает кнопку "Назад".
        return HttpResponseRedirect(reverse('detail', kwargs={'test_id': test.id, 'question_id': new_question_id}))



# def vote(request, question_id):
#     catig = get_object_or_404(Cat, pk=question_id)
#     question = catig.quest_set.get(pk=1)
#     key = question.cat_key
#     newid = question_id + 1
#     # question = get_object_or_404(Quest, pk=question_id)
#     # key = question.cat_key
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Повторно отобразите форму для голосования по вопросу.
#         return render(request, 'main/detail.html', {
#             'question': question,
#             'error_message': "Вы не выбирали вариант.",
#         })
#     else:
#         new_result = Rez.objects.create(user='Ivan2', rez_ball=0, question=question, cat_key=key)
#         new_result.rez_ball += selected_choice.ball
#         new_result.save()
#         # Всегда возвращайте HttpResponseRedirect после успешной обработки
#         #  # с данными POST. Это предотвращает повторную отправку данных, если пользователь
#         #  # нажимает кнопку "Назад".
#         return HttpResponseRedirect(reverse('detail', args=(newid,)))


def results(request, test_id):
    test = get_object_or_404(Tests, pk=test_id)
    x = test.result_set.get(test_key=test_id)
    tes = test.valuation_set.all()
    rez = 0
    for t in tes:
        if x.result > t.value_max:
            rez = t
    return render(request, 'main/results.html', {'test': test, 'x':x, 'rez': rez, })


# class ResultsView(generic.DetailView):
#     model = Quest
#     template_name = 'main/results.html'

# def index (request):
#     return render(request, 'main/index.html', {'menu': menu, 'title': "Главная страница."})


@login_required
def about (request):
    return render(request, 'main/about.html', {'menu': menu, 'title': "О сайте"})

def contact (request):
    return render(request, 'main/contact.html', {'title': 'Контакты'})

def index (request):
    return HttpResponseRedirect('catalog')

def pageNotFound (request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена </h1>')



# def index(request):
#     return HttpResponse("Вы попали на страницу списка опросов.")

# def detail(request, question_id):
#     return HttpResponse("Вы смотрите на опрос %s." % question_id)

# def results(request, question_id):
#     response = "Вы смотрите на результаты опроса: %s."
#     return HttpResponse(response % question_id)

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

@login_required
def add_tests(request):
    if request.method == 'POST':  # Проверка заполенния в форме
        form = AddTestsForm(request.POST)  # Возврат внесенных данных ползователем обратно в форму, если данные не были отпавлены
        if form.is_valid():
            form.instance.author = request.user
            obj = form.save()
            test_id = obj.pk
            # return redirect ('add_question',) # Адрес страницы перенаправления после успешного заполенния формы
            # return HttpResponseRedirect(reverse('add_question', kwargs={'test_id': test_id, }))
            return HttpResponseRedirect(reverse('demo_test', kwargs={'test_id': test_id, }))
    else:
        form = AddTestsForm()
    data = {'form': form,
            'menu': menu,
            # 'test_id': test_id,
            'title': 'Создание теста.'
            }
    return render(request, 'main/add-tests.html', context=data)


class DemoTest(DetailView):
    model = Tests
    template_name = 'main/demo-test.html'
    pk_url_kwarg = 'test_id'
    allow_empty = False


@login_required
def add_question(request, test_id):
    test = Tests.objects.get(pk=test_id)
    number_of_сhoice = test.number_of_сhoice
    if request.method == "POST":
        question_form = QuestionsForm(request.POST, instance=Questions())
        choice_forms = [ChoiceForm(request.POST, prefix=str(x), instance=Choice()) for x in range(0,number_of_сhoice)]
        if question_form.is_valid() and all([c.is_valid() for c in choice_forms]):
            new_question = question_form.save(commit=False)
            new_question.test_key = test
            new_question.save()
            for c in choice_forms:
                new_choice = c.save(commit=False)
                new_choice.question_key = new_question
                new_choice.test_key = test
                new_choice.save()
            if 'button1' in request.POST:
                return HttpResponseRedirect(reverse('add_question', kwargs={'test_id': test_id, }))
            else:
                return HttpResponseRedirect(reverse('demo_list_questions', kwargs={'test_id': test_id, }))
    else:
        question_form = QuestionsForm(instance=Questions())
        choice_forms = [ChoiceForm(prefix=str(x), instance=Choice()) for x in range(0,number_of_сhoice)]
    context = {
        'question_form': question_form,
        'choice_forms': choice_forms,
        'test_id': test_id,
    }
    return render(request,'main/add-question.html', context)


@login_required
def update_question(request, test_id, question_id):
    # try:
    #     old_question = get_object_or_404(Questions, id=id)
    # except Exception:
    #     raise Http404('Такого студента не существует')
    old_question = get_object_or_404(Questions, pk=question_id)
    # old_choice_list = Choice.objects.filter(question_key=question_id)
    test = Tests.objects.get(pk=test_id)
    number_of_сhoice = test.number_of_сhoice
    if request.method == "POST":
        question_form = QuestionsForm(request.POST, instance=old_question)
        choice_forms = [ChoiceForm(request.POST, prefix=str(x), instance=Choice.objects.filter(question_key=question_id)[x]) for x in range(0,number_of_сhoice)]
        if question_form.is_valid() and all([c.is_valid() for c in choice_forms]):
            new_question = question_form.save(commit=False)
            new_question.test_key = test
            new_question.save()
            for c in choice_forms:
                new_choice = c.save(commit=False)
                # new_choice.question_key = new_question
                # new_choice.test_key = test
                new_choice.save()
            return HttpResponseRedirect(reverse('demo_list_questions', kwargs={'test_id': test_id, }))
    else:
        question_form = QuestionsForm(instance=old_question)
        choice_forms = [ChoiceForm(prefix=str(x), instance=Choice.objects.filter(question_key=question_id)[x]) for x in range(0,number_of_сhoice)]
    context = {
        'question_form': question_form,
        'choice_forms': choice_forms,
        'test_id': test_id,
        'question_id': question_id,
        'old_question': old_question,
    }
    return render(request,'main/update-question.html', context)


class DemoListQuestions(ListView):
    model = Questions
    template_name = 'main/deno-list-questions.html'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test_id'] = self.kwargs['test_id']
        return context

    def get_queryset(self):
        return Questions.objects.filter(test_key=self.kwargs['test_id'])


def add_valuation(request, test_id):
    if request.method == 'POST':  # Проверка заполенния в форме
        test = Tests.objects.get(pk=test_id)
        form = AddValuationForm(request.POST)  # Возврат внесенных данных ползователем обратно в форму, если данные не были отпавлены
        if form.is_valid():
            new_valuation = form.save(commit=False)
            new_valuation.test_key = test
            new_valuation.save()
            if 'button1' in request.POST:
                return HttpResponseRedirect(reverse('add_valuation', kwargs={'test_id': test_id,}))
            else:
                return HttpResponseRedirect(reverse('demo_valuation', kwargs={'test_id': test_id,}))

    else:
        form = AddValuationForm()
    data = {'form': form,
            'test_id': test_id,
            'title': 'Добавление оценок теста'
            }
    return render(request, 'main/add-valuation.html', context=data)


class DemoValuation(ListView):
    model = Valuation
    template_name = 'main/demo-valuation.html'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test_id'] = self.kwargs['test_id']
        return context

    def get_queryset(self):
        return Valuation.objects.filter(test_key=self.kwargs['test_id'])


def add_final(request, test_id):
    test = Tests.objects.get(pk=test_id)
    data = {'test': test,
            'menu': menu,
            'test_id': test_id,
            'title': 'Создание теста.'
            }
    return render(request, 'main/add-final.html', context=data)

def test_valuation(request, test_id):
    return HttpResponse("Результаты теста %s." % test_id)


class UpdateTest(UpdateView):
    model = Tests
    template_name = 'main/update-test.html'
    # context_object_name = 'test'
    pk_url_kwarg = 'test_id'
    fields = ['title', 'review', 'manual', 'category_key', 'number_of_questions', 'number_of_сhoice',]

    def get_success_url(self):
        return reverse_lazy('add_question', kwargs={'test_id': self.object.pk,})

class UpdateValuation(UpdateView):
    model = Valuation
    template_name = 'main/update-valuation.html'
    pk_url_kwarg = 'valuation_id'
    fields = ['valuation', 'value_max', 'analysis']

    def get_success_url(self):
        return reverse_lazy('demo_valuation', kwargs={'test_id': self.object.test_key_id})

