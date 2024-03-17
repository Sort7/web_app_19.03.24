from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView

from main.models import Tests, Result
from user.forms import LoginForm, RegistrationForm


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'user/login.html'
    extra_context = {'title': 'Авторизация'}


class RegistrationUser(CreateView):
    form_class = RegistrationForm
    template_name = 'user/registration.html'
    extra_context = {'title': "Регистрация"}
    success_url = reverse_lazy('user:login')


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
