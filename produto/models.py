from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=50,verbose_name='Produto')
    descricao = models.TextField(max_length=255,verbose_name='Descrição')
    preco = models.DecimalField(max_digits=9,decimal_places=2,verbose_name='Preço')
    fornecedor = models.ForeignKey('fornecedor.Fornecedor',on_delete=models.CASCADE)

    def __str__(self):
        return self.nome