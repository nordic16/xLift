from django.urls import path, include
from base.views import index_page, workouts_page, profile_page

urlpatterns = [
    path('', index_page, name='index'),   
    path('workouts/', workouts_page, name='workouts'),
    path('profile/', profile_page, name='profile'),
    
    path('lifters/', include('users.urls')),
 
]