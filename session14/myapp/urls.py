from django.urls import path
from .views import *
urlpatterns = [
    path('post_list/',post_list),
    # path('post_list_file/',post_list_file),
    # path('post_list_database/',post_list_database),
]