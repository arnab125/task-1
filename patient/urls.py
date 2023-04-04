from django.urls import path
from .views import *


urlpatterns = [
    path('login/', signin, name='patient_login'),
    path('register/', signup, name='patient_register'),
    path('<str:username>/', patient_info, name='patient_info'),
]
