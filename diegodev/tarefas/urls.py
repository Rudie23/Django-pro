from django.urls import path

from diegodev.tarefas.views import home, detalhe, apagar

app_name = 'tarefas'

urlpatterns = [
    path('', home, name='home'),
    path('<int:tarefa_id>', detalhe, name='detalhe'),
    path('apagar/<int:tarefa_id>', apagar, name='apagar'),

]
