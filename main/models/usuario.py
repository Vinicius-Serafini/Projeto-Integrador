from django.db import models


class Usuario(models.Model):

    class Meta(object):
        app_label ='main'
        db_table = 'main_usuario'