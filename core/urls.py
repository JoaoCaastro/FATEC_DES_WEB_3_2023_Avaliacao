from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastro, name='index'),
    path('listar', views.listar, name='listar'),

]