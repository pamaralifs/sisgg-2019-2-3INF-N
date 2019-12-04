from django.db import models

# Create your models here.
class Usuario(models.Model):
    SEXO_CHOICES = [
        ["F", "Feminino"],
        ["M", "Masculino"],
        ["N", "Nenhuma das opções"]
    ]
    nome = models.CharField(max_length=40,verbose_name='Nome')
    email = models.EmailField(max_length=140,verbose_name = 'E-mail',unique=True)
    senha = models.CharField(max_length=8,verbose_name = 'Senha')
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES,verbose_name='Sexo')
    
    def __str__(self):
        return self.nome