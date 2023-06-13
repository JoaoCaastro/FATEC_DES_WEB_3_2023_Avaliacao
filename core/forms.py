from django import forms
from .models import modelAluno

class modelAlunoForm(forms.ModelForm):
    class Meta:
        model = modelAluno
        fields = ('nomeCompleto', 'professores')
        widgets = {
            'professores': forms.Select(choices=[('1', 'Orlando'), ('2','Thiago')])
        }