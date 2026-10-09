from django.db import models

# Create your models here.
class Choice(models.Model):
    choice_text = models.CharField("Texto", max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey("Question", on_delete=models.CASCADE, verbose_name="choices", related_name="choices")

    def __str__(self):
        return self.choice_text

class Category(models.Model):
    name = models.CharField("Nome", max_length=200, unique=True)
    def __str__(self):
        return self.name

class Question(models.Model):
    class Status(models.TextChoices):
        RASCUNHO = "R", "RASCUNHO"
        PUBLICADA = "P", "PUBLICADA"

    question_text = models.CharField("Texto", max_length=200, unique=True)
    status = models.CharField(max_length=1, choices=Status, default=Status.RASCUNHO)
    pub_date = models.DateField("Data de publicação", auto_now_add=True)
    closes_at = models.DateTimeField(null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name="questions", verbose_name="Categorias")


    class Meta:
        ordering = ["-pub_date"]
        verbose_name = "Enquete"
        verbose_name_plural = "Enquetes"

    def __str__(self):
        return self.question_text

class Detail(models.Model):
    description = models.TextField(verbose_name='Descrição')
    question = models.OneToOneField(Question, on_delete=models.CASCADE)

class Author(models.Model):
    name = models.CharField("Nome", max_length=200)
    email = models.CharField("Email", max_length=200)

class Book(models.Model):
    title = models.CharField("Titulo", max_length=200)
