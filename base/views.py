from .models import *
from .forms import WorkoutForm
from users.models import Lifter
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy


def index_page(request):
    if request.method == 'GET':
        return render(request, template_name='index.html', context={'user' : request.user})
    
    
def workouts_page(request):
    if request.method == 'GET':
        return render(request, template_name='workouts.html')
    

def DashboardView(request):        
    return render(request, 'dashboard.html', context={'user' : request.user})


def workout_page_view(request, id):
    workout = Workout.objects.get(id=id)
        
    return render(request, 'edit_workout.html',
        context={'workout' : workout})


def new_workout(request):
    user = request.user
    if request.method == 'GET':    
        form = WorkoutForm()
        
        if user.is_authenticated:
            return render(request, 'workout_creation.html', context={'form' : form})

    else:
        form = WorkoutForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data

            workout = Workout.objects.create(intensity=data['intensity'],
            name=data['name'],
            notes=data['notes'],
            owner=user)
                    
            return redirect(f'/workouts/{workout.id}')

# EXCEPTIONS
def page_not_found_view(request, exception):
     return render(request, 'errors/404.html')
 

