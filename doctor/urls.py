from django.urls import path
from .views import *


urlpatterns = [
    path('login/', signin, name='doctor_login'),
    path('register/', signup, name='doctor_register'),
    path('<str:username>/', doctor_info, name='doctor_info'),

]