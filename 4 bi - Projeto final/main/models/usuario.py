from django.db import models


class Usuario(models.Model):

    email = models.CharField(max_length=50, null=True)
    senha = models.CharField(max_length=150, null=True)
    nome = models.CharField(max_length=100, null=True)
    cidade = models.CharField(max_length=100, null=True)
    uf = models.CharField(max_length=2, null=True)

    class Meta(object):
        app_label ='main'
        db_table = 'main_usuario'