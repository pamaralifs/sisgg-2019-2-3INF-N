# Arquivo criado para implementar filtro na view listview
from django import forms
#from fornecedor.models import Fornecedor

class FornecedorMeuFormFiltro(forms.Form):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Digite o nome'}))
    #class Meta:
    #    model = Fornecedor
    #    fields = ['nome']