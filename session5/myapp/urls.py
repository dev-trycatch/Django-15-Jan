from django.urls import path
from .views import *

urlpatterns = [
    path('home',home,name ='home'),
    path('update/<int:id>',update_emp,name ='update_emp'),
    path('delete/<int:id>',delete_emp,name ='delete_emp'),
]
