from django.urls import reverse
from diegodev.tarefas.models import Tarefa
import pytest


@pytest.fixture
def resposta(client, db):
    resp = client.get(reverse('tarefas:home'), data={'nome': 'Tarefa'})
    return resp


def test_tarefa_existe_bd(resposta):
    assert Tarefa.objects.exists()
    