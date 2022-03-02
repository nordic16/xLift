from .forms import *
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.forms import ModelForm
from .forms import SignUpForm
from base.forms import ProfileForm
from django.views.generic import CreateView
from django.views import View
from django.shortcuts import redirect, render, reverse


# Sign Up View
class SignUpView(CreateView):
    form_class = SignUpForm
    model = Lifter
    template_name = 'registration/signup.html'
    success_url="/"
    
    def post(self, request):
        form = SignUpForm(request.POST)  
        if form.is_valid():
            data = form.cleaned_data
            user = Lifter.objects.create(
                username=data['username'], email=data['email'], 
                password=data['password1'])
                    
            user.save()
            login(request, user)
            
            form = ProfileForm() 
            print(form.fields)
            return render(request, 'profile.html', context={'form' : form, 'user' : user})
            
        else:
            print(form.error_messages)
        
    
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