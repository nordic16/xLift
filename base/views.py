from .models import *
from .forms import WorkoutForm, AddExerciseForm
from users.models import Lifter
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from base import utils


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
    
    if request.method == 'GET':        
        if workout.owner == request.user:
            form = AddExerciseForm()
            sets = ExSet.objects.filter(workout=workout)
            
            return render(request, 'edit_workout.html',
                context={'form' : form, 'sets' : sets})

            #return render(request, 'edit_workout.html',
             #   context={'workout' : workout, 'sets' : sets, 
              #           'exercises' : utils.exercises})
            
        else:
            return redirect(reverse_lazy('home'))
        
    else:
        form = AddExerciseForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            for ex in data["Exercises"]:
                print(ex.name)
                
                # Creates a set for each exercise.
                exset = ExSet.objects.create(exercise=ex, reps=0, weight=0, workout=workout)
                exset.save()
            
            return redirect(f'/workouts/{id}')
    
    


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
 

