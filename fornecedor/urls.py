from django.urls import path
from .views import *
# ou FornecedorCreate,FornecedorList,FornecedorUpdate,
# FornecedorDelete,FornecedorDetail

# Definir namespace como informado em urls projeto
app_name = 'fornecedor'

urlpatterns = [
    path('create/', FornecedorCreate.as_view(), name='fornecedor_create'),
    #path('read/', FornecedorList.as_view(), name='fornecedor_read'),
    path('read/', FornecedorListFiltro.as_view(), name='fornecedor_read'),
    path('update/<int:pk>', FornecedorUpdate.as_view(), name='fornecedor_update'),
    path('delete/<int:pk>', FornecedorDelete.as_view(), name='fornecedor_delete'),
    path('detail/<int:pk>', FornecedorDetail.as_view(), name='fornecedor_detail'),
]