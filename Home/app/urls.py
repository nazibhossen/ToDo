from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('updateTask/<id>/',updateTask, name='updateTask'),
    path('deleteTask/<id>/', deleteTask, name='deleteTask'),
    path('tese/',test, name='test')
]
