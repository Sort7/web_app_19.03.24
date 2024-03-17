from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView

from main.models import Tests, Result
from user.forms import LoginForm, RegistrationForm


# def authentication (request):
#     return HttpResponse('Вход пользователя')

def register(request):
    return HttpResponse('Регистрация')


# def profile(request):
#     return HttpResponse('Профиль пользователя')


def user_office(request, username):
    us = User.objects.get(username=username)
    added_tests = Tests.objects.filter(author=us.id)
    completed_tests = Result.objects.filter(user=us.id)
    return render(request, 'user/office.html', {
        'added_tests': added_tests,
        'completed_tests': completed_tests,
        'title': "Личный кабинет",
        'username': username
    })

class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'user/login.html'
    extra_context = {'title': 'Авторизация'}

# def login_user(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('about'))
#     else:
#         form = LoginForm()
#     return render(request, 'user/login.html', {'form': form})

# def login_user(request):
#     if request.method == 'POST':
#         form = LoginUserForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('about'))
#     else:
#         form = LoginUserForm()
#     return render(request, 'user/login.html', {'form': form})


# def logout_user(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('user:login'))

# class RegisterUser (DateMixim, CraeteView):
#     from_class = UserCreationForm
#     template_name = 'user.html'
#     success_user = reverse_lazy('login')
#
#     def get_context_date(self, *args, object_list=None, **kwargs):
#         contex = super().get_context_date(**kwargs)
#         c_def = self.get_user_context (title='Регистрация')
#         return dict(list(contex.items()) + list(c_def.items()))

class RegistrationUser(CreateView):
    form_class = RegistrationForm
    template_name = 'user/registration.html'
    extra_context = {'title': "Регистрация"}
    success_url = reverse_lazy('user:login')