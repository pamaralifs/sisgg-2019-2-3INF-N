from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.edit import FormView
from .models import Produto
from .forms import ProdutoMeuFormFiltro, ProdutoFormCreateUpdate
# Create your views here.

class ProdutoList(ListView):
    model = Produto
    

class ProdutoListFiltro(ListView): # Optamos por criar uma nova View
    #model = Fornecedor
    #template_name = 'fornecedor/fornecedor_list.html'
    form_class = ProdutoMeuFormFiltro
    model = Produto
    #success_url = reverse_lazy('core:sucesso_inscricao')
    template_name = "produto/produto_list.html"

    def get_queryset(self, **kwargs):
        filtro1 = self.request.GET.get('nome', '') # Pega o conteúdo do campo nome do form
        #print("FILTRO1",filtro1)
        modo_busca = self.request.GET.get('modo_busca', '1')
        #print("MODO BUSCA ANTES")
        #print("MODO BUSCA",modo_busca)
        #print("MODO BUSCA DEPOIS")
        if not filtro1:  # Retorna queryset vazio se for primeira vez
            return Produto.objects.none() 
        elif filtro1.strip() == '*':  # Traz todos se campo nome = '*'
            return Produto.objects.all()
        elif modo_busca == '1':
            return Produto.objects.filter(nome__startswith=filtro1)
        elif modo_busca == '2':
            return Produto.objects.filter(nome__icontains=filtro1)
        elif modo_busca == '3':
            return Produto.objects.filter(nome__endswith=filtro1)
        # Filtra dessa forma caso não ocorra nenhuma condição acima
        return Produto.objects.filter(nome__startswith=filtro1)

    def get_context_data(self, **kwargs):
        context = super(ProdutoListFiltro, self).get_context_data(**kwargs)
        context['form'] = ProdutoMeuFormFiltro # Insere o form no contexto do template
        # Pegar o valor da variável de pesquisa. Se for vazio (=Falso) é porque é a primeira 
        # vez mas para o contexto do template será igual a 1 (=Verdadeiro)
        primeira_vez = self.request.GET.get('nome', '')
        if primeira_vez:
            context['primeira_vez'] = 0
        else:
            context['primeira_vez'] = 1
        #print("PRIMEIRA VEZ",primeira_vez)
        return context


class ProdutoCreate(CreateView):
    model = Produto
    form_class = ProdutoFormCreateUpdate
    #fields = ['nome', 'descricao', 'preco', 'fornecedor']
    success_url = reverse_lazy('produto:produto_read')


class ProdutoUpdate(UpdateView):
    model = Produto
    form_class = ProdutoFormCreateUpdate
    #fields = ['nome', 'descricao', 'preco', 'fornecedor']
    success_url = reverse_lazy('produto:produto_read')


class ProdutoDelete(DeleteView):
    model = Produto
    success_url = reverse_lazy('produto:produto_read')


class ProdutoDetail(DetailView):
    model = Produto
    fields = ['nome', 'descricao', 'preco', 'fornecedor']

