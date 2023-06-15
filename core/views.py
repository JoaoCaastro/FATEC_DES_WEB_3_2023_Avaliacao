from django.http import HttpResponse
from django.shortcuts import render
from .forms import ModelAlunoForm
from .models import ModelAluno

def cadastro(request):
    if request.method == 'POST':
        form = ModelAlunoForm(request.POST)
        if form.is_valid():
            aluno = form.data['aluno']
            professor = form.data['professor']
            form.save()
            return render(request, 'index.html', {'form': form})

    else:
        form = ModelAlunoForm()
    return render(request, 'index.html', {'form': form})

def listar(request):
    presentes = ModelAluno.objects.all()
    context = {'listaPresentes': presentes}
    return render(request, 'listar.html', context)