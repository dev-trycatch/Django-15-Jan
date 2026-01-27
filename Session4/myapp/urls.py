from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home,name = 'home'),
    path('student_data/',student_data,name = 'student_data'),
]