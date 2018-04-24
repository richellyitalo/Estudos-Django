from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Question


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
#     return render(request, 'polls/details.html', {'question': question})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # question_text = Question.objects.get(pk=question_id).question_text
    return render(request, 'polls/details.html', {'question': question})


def results(request, question_id):
    response = 'Você está procurando resultados da questão %s.'
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse('Você está votando na equestão %s.' % question_id)
