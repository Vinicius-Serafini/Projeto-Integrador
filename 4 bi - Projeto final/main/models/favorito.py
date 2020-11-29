from django.db import models

from main.models import Usuario
from main.models import Publicacao

class Favorito(models.Model):

    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, null=True)
    publicacao = models.ForeignKey(Publicacao, on_delete=models.PROTECT, null=True)

    class Meta(object):
        app_label ='main'
        db_table = 'main_favorito'