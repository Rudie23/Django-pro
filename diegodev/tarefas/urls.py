
from django.urls import path
from views import home

app_name = 'tarefas'

urlpatterns = [
    path('', views.home, name='home')
]
