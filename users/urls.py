from .views import SignUpView, login_view
from django.urls import path, include

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', login_view, name='login')
]