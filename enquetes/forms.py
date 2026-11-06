from django import forms

from enquetes.models import Question

class QuestionForm(forms.Form):
    question_text = forms.CharField(label="Título da enquete", max_length=50, min_length=10)
    closes_at = forms.DateTimeField(label="Fecha em")

    def clean_question_text(self):
        text = self.cleaned_data["question_text"].strip()
        if not text.endswith("?"):
            raise forms.ValidationError("A enquete deve terminar com '?'.")
        return text

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