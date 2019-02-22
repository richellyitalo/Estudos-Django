from django.shortcuts import render, redirect
from django.contrib import messages

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def register(request):
    if request.method == 'POST':
        # Cadastra novo usuário
        messages.error(request, 'Dados inválidos')
        return render(request, 'accounts/register.html')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        # Autenticação
        print('Autenticação')
    else:
        return render(request, 'accounts/login.html')
    
def logout(request):
    # Deslogar
    return redirect('home')