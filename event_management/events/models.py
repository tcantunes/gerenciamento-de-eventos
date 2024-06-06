from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateTimeField()
    data_termino = models.DateTimeField()
    local = models.CharField(max_length=100)
    criador = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.titulo


