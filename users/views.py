from .forms import *
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetForm
from django.contrib.auth import logout, login
from django.forms import ModelForm
from .forms import SignUpForm
from base.forms import ProfileForm
from django.views.generic import CreateView
from django.views import View
from django.shortcuts import redirect, render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

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
    
    
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')

    return render(request, 'registration/logout.html')