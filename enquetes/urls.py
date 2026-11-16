from django.urls import path
from . import views

app_name = 'enquetes'
urlpatterns = [
    path('', views.ListQuestionView.as_view(), name='index'),
    path('detalhe/<int:question_id>', views.DetailQuestionView.as_view(), name='detalhe'),
    path('enquete',views.CreateQuestionView.as_view(),name='criar_enquete'),
    path('enquete/<int:pk>', views.criar_enquete, name='editar_enquete'),

]
