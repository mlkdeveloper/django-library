from django.urls import path
from .views import *

app_name = 'group'

urlpatterns = [
    path('', group_list, name='group_list'),
    path('create/', group_create, name='group_create'),
    path('update/<int:pk>/', group_update, name='group_update'),
    path('delete/<int:pk>/', group_delete, name='group_delete'),
]