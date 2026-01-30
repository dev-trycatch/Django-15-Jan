from django.urls import path
from .views import *

urlpatterns = [
    path('student_create/',student_create,name='student_create'),
    path('student_list/',student_list,name='student_list'),
    path('student_edit/<int:pk>',student_edit,name='student_edit')
]