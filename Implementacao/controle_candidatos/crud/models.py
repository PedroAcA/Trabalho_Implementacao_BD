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

class PoliticoEmMandato (models.Model):
	idPoliticoEmMandato=models.ForeignKey('Politico')
	dataPosse = models.DateField()

class Candidato (models.Model):
	idCandidato = models.ForeignKey('Politico')
	dataNascimento = models.DateField()

class Politico_Cargo (models.Model):
	idPolitico = models.ForeignKey('Politico')
	idCargo = models.ForeignKey('Cargo')
	nroEleitora = models.IntegerField()
	tipoLocalCargo = models.CharField(max_length=1)
	nomeLocalCargo = models.CharField(max_length=200)

class Processo (models.Model):
	idProcesso = models.AutoField(primary_key=True)
	descricao = models.CharField(max_length=200)
	dataCriacao = models.CharField(max_length=200)
	terminou = models.CharField(max_length=200)

class Politico_Processos (models.Model):
	idPolitico = models.ForeignKey('Politico')
	idProcesso = models.ForeignKey('Processo')

class Doador (models.Model):
	idDoador = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=200)
	valor = models.FloatField()

class Politico_Doador (models.Model):
	idPolitico = models.ForeignKey('Politico')
	idDoador = models.ForeignKey('Doador')

class AvaliacaoPopular (models.Model):
	idAvaliacaoPopular = models.AutoField(primary_key=True)
	idPoliticoAvaliado = models.ForeignKey('PoliticoEmMandato')
	nota = models.IntegerField()
	descricao = models.CharField(max_length=200)

class PromessasCampanha (models.Model):
	idPromessasCampanha = models.AutoField(primary_key=True)
	idCandidato = models.ForeignKey('Candidato')
	plano = models.CharField(max_length=200)
	descricao = models.CharField(max_length=200)
	dataOrigem = models.CharField(max_length=200)
	
