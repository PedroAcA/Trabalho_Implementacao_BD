# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvaliacaoPopular',
            fields=[
                ('idAvaliacaoPopular', models.AutoField(serialize=False, primary_key=True)),
                ('nota', models.IntegerField()),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dataNascimento', models.DateField()),
            ],
        ),
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
            name='Doador',
            fields=[
                ('idDoador', models.AutoField(serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('valor', models.FloatField()),
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
        migrations.CreateModel(
            name='Politico_Cargo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nroEleitora', models.IntegerField()),
                ('tipoLocalCargo', models.CharField(max_length=1)),
                ('nomeLocalCargo', models.CharField(max_length=200)),
                ('idCargo', models.ForeignKey(to='crud.Cargo')),
                ('idPolitico', models.ForeignKey(to='crud.Politico')),
            ],
        ),
        migrations.CreateModel(
            name='Politico_Doador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idDoador', models.ForeignKey(to='crud.Doador')),
                ('idPolitico', models.ForeignKey(to='crud.Politico')),
            ],
        ),
        migrations.CreateModel(
            name='Politico_Processos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idPolitico', models.ForeignKey(to='crud.Politico')),
            ],
        ),
        migrations.CreateModel(
            name='PoliticoEmMandato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dataPosse', models.DateField()),
                ('idPoliticoEmMandato', models.ForeignKey(to='crud.Politico')),
            ],
        ),
        migrations.CreateModel(
            name='Processo',
            fields=[
                ('idProcesso', models.AutoField(serialize=False, primary_key=True)),
                ('descricao', models.CharField(max_length=200)),
                ('dataCriacao', models.CharField(max_length=200)),
                ('terminou', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PromessasCampanha',
            fields=[
                ('idPromessasCampanha', models.AutoField(serialize=False, primary_key=True)),
                ('plano', models.CharField(max_length=200)),
                ('descricao', models.CharField(max_length=200)),
                ('dataOrigem', models.CharField(max_length=200)),
                ('idCandidato', models.ForeignKey(to='crud.Candidato')),
            ],
        ),
        migrations.AddField(
            model_name='politico_processos',
            name='idProcesso',
            field=models.ForeignKey(to='crud.Processo'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='idCandidato',
            field=models.ForeignKey(to='crud.Politico'),
        ),
        migrations.AddField(
            model_name='avaliacaopopular',
            name='idPoliticoAvaliado',
            field=models.ForeignKey(to='crud.PoliticoEmMandato'),
        ),
    ]
