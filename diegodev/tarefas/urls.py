
from django.urls import path
from diegodev.tarefas.views import home


app_name = 'tarefas'

urlpatterns = [
    path('', home, name='home')
]
