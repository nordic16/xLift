from .views import SignUpView, LoginView
from django.urls import path, include
from django.contrib.auth.urls import *

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('', include('django.contrib.auth.urls'))
]