from django.db import models

class ModelAluno(models.Model):
    aluno = models.CharField(max_length=150)
    select = [
        ('1', 'Orlando'),
        ('2', 'Mendes')
    ]
    professor = models.CharField(max_length=150, choices=select)