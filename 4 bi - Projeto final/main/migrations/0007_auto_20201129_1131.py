# Generated by Django 3.1.2 on 2020-11-29 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20201128_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacao',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.usuario'),
        ),
        migrations.CreateModel(
            name='Favorito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicacao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.publicacao')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.usuario')),
            ],
            options={
                'db_table': 'main_favorito',
            },
        ),
    ]
