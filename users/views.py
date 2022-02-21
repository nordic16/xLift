from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from .forms import SignUpForm
from django.views.generic import TemplateView

# Sign Up View
class SignUpView(CreateView):
    form_class = SignUpForm
    model = Lifter
    template_name = 'registration/signup.html'
    success_url="/"