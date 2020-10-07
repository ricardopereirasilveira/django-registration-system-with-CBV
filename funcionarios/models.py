from django.db import models


class DocumentoRG(models.Model):
    numeroRG = models.CharField(max_length=8, blank=True, null=True)

    def __str__(self):
        return self.numeroRG


class DocumentoCPF(models.Model):
    numeroCPF = models.CharField(max_length=11)

    def __str__(self):
        return self.numeroCPF


class Funcionario(models.Model):
    primeiroNome = models.CharField(max_length=30)
    ultimoNome = models.CharField(max_length=30)
    idade = models.IntegerField()
    email = models.EmailField()
    profile = models.ImageField(blank=True, null=True, upload_to='func_pictures')
    dataNascimento = models.DateField()
    acessarSistema = models.BooleanField(default=False)
    rg = models.OneToOneField(DocumentoRG, on_delete=models.DO_NOTHING, blank=True, null=True)
    cpf = models.OneToOneField(DocumentoCPF, on_delete=models.CASCADE, blank=True, null=True)

    def hasPicture(self):
        if self.profile:
            return True
        else:
            return False
    hasPicture.short_description = 'Possui Foto'



class Produtos(models.Model):
    produto = models.CharField(max_length=100)
    preco = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.produto

class Vendas(models.Model):
    numero = models.PositiveIntegerField()
    valor = models.DecimalField(decimal_places=2, max_digits=10)
    desconto = models.DecimalField(decimal_places=2, max_digits=10)
    imposto = models.DecimalField(decimal_places=2, max_digits=10)
    person = models.ForeignKey(Funcionario, null=True, blank=True, on_delete=models.PROTECT)
    produtos = models.ManyToManyField(Produtos, blank=True, default='NULL')

    def nomeCompleto(self):
        return self.person.primeiroNome + ' ' + self.person.ultimoNome
    nomeCompleto.short_description = 'Nome Completo'

    def aPagar(self):
        valorTotal = 0
        for produto in self.produtos.all():
            valorTotal += produto.preco
        valorTotal = (valorTotal + self.imposto) - self.desconto
        return valorTotal
    aPagar.short_description = 'A Pagar'

    def valorCompra(self):
        totalCompra = 0
        for produto in self.produtos.all():
            totalCompra += produto.preco
        return totalCompra
    valorCompra.short_description = 'Total Compra'

class itemDoPedido(models.Model):
    venda = models.ForeignKey(Vendas, on_delete=models.DO_NOTHING)
    produto = models.ForeignKey(Produtos, on_delete=models.DO_NOTHING)
    quantidade = models.FloatField()
