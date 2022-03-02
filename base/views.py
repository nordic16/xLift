from .models import *
from .forms import ProfileForm
from users.models import Lifter
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, reverse, get_object_or_404


def index_page(request):
    if request.method == 'GET':
        return render(request, template_name='index.html', context={'user' : request.user})
    
    
def workouts_page(request):
    if request.method == 'GET':
        return render(request, template_name='workouts.html')
    

def DashboardView(request):        
    return render(request, 'dashboard.html', context={'user' : request.user})


def profile_view(request, username=None):
    if not username:
        user = request.user
    else:
        user = get_object_or_404(Lifter, username=username)
    
    if request.method == 'POST':
        form = ProfileForm(data=request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.date_of_birth = data['date_of_birth']
            user.weight = data['weight']
            user.height = data['height']
            user.save()
        
            return redirect(reverse(index_page)) 
        
    else:
        # Prevents people from editing other user's profiles.
        form = ProfileForm() if user is request.user else None
        return render(request, 'profile.html', context={
            'form' : form, 'user' : user})
        


# EXCEPTIONS
def page_not_found_view(request, exception):
     return render(request,'errors/404.html')