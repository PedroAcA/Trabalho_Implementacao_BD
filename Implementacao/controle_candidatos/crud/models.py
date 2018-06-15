# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Partido (models.Model):
	idPartido = models.IntegerField(primary_key=True)
	nome = models.TextField(null=True)
	sede = models.TextField(null=True)
	nomePresidente = models.TextField(null=True)
	qtdFiliados = models.IntegerField(null=True)
	dataCriacao = models.DateField(null=True)

class Cargo (models.Model):
	idCargo = models.IntegerField(primary_key=True)
	nome = models.TextField(null=True)
	salario = models.FloatField(null=True)
	competencias = models.TextField(null=True)

class Politico (models.Model):
	idPolitico = models.IntegerField(primary_key=True)
	nome = models.TextField(null=False)
	apelido = models.TextField(null=False)
	foto = models.FileField(upload_to='Trabalho_Implementacao_BD/')
	idPartido = models.ForeignKey(Partido,on_delete=models.CASCADE)
	idCargo = models.ForeignKey(Cargo,on_delete=models.CASCADE)