# Arquivo criado para implementar filtro na view listview
from django import forms
from produto.models import Produto
from fornecedor.models import Fornecedor

class ProdutoMeuFormFiltro(forms.Form):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Digite o nome'}))
    #class Meta:
    #    model = Produto
    #    fields = ['nome']

#o form abaixo deu certo para create e update
#dimensionamento de linhas do Textarea (area minúsculo)
class ProdutoFormCreateUpdate(forms.ModelForm):
    nome = forms.CharField()
    descricao = forms.CharField(widget=forms.Textarea(attrs={'rows':'3','columns':'10'}))
    preco = forms.CharField()
    fornecedor = forms.ModelChoiceField(queryset=Fornecedor.objects.all())
    class Meta:
        model = Produto
        exclude = ['id']