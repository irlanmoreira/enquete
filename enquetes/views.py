from typing import Any

from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.list import ListView

from enquetes.models import Question, Detail
from .mixins import QuestionFormsMixin
from .forms import QuestionModelForm, SignUpForm, QuestionDetailsModelForm, ChoiceFormSet


# Create your views here.

def index(request):
    questions = Question.objects.all()
    context = {"questions": questions}
    return render(request, 'enquetes/index.html',context)

class ListQuestionView(ListView):
    model = Question
    template_name = 'enquetes/index.html'
    context_object_name = 'questions'

def detalhe(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'enquetes/detalhe.html',{"question":question})

class DetailQuestionView(DetailView):
    model = Question
    template_name = 'enquetes/detalhe.html'
    pk_url_kwarg = 'question_id'
def criar_enquete(request, pk=None):
    if pk:
        question = get_object_or_404(Question, pk=pk)
    else:
        question = Question()
        details = Detail()
    if request.method == "POST":
        form_question = QuestionModelForm(request.POST,request.FILES, instance=question)
        form_details = QuestionDetailsModelForm(request.POST, instance=details)
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
        form_details = QuestionDetailsModelForm(instance=details)
        choice_formset = ChoiceFormSet(instance=question)
    context = {"form_question": form_question, "form_details": form_details, "choice_formset": choice_formset}
    return render(request, 'enquetes/create_question.html', context)

class CreateQuestionView(QuestionFormsMixin, CreateView):
    model = Question
    template_name = 'enquetes/create_question.html'
    form_class = QuestionModelForm
    success_url = reverse_lazy('enquetes:index')

    '''def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["choice_formset"] = ChoiceFormSet(self.request.POST)
            context["form_details"] = QuestionDetailsModelForm(self.request.POST)
        else:
            context["choice_formset"] = ChoiceFormSet()
            context["form_details"] = QuestionDetailsModelForm()
        return context

    def form_valid(self, form):
        choice_formset = ChoiceFormSet(self.request.POST)
        form_details = QuestionDetailsModelForm(self.request.POST)
        if not (choice_formset.is_valid() and form_details.is_valid()):
            return self.form_invalid(form)

        with transaction.atomic():
            self.object = form.save()
            details = form_details.save(commit=False)
            details.question = self.object
            choice_formset.instance = self.object
            choice_formset.save()
            details.save()
            return redirect(self.get_success_url())'''

class UpdateQuestionView(QuestionFormsMixin, UpdateView):
    model = Question
    form_class = QuestionModelForm
    template_name = 'enquetes/create_question.html'
    success_url = reverse_lazy('enquetes:index')

    '''def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["choice_formset"] = ChoiceFormSet(self.request.POST, instance=self.object)
            context["form_details"] = QuestionDetailsModelForm(self.request.POST, instance=self.object.detail)
        else:
            print(self.object.detail)
            context["choice_formset"] = ChoiceFormSet(instance=self.object)
            context["form_details"] = QuestionDetailsModelForm(instance=self.object.detail)
        return context

    def form_valid(self, form):
        choice_formset = ChoiceFormSet(self.request.POST, instance=self.object)
        form_details = QuestionDetailsModelForm(self.request.POST, instance=self.object.detail)
        if not choice_formset.is_valid() or not form_details.is_valid():
            return self.form_invalid(form)
        with transaction.atomic():
            form_details.save()
            choice_formset.save()
            form.save()
            return redirect(self.get_success_url())'''

class DeleteQuestionView(DeleteView):
    model = Question
    success_url = reverse_lazy('enquetes:index')
    template_name = 'enquetes/delete.html'

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            return redirect('enquetes:index')
    else:
        form = SignUpForm()

    return render(request, 'enquetes/signup.html', {'form': form})