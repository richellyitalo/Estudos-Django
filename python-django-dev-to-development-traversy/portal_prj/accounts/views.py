from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

from contacts.models import Contact

def accounts(request):
    return redirect('dashboard')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username já está cadastrado')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'E-mail já está cadastrado')
                return redirect('register')
            else:
                # OK
                user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
                user.save()
                # Logando após registrar
                # auth.login(request, user)
                # messages.success(request, 'Usuário criado e logado com sucesso')
                # return redirect('index')
                messages.success(request, 'Conta criada. Agora você precisa se autenticar')
                return redirect('login')
        else:
            messages.error(request, 'As senhas não estão iguais')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Agora você está logado')
            return redirect('dashboard')
        else:
            messages.error(request, 'Dados inválidos')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Você foi deslogado')
        return redirect('index')

def dashboard(request):
    if not request.user.is_authenticated:
        messages.error(request, 'É necessário que você esteja logado')
        return redirect('login')

    user_contacts = Contact.objects.filter(user_id=request.user.id).order_by('-contact_date')
    context = {
        'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)

