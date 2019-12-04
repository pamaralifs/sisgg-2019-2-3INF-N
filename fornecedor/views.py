from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.edit import FormView
from .models import Fornecedor
from .forms import FornecedorMeuFormFiltro
# Create your views here.

class FornecedorList(ListView):
    model = Fornecedor
    

class FornecedorListFiltro(ListView): # Optamos por criar uma nova View
    #model = Fornecedor
    #template_name = 'fornecedor/fornecedor_list.html'
    form_class = FornecedorMeuFormFiltro
    model = Fornecedor
    #success_url = reverse_lazy('core:sucesso_inscricao')
    template_name = "fornecedor/fornecedor_list.html"

    def get_queryset(self, **kwargs):
        filtro1 = self.request.GET.get('nome', '') # Pega o conteúdo do campo nome do form
        #print("FILTRO1",filtro1)
        modo_busca = self.request.GET.get('modo_busca', '1')
        #print("MODO BUSCA ANTES")
        #print("MODO BUSCA",modo_busca)
        #print("MODO BUSCA DEPOIS")
        if not filtro1:  # Retorna queryset vazio se for primeira vez
            return Fornecedor.objects.none() 
        elif filtro1.strip() == '*':  # Traz todos se campo nome = '*'
            return Fornecedor.objects.all()
        elif modo_busca == '1':
            return Fornecedor.objects.filter(nome__startswith=filtro1)
        elif modo_busca == '2':
            return Fornecedor.objects.filter(nome__icontains=filtro1)
        elif modo_busca == '3':
            return Fornecedor.objects.filter(nome__endswith=filtro1)
        # Filtra dessa forma caso não ocorra nenhuma condição acima
        return Fornecedor.objects.filter(nome__startswith=filtro1)

    def get_context_data(self, **kwargs):
        context = super(FornecedorListFiltro, self).get_context_data(**kwargs)
        context['form'] = FornecedorMeuFormFiltro # Insere o form no contexto do template
        # Pegar o valor da variável de pesquisa. Se for vazio (=Falso) é porque é a primeira 
        # vez mas para o contexto do template será igual a 1 (=Verdadeiro)
        primeira_vez = self.request.GET.get('nome', '')
        if primeira_vez:
            context['primeira_vez'] = 0
        else:
            context['primeira_vez'] = 1
        #print("PRIMEIRA VEZ",primeira_vez)
        return context


class FornecedorCreate(CreateView):
    model = Fornecedor
    fields = ['nome', 'cnpj', 'ddd_telefone', 'telefone']
    success_url = reverse_lazy('fornecedor:fornecedor_read')


class FornecedorUpdate(UpdateView):
    model = Fornecedor
    fields = ['nome', 'cnpj', 'ddd_telefone', 'telefone']
    success_url = reverse_lazy('fornecedor:fornecedor_read')


class FornecedorDelete(DeleteView):
    model = Fornecedor
    success_url = reverse_lazy('fornecedor:fornecedor_read')


class FornecedorDetail(DetailView):
    model = Fornecedor
    fields = ['nome', 'cnpj', 'ddd_telefone', 'telefone']

