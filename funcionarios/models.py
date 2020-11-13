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