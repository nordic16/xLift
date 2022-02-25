from .forms import *
from django.contrib.auth.views import LoginView, LogoutView
from django.forms import ModelForm
from .forms import SignUpForm
from django.views.generic import CreateView
from django.views import View
from django.shortcuts import redirect, render

# Sign Up View
class SignUpView(CreateView):
    form_class = SignUpForm
    model = Lifter
    template_name = 'registration/signup.html'
    success_url="/"
    
    
class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'
    
    def get_success_url(self):
        return '/'


class LogoutView(LogoutView):
    pass