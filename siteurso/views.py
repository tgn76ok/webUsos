from django.shortcuts import render, get_object_or_404
from .models import Urso,Doacao
from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

def home(request):
    
    Docera = Doacao.objects.all().order_by('-valor')[:10]
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
        valor = request.POST.get('value')
        username = request.POST.get('username')
        
        errors = []

        # Verifica se 'valor' e 'username' não estão vazios
        if not valor:
            errors.append("O campo 'valor' é obrigatório.")
        else:
            try:
                valor = float(valor)
                MinValueValidator(0.01)(valor)  # Garante que 'valor' seja positivo
            except ValueError:
                errors.append("O campo 'valor' deve ser um número.")
            except ValidationError:
                errors.append("O valor deve ser maior que zero.")

        if not username:
            errors.append("O campo 'username' é obrigatório.")

        # Se houver erros, renderiza o formulário com mensagens de erro
        if errors:
            return render(request, 'doar.html', {'errors': errors})

        # Se não houver erros, cria a instância de Doacao
        Doacao.objects.create(valor=valor, username=username)
        
        return render(request, 'doacao_sucesso.html')
    
    return render(request, 'doar.html')

def ursos(request):
    ursos = Urso.objects.all()
    return render(request, 'ursos.html', {'ursos': ursos})

def doacao_sucesso(request):
    return render(request, 'doacao_sucesso.html')
