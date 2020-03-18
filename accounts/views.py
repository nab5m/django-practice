from django.contrib.auth.views import LoginView
from django.shortcuts import render

# Create your views here.
from accounts.forms import LoginForm


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
