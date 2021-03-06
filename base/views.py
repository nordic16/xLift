from .models import *
from .forms import WorkoutCreationForm, AddExerciseForm
from users.models import Lifter
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from base import utils
from django.utils import timezone


def index_page_view(request):
    if request.method == 'GET':
        return render(request, template_name='index.html', context={'user' : request.user})
    
    
def workouts_page_view(request):
    if request.method == 'GET':
        return render(request, template_name='workout/workouts.html')
    

def dashboard_view(request):        
    return render(request, 'dashboard.html', context={'user' : request.user})


def workout_page_view(request, id):
    workout = Workout.objects.get(id=id)
    
    if request.method == 'GET':        
        if workout.owner == request.user:
            form = AddExerciseForm()
            sets = ExSet.objects.filter(workout=workout)
            
            return render(request, 'workout/edit_workout.html',
                context={'form' : form, 'sets' : sets, 'id' : id})

        else:
            return redirect(reverse_lazy('home'))
        
    else:
        form = AddExerciseForm(request.POST)
        if form.is_valid():
            if request.POST.get('add-exercise'):    
                data = form.cleaned_data

                for ex in data["Exercises"]:                
                    # If exercise is already in the workout, add another set
                    exset = ExSet.objects.filter(exercise=ex, workout=workout)
                    
                    if exset:
                        exset[0].number += 1
                        exset[0].save()
                        
                    else:
                        exset = ExSet.objects.create(exercise=ex, reps=0, weight=0, workout=workout)
                        exset.save()
                
                return redirect(f'/workouts/{id}')

            # Discards workout and redirects user to home.
            elif request.POST.get('discard'):
                workout.delete()
                return redirect(reverse_lazy('workouts'))

            # Finishes workout and, redirects the user to an overview page
            elif request.POST.get('finish'):
                # workout.active = False
                workout.save()
                
                return redirect(f'/workouts/{id}/overview')
            
            
            return render(request, 'temp.html')


def new_workout_view(request):
    user = request.user
    if request.method == 'GET':    
        form = WorkoutCreationForm()
        
        if user.is_authenticated:
            return render(request, 'workout/workout_creation.html', context={'form' : form})

    else:
        form = WorkoutCreationForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data

            workout = Workout.objects.create(name=data['name'],
            notes=data['notes'],
            owner=user)
                    
            
                    
            return redirect(f'/workouts/{workout.id}')


# EXCEPTIONS
def page_not_found_view(request, exception):
     return render(request, 'errors/404.html')
 

def overview_page_view(request, id):
    workout = Workout.objects.get(id=id)
    sets = ExSet.objects.filter(workout=workout)
    
    intensity= INTENSITY_CHOICES[int(workout.intensity) - 1][1]
    
    return render(request, 'workout/workout_overview.html', 
        context={'workout' : workout, 
            'intensity' : intensity, 'sets' : sets})