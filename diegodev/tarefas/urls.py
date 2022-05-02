
from django.urls import path
from diegodev.tarefas import views


app_name = 'tarefas'

urlpatterns = [
    path('', views.home, name='home')
]
