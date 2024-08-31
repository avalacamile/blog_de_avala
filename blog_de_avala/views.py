from django.shortcuts import render
from django.shortcuts import render
from .models import*

# Create your views here.

def index(request):
    avala = Pessoa.objects.all()
    dados = {
        'Estudante':  avala,
    }
    return render(request, 'blog/index.html',dados)

def sobre_eu(request):
    avala = Pessoa.objects.all()
    dados = {
        'Estudante':  avala,
    }
    return render(request, 'blog/sobre.html',dados)
# Create your views here.
