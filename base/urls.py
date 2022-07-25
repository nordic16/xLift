from django.urls import path, include
from base.views import index_page, workouts_page, DashboardView, new_workout, workout_page_view

urlpatterns = [
    path('', index_page, name='home'),   
    
    path('workouts/', workouts_page, name='workouts'),    
    path('workouts/new', new_workout, name='new'),    
    
    path('workouts/<int:id>', workout_page_view, name='workout'),
    
    path('lifters/', include('users.urls')),
    
    path('dashboard/', DashboardView, name='dashboard'),
]