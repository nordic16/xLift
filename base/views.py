from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect


def index_page(request):
    if request.method == 'GET':
        return render(request, template_name='index.html', context={'user' : request.user})
    
    
def workouts_page(request):
    if request.method == 'GET':
        return render(request, template_name='workouts.html')
    
    
def profile_page(request):
    if request.method == 'GET':
        return render(request, template_name='profile.html')