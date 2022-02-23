from .forms import *
from django.contrib.auth.views import LoginView
from .forms import SignUpForm
from django.views.generic import CreateView

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