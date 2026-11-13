from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from enquetes.models import Question
from .forms import QuestionModelForm, SignUpForm, QuestionDetailsModelForm, ChoiceFormSet


# Create your views here.

def index(request):
    questions = Question.objects.all()
    context = {"questions": questions}
    return render(request, 'enquetes/index.html',context)

def detalhe(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'enquetes/detalhe.html',{"question":question})

def criar_enquete(request, pk=None):
    if pk:
        question = get_object_or_404(Question, pk=pk)
    else:
        question = Question()
    if request.method == "POST":
        form_question = QuestionModelForm(request.POST, instance=question)
        form_details = QuestionDetailsModelForm(request.POST, instance=question.detail)
        choice_formset = ChoiceFormSet(request.POST, instance=question)

        if form_question.is_valid() and form_details.is_valid() and choice_formset.is_valid():
            with transaction.atomic():
                question = form_question.save()
                details = form_details.save(commit=False)
                details.question = question
                choice_formset.instance = question
                choice_formset.save()
                details.save()
                return redirect('enquetes:index')
    else:
        form_question = QuestionModelForm(instance=question)
        form_details = QuestionDetailsModelForm(instance=question.detail)
        choice_formset = ChoiceFormSet(instance=question)
    context = {"form_question": form_question, "form_details": form_details, "choice_formset": choice_formset}
    return render(request, 'enquetes/create_question.html', context)

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            return redirect('enquetes:index')
    else:
        form = SignUpForm()

    return render(request, 'enquetes/signup.html', {'form': form})