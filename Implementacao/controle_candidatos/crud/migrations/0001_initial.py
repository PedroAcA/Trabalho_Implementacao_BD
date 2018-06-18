# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('idCargo', models.IntegerField(serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=200, null=True)),
                ('salario', models.FloatField(null=True)),
                ('competencias', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('idPartido', models.IntegerField(serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=200, null=True)),
                ('sede', models.CharField(max_length=200, null=True)),
                ('nomePresidente', models.CharField(max_length=200, null=True)),
                ('qtdFiliados', models.IntegerField(null=True)),
                ('dataCriacao', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Politico',
            fields=[
                ('idPolitico', models.IntegerField(serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('apelido', models.CharField(max_length=200)),
                ('foto', models.BinaryField()),
                ('idCargo', models.ForeignKey(to='crud.Cargo')),
                ('idPartido', models.ForeignKey(to='crud.Partido')),
            ],
        ),
    ]
