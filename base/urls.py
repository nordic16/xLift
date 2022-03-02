from django.urls import path, include
from base.views import index_page, workouts_page, DashboardView, profile_view

handler404 = 'base.views.page_not_found_view'

urlpatterns = [
    path('', index_page, name='home'),   
    path('workouts/', workouts_page, name='workouts'),    
    path('lifters/', include('users.urls')),
    path('dashboard/', DashboardView, name='dashboard'),
    path('profile/', profile_view, name='profile'),
    path('profile/<str:username>', profile_view, name='profile')
]