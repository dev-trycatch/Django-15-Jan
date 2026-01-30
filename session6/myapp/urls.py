from django.urls import path,include
from .views import *

urlpatterns = [
    path('register/',register,name='register'),
    path('login/',login_page,name='login_page'),
    path('dashboard/',dashboard,name='dashboard'),
    path('logout/',logout_page,name='logout_page'),

]