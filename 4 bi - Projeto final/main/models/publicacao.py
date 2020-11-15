from django.db import models

from main.models import Usuario


class Publicacao(models.Model):

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)

    titulo = models.CharField(max_length=50, null=True)
    descricao = models.CharField(max_length=600, null=True)
    roupa = models.BooleanField(default=False)
    alimento = models.BooleanField(default=False)
    dinheiro = models.BooleanField(default=False)
    email = models.CharField(max_length=100, null=True)
    whatsapp = models.CharField(max_length=100, null=True)

    class Meta(object):
        app_label ='main'
        db_table = 'main_doacao'