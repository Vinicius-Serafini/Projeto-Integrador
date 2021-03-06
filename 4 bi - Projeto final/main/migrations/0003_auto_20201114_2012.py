# Generated by Django 3.1.2 on 2020-11-14 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201019_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, null=True)),
                ('descricao', models.CharField(max_length=600, null=True)),
                ('roupa', models.BooleanField()),
                ('alimento', models.BooleanField()),
                ('dinheiro', models.BooleanField()),
                ('email', models.CharField(max_length=100, null=True)),
                ('whatsapp', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'main_doacao',
            },
        ),
        migrations.DeleteModel(
            name='Publicacao',
        ),
    ]
