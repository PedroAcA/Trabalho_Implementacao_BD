# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#ref para binaryfiled de https://docs.djangoproject.com/en/1.11/ref/models/fields/ em 17/06/2018
# Create your models here.
class Partido (models.Model):
	idPartido = models.IntegerField(primary_key=True)
	nome = models.CharField(max_length=200,null=True)
	sede = models.CharField(max_length=200,null=True)
	nomePresidente = models.CharField(max_length=200,null=True)
	qtdFiliados = models.IntegerField(null=True)
	dataCriacao = models.DateField(null=True)

class Cargo (models.Model):
	idCargo = models.IntegerField(primary_key=True)
	nome = models.CharField(max_length=200,null=True)
	salario = models.FloatField(null=True)
	competencias = models.CharField(max_length=200,null=True)

class Politico (models.Model):
	idPolitico = models.IntegerField(primary_key=True)
	nome = models.CharField(max_length=200,null=False)
	apelido = models.CharField(max_length=200,null=False)
	foto = models.BinaryField()
	idPartido = models.ForeignKey('Partido')
	idCargo = models.ForeignKey('Cargo')
