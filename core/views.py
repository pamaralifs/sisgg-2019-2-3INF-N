from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView
from django.views.generic.edit import FormView
from .models import Usuario
from .forms import UsuarioFormInscricao, UsuarioFormEntrar
from django.db.models import Q

# Create your views here.
class UsuarioCreate_OR_OLD(CreateView):
    model = Usuario
    form = UsuarioFormInscricao()
    fields = ['nome','email','senha','sexo']
    success_url = reverse_lazy('core:sucesso_inscricao')

class UsuarioInscricao(FormView):
    form_class = UsuarioFormInscricao
    model = Usuario
    success_url = reverse_lazy('core:sucesso_inscricao')
    template_name = "core/usuario_form.html"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        #form.send_email()
        #dados_form = form.data
        #if (dados_form['senha'] != dados_form['confirma_senha']):  ou
        if (self.request.POST.get('senha') != self.request.POST.get('confirma_senha')):
           self.mensagem = 'Senha e confirmação de senha não coincidem!'
           return super().form_invalid(form)
        elif Usuario.objects.filter(email=self.request.POST.get('email')):
           self.mensagem = 'Já existe um usuário inscrito com este e-mail!'
           return super().form_invalid(form)
        else:
            usu_nome = self.request.POST.get('nome')
            usu_email = self.request.POST.get('email')
            usu_senha = self.request.POST.get('senha')
            usu_sexo = self.request.POST.get('sexo')
            novo_usuario = Usuario(nome=usu_nome,email=usu_email,senha=usu_senha,sexo=usu_sexo)
            novo_usuario.save()
            return super().form_valid(form)
        #   new_post = Post(title=post_title, slug=post_slug, body=post_body, author=post_author, status=post_status)
        #   new_post.save()
        #   return redirect('blog:post_list')
        #FBV
        #if not form.is_valid():
        #   return render(request, 'ticket_novo.html',{'form': form})
    def get_context_data(self, **kwargs):
        context = super(UsuarioInscricao, self).get_context_data(**kwargs)
        context['form'] = UsuarioFormInscricao # Insere o form no contexto do template
        #print('TESTE',self.request.POST.get('email'))
        if not self.request.POST.get('email'):
            self.mensagem = ''
        context['mensagem'] = self.mensagem
        return context

class Entrar(FormView):
    form_class = UsuarioFormEntrar
    success_url = reverse_lazy('core:menu') #temporario
    template_name = "core/index.html"
    model = Usuario

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        #form.send_email()
        filtro1 = self.request.POST.get('email')
        filtro2 = self.request.POST.get('senha')
        #print('FILTRO1 ',filtro1)
        #print('FILTRO2 ',filtro2)
        #print('passei')
        criterion1 = Q(email=filtro1)
        criterion2 = Q(senha=filtro2)
        if Usuario.objects.filter(email=self.request.POST.get('email'), senha=self.request.POST.get('senha')):
            return super().form_valid(form)
        else:
            return super().form_invalid(form)
        #return super().form_valid(form)
        
    def get_context_data(self, **kwargs):
        context = super(Entrar, self).get_context_data(**kwargs)
        context['form'] = UsuarioFormEntrar # Insere o form no contexto do template
        #print('TESTE',self.request.POST.get('email'))
        if self.request.POST.get('email'):
            context['mensagem'] = 'E-mail e/ou senha inválidos!'
        else:
            context['mensagem'] = ''
        return context


class SucessoInscricao(TemplateView):
    template_name = "core/sucesso_inscricao.html"

class Menu(TemplateView):
    template_name = "core/menu.html"