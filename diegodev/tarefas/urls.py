from django.urls import path

from diegodev.tarefas.views import home, detalhe

app_name = 'tarefas'

urlpatterns = [
    path('', home, name='home'),
    path('<int:tarefa_id>', detalhe, name='detalhe'),

]
