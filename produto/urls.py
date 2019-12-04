from django.urls import path
from .views import *
# ou ProdutoCreate,ProdutoList,ProdutoUpdate,
# ProdutoDelete,ProdutoDetail

# Definir namespace como informado em urls projeto
app_name = 'produto'

urlpatterns = [
    path('create/', ProdutoCreate.as_view(), name='produto_create'),
    #path('read/', ProdutoList.as_view(), name='produto_read'),
    path('read/', ProdutoListFiltro.as_view(), name='produto_read'),
    path('update/<int:pk>', ProdutoUpdate.as_view(), name='produto_update'),
    path('delete/<int:pk>', ProdutoDelete.as_view(), name='produto_delete'),
    path('detail/<int:pk>', ProdutoDetail.as_view(), name='produto_detail'),
]