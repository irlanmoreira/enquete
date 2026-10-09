from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from enquetes.models import Question


# Create your views here.

def index(request):
    questions = Question.objects.all()
    context = {"questions": questions}
    return render(request, 'enquetes/index.html',context)

def detalhe(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'enquetes/detalhe.html',{"question":question})