from django.core.exceptions import ValidationError


def validate_question_mark(value):
    if not value.strip().endswith('?'):
        raise ValidationError('---O título da pergunta deve terminar com uma interrogação.')