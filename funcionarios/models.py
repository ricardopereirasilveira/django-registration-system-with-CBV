from django.db import models


class Funcionario(models.Model):
    primeiroNome = models.CharField(max_length=30)
    ultimoNome = models.CharField(max_length=30)
    idade = models.IntegerField()
    email = models.EmailField()
    profile = models.ImageField(blank=True, null=True, upload_to='func_pictures')
    dataNascimento = models.DateField()
    acessarSistema = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} - {self.primeiroNome} {self.ultimoNome} '
