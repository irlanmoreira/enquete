from django.urls import path
from . import views

app_name = 'enquetes'
urlpatterns = [
    path('', views.index, name='index'),
    path('detalhe', views.detalhe, name='detalhe'),
]
