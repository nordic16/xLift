from django.urls import path, include
from base.views import index_page, workouts_page, DashboardView, profile_view

urlpatterns = [
    path('', index_page, name='home'),   
    path('workouts/', workouts_page, name='workouts'),    
    path('lifters/', include('users.urls')),
    path('dashboard/', DashboardView, name='dashboard'),
    path('profile/', profile_view, name='profile')
]