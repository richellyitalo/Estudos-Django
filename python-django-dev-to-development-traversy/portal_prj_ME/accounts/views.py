from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            messages.error(request, 'Senha de confirmação deve ser igual a senha')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username em uso')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'E-mail em uso')
            return redirect('register')
            
        user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
        user.save()

        # Autenticar
        # auth.login(request, user)
        # messages.success(request, 'Conta criada e autenticada')
        # return redirect('home')

        messages.success(request, 'Conta criada  com sucesso. Realize login')
        return redirect('login')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        # Autenticação
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Autenticado com sucesso')
            return redirect('dashboard')
        else:
            messages.error(request, 'Dados inválidos')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')
    
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')