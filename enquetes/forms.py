from django import forms

class QuestionForm(forms.Form):
    question_text = forms.CharField(label="Título da enquete", max_length=50, min_length=10)
    closes_at = forms.DateTimeField(label="Fecha em")

    def clean_question_text(self):
        text = self.cleaned_data["question_text"].strip()
        if not text.endswith("?"):
            raise forms.ValidationError("A enquete deve terminar com '?'.")
        return text