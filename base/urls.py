from django.urls import path, include
from base.views import index_page_view, workouts_page_view, dashboard_view, new_workout_view, workout_page_view, overview_page_view

urlpatterns = [
    path('', index_page_view, name='home'),   
    
    path('workouts/', workouts_page_view, name='workouts'),    
    path('workouts/new', new_workout_view, name='new'),    
    
    path('workouts/<int:id>', workout_page_view, name='workout'),
    path('workouts/<int:id>/overview', overview_page_view, name='overview'),
    
    path('lifters/', include('users.urls')),
    
    path('dashboard/', dashboard_view, name='dashboard'),
]