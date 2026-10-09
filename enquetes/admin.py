from django.contrib import admin

# Register your models here.
from .models import Question, Choice, Category, Detail


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4
    readonly_fields = ['votes']

class DetailInline(admin.TabularInline):
    model = Detail


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date']
    list_filter = ['pub_date']
    search_fields = ['question_text']
    readonly_fields = ['pub_date']
    inlines = [ChoiceInline, DetailInline]

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice_text', 'votes']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
