from django.forms import ModelForm

from diegodev.tarefas.models import Tarefa


class TarefaNovaForm(ModelForm):
    class Meta:
        model = Tarefa  # herdará de Tarefa o modelo de banco de dados
        fields = ['nome']  # Campos presentes no formulário, no caso apenas o nome


class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa  # herdará de Tarefa o modelo de banco de dados
        fields = ['nome', 'feita']
