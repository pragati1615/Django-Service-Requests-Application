from django.urls import path
from .views import CustomAuthToken, register

urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('register/', register, name='register'),
]

