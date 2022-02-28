from .models import *
from .forms import ProfileForm

from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render


def index_page(request):
    if request.method == 'GET':
        return render(request, template_name='index.html', context={'user' : request.user})
    
    
def workouts_page(request):
    if request.method == 'GET':
        return render(request, template_name='workouts.html')
    

def DashboardView(request):        
    return render(request, 'dashboard.html', context={'user' : request.user})


def profile_view(request):
    if request.method == 'POST':
        pass
    
    else:
        x = ProfileForm()
        
        return render(request, 'profile.html', context={'form' : x})