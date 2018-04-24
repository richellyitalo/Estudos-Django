from django.http import HttpResponse

def index(request):
    return HttpResponse('Olá. Essa é a segunda view em django.')