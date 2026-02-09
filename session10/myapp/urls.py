from django.urls import path
from .views import *
urlpatterns = [
        path('category_list/',category_list,name='category_list'),

        # Product crud
        path('product_list/',product_list,name='product_list'),
        path('product_Update/<int:pk>/',product_Update,name='product_Update'),
        path('product_delete/<int:pk>/',product_delete,name='product_delete'),
]