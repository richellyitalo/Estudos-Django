from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db.models import F
from django.urls import reverse


from .models import Pergunta, Opcao


class IndexView(generic.ListView):
    model = Pergunta

class DetalharView(generic.DetailView):
    model = Pergunta


class ResultadosView(generic.DetailView):
    model = Pergunta
    template_name = 'enquete/resultados.html'


def index(request):
    context = {
        'perguntas': Pergunta.objects.all()
    }
    return render(request, 'enquete/index.html', context)


def view(request, id_da_enquete):
    pergunta = get_object_or_404(Pergunta, pk=id_da_enquete)
    context = {'pergunta': pergunta}
    return render(request, 'enquete/view.html', context)


def votar(request, id_pergunta):
    pergunta = get_object_or_404(Pergunta, pk=id_pergunta)
    try:
        opcao = pergunta.opcao_set.get(pk=request.POST['opcao'])
    except (KeyError, Opcao.DoesNotExist):
        return render(request, 'enquete/pergunta_detail.html', {
            'mensagem_de_erro': 'Selecione uma opção'
        })
    else:
        opcao.votacoes = F('votacoes') + 1
        opcao.save()
        return HttpResponseRedirect(reverse('enquete:resultados', args=(pergunta.id,)))
