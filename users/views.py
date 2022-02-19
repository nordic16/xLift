from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm

# Sign Up View
class SignUpView(CreateView):
    form_class = SignUpForm
    # success_url = reverse_lazy('login')
    template_name = 'signup.html'