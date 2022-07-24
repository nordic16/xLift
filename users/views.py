from .forms import *
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetForm
from django.contrib.auth import logout, login
from django.forms import ModelForm
from .forms import SignUpForm
from .forms import ProfileForm
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
    success_url = 'registration/login.html'
    
    
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


def profile_view(request, username=None):
    if not username:
        user = request.user
    else:
        user = get_object_or_404(Lifter, username=username)
    
    if request.method == 'POST':
        form = ProfileForm(data=request.POST)
        
        if form.is_valid():
            data = form.cleaned_data

            # Might want to fix this later lmao            
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.date_of_birth = data['date_of_birth']
            user.weight = data['weight']
            user.height = data['height']
            user.save()
        
            return redirect(reverse_lazy('home')) 
        
    else:
        # Prevents people from editing other user's profiles.
        form = ProfileForm() if user.id is request.user.id else None
        return render(request, 'profile.html', context={
            'form' : form, 'user' : user})
        