from django.urls import path, include
from base.views import index_page

urlpatterns = [
    path('', index_page),   
    
    path('lifters/', include('users.urls')),
 
]