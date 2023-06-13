from django.db import models

class modelAluno(models.Model):
    nomeCompleto = models.CharField('nomeCompleto', max_length=150)
    professores = models.CharField('professores', max_length=150)