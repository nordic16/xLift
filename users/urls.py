from .views import SignUpView, LoginView, logout_view, profile_view
from django.urls import path, include
from django.contrib.auth.urls import *
from django.contrib.auth.views import PasswordResetView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('profile/<str:username>', profile_view, name='profile'),
    
    path('', include('django.contrib.auth.urls'))
]