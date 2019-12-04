from django import forms
from core.models import Usuario

class UsuarioFormInscricao(forms.Form):
    #<option value="" selected="selected" hidden="hidden">Choose here</option>
    SEXO_CHOICES = [
        ["","Selecione o sexo"],
        ["F", "Feminino"],
        ["M", "Masculino"],
        ["N", "Nenhuma das opções"]
    ]
    nome = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Digite seu nome'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Digite seu email'}))
    sexo = forms.ChoiceField(initial='',choices=SEXO_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Digite sua senha','maxlength':'8'}))
    confirma_senha = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Repita sua senha','maxlength':'8'}))

class UsuarioFormInscricao_OR(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome','email','senha','sexo']

class UsuarioFormEntrar(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Digite seu email'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Digite sua senha','maxlength':'8'}))

    



        
        


    
