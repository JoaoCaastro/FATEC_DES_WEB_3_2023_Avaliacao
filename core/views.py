from django.shortcuts import render
from core.forms import modelAlunoForm
from core.models import modelAluno

def cadastro(request):
    if request.method == 'POST':
        form = modelAlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
    
    else:
        form = modelAlunoForm()
    return render(request, 'index.html', {'form': form})
