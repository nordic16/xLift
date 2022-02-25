from django.urls import path, include
from base.views import index_page, workouts_page

urlpatterns = [
    path('', index_page, name='home'),   
    path('workouts/', workouts_page, name='workouts'),    
    path('lifters/', include('users.urls'))
]