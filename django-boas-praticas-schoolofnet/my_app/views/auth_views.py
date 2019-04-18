from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def login(request):
    context = {
        'app_path': request.get_full_path
    }
    if request.method == 'GET':
        return render(request, 'my_app/login.html', context)

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        # print(vars(user))
        django_login(request, user)

        # Redireciona caso haja next
        next_param = request.GET.get('next')
        if next_param:
            return redirect(next_param)
        return redirect('/home/')

    context['message'] = 'Dados inválidos'
    return render(request, 'my_app/login.html', context)


@login_required(login_url='/login/')
def logout(request):
    django_logout(request)
    return redirect('/login/')