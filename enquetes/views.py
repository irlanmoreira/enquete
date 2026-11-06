from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from enquetes.models import Question
from .forms import QuestionForm


# Create your views here.

def index(request):
    questions = Question.objects.all()
    context = {"questions": questions}
    return render(request, 'enquetes/index.html',context)

def detalhe(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'enquetes/detalhe.html',{"question":question})

def criar_enquete(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            Question.objects.create(
                question_text=form.cleaned_data['question_text'],

                closes_at = form.cleaned_data['closes_at'],
            )
            return redirect('enquetes:index')
    else:
        form = QuestionForm()
    return render(request, 'enquetes/create_question.html', {'form': form})