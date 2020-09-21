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

    def __str__(self):
        return f'{self.id} - {self.primeiroNome} {self.ultimoNome} '


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
    produtos = models.ManyToManyField(Produtos, blank=True, null=True, default='NULL')

    def __str__(self):
        return f'{self.numero} - {self.valor} {self.person}'