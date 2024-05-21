from django.shortcuts import render, get_object_or_404
from .models import Urso,Doacao

def home(request):
    
    Docera = Doacao.objects.all().order_by('-valor')[:5]
    return render(request, 'home.html',{'maiores_doacoes':Docera})

def detalhes_urso(request, urso_id):
    urso = get_object_or_404(Urso, pk=urso_id)
    return render(request, 'detalhes_urso.html', {'urso': urso})

def maiores_doacoes(request):
    # Consulta ao banco de dados para obter as maiores doações
    maiores_doacoes = Doacao.objects.order_by('-valor')[:10]  # Obtém as 10 maiores doações
    return render(request, 'maiores_doacoes.html', {'maiores_doacoes': maiores_doacoes})

def doar(request):
    if request.method == 'POST':
        valor = request.POST.get('valor')
        username = request.POST.get('username')
        Doacao.objects.create(valor=valor, username=username)
        return render(request, 'doacao_sucesso.html')
    return render(request, 'doar.html')

def ursos(request):
    ursos = Urso.objects.all()
    return render(request, 'ursos.html', {'ursos': ursos})

def doacao_sucesso(request):
    return render(request, 'doacao_sucesso.html')
