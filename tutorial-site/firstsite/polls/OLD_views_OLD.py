from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import F

from .models import Question, Choice

'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    # output = '<br/> '.join([q.question_text for q in latest_question_list])
    context = {
        'latest_question_list': latest_question_list
    }
    return HttpResponse(template.render(context, request))
'''


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404('Questão não existe.')
#     # question_text = Question.objects.get(pk=question_id).question_text
#     return render(request, 'polls/detail.html', {'question': question})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # question_text = Question.objects.get(pk=question_id).question_text
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'Você não selecionou nenhum opção'
        })
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
