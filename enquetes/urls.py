from django.urls import path
from . import views

app_name = 'enquetes'
urlpatterns = [
    path('', views.index, name='index'),
    path('detalhe/<int:question_id>', views.detalhe, name='detalhe'),
    path('enquete',views.criar_enquete,name='criar_enquete'),

]
