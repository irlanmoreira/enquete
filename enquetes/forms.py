from django import forms
from django.forms.models import inlineformset_factory

from enquetes.models import Question, Detail, Choice


class QuestionForm(forms.Form):
    question_text = forms.CharField(label="Título da enquete", max_length=50, min_length=10)
    closes_at = forms.DateTimeField(label="Fecha em")

    def clean_question_text(self):
        text = self.cleaned_data["question_text"].strip()
        if not text.endswith("?"):
            raise forms.ValidationError("A enquete deve terminar com '?'.")
        return text

class QuestionModelForm(forms.ModelForm):
    class Meta:
        model = Question
        fields=['question_text', 'closes_at']
        labels = {'closes_at': 'Fecha em'}

    def clean_question_text(self):
        text = self.cleaned_data["question_text"].strip()
        if not text.endswith("?"):
            raise forms.ValidationError("A enquete deve terminar com '?'.")
        return text

class QuestionDetailsModelForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = ['description', 'difficulty']
        widgets = {'description': forms.Textarea(attrs={'rows': 4})}

class SignUpForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', 'A senha não confere.')

        return cleaned_data

ChoiceFormSet = inlineformset_factory(
    Question,
    Choice,
    fields=['choice_text'],
    extra=1,
    min_num=2,
    validate_min=True,
    can_delete=True,
)