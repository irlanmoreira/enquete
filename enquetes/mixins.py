from django.db import transaction
from django.shortcuts import redirect

from enquetes.forms import ChoiceFormSet, QuestionDetailsModelForm

class QuestionFormsMixin:
    def get_choice_formset(self):
        if self.request.method == "POST":
            return ChoiceFormSet(self.request.POST, instance=self.object)
        return ChoiceFormSet(instance=self.object)

    def get_form_detail(self):
        detail = getattr(self.object, "detail", None)
        if self.request.method == "POST":
            return QuestionDetailsModelForm(self.request.POST, instance=detail)
        return QuestionDetailsModelForm(instance=detail)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["choice_formset"] = self.get_choice_formset()
        context["form_detail"] = self.get_form_detail()
        return context

    def form_valid(self, form):
        choice_formset = self.get_choice_formset()
        form_detail = self.get_form_detail()

        if not (choice_formset.is_valid() and form_detail.is_valid()):
            return self.form_invalid(form)

        with transaction.atomic():
            self.object = form.save()
            choice_formset.instance = self.object
            form_detail.instance.question = self.object
            form_detail.save()
            choice_formset.save()
        return redirect(self.get_success_url())



















'''class QuestionFormsMixin:
    def get_choice_formset(self):
        if self.request.method == "POST":
            return ChoiceFormSet(self.request.POST, instance=self.object)
        return ChoiceFormSet(instance=self.object)

    def get_form_detail(self):
        detail = getattr(self.object, "detail", None)
        if self.request.method == "POST":
            return QuestionDetailsModelForm(self.request.POST, instance=detail)
        return QuestionDetailsModelForm(instance=detail)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["choice_formset"] = self.get_choice_formset()
        context["form_detail"] = self.get_form_detail()
        return context

    def form_valid(self, form):
        formset = self.get_choice_formset()
        form_detail = self.get_form_detail()
        if not (formset.is_valid() and form_detail.is_valid()):
            return self.form_invalid(form)
        with transaction.atomic():
            self.object = form.save()
            formset.instance = self.object
            form_detail.instance.question = self.object
            form_detail.save()
            formset.save()
        return redirect(self.get_success_url())'''