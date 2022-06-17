from django.contrib import admin

# Register your models here.
from diegodev.tarefas.models import Tarefa


@admin.register(Tarefa)
class ModuloTarefa(admin.ModelAdmin):
    list_display = ('nome', 'feita', 'pendente')
