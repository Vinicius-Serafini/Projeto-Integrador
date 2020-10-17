from django.db import models


class Publicacao(models.Model):

    class Meta(object):
        app_label ='main'
        db_table = 'main_publicacao'