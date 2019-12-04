from django.urls import path, include
from .views import *

app_name = 'core'

urlpatterns = [
    path('menu/', Menu.as_view(),name='menu'),
    path('inscricao/', UsuarioInscricao.as_view(),name='usuario_inscricao'),
    path('sucesso/', SucessoInscricao.as_view(),name='sucesso_inscricao'),
]
