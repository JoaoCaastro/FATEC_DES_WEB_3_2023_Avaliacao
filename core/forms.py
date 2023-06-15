from .models import ModelAluno
from django.forms import ModelForm

class ModelAlunoForm(ModelForm):
    class Meta:
        model = ModelAluno
        fields = ['aluno','professor']