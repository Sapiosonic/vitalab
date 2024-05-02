from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages

# Create your views here.
def cadastro(request):
    
    if request.method == "GET":
        
        return render(request, 'cadastro.html')
    
    else:
        
        primeiro_nome = request.POST.get('primeiro_nome')
        ultimo_nome = request.POST.get('ultimo_nome')
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        # verifica se as senhas são iguais
        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não são iguais!')
            return redirect('/usuarios/cadastro')
        
        # Verifica se a senha tem mais de seis digitos
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'A senha deve conter 7 ou mais caracteres!')
            return redirect('/usuarios/cadastro')
        
        # Verifica se o nome de usuário já existe
        if User.objects.filter(username=username).exists():
            messages.add_message(request, constants.ERROR, 'Este nome de usuário já está em uso!')
            return redirect('/usuarios/cadastro')

        try:
            #Username deve ser único
            user = User.objects.create_user(
                first_name=primeiro_nome,
                last_name=ultimo_nome,
                username=username,
                email=email,
                password=senha,
            )
            
            messages.add_message(request, constants.SUCCESS, 'Usuário salvo com sucesso!')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema, contate um administrador!')
            
            return redirect('/usuarios/cadastro')
        
        return redirect('/usuarios/cadastro')