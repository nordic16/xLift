from .views import SignUpView
from django.urls import path, include

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', include('django.contrib.auth.urls'))
]