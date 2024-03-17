from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import LoginUser, user_office, RegistrationUser

app_name = "user"

urlpatterns = [
    path('', RegistrationUser.as_view(), name='registration'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<str:username>/office/', user_office, name='user_office'),

]