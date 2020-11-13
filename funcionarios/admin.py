from django.contrib import admin
from .models import Funcionario, DocumentoRG, DocumentoCPF

class funcionarioAdmin(admin.ModelAdmin):
    # fields = (
    #     ('primeiroNome', 'ultimoNome'), 'idade', ('email', 'dataNascimento'), 'profile',
    #     'acessarSistema', ('rg', 'cpf')
    # )
    list_display = (
        'primeiroNome', 'ultimoNome', 'idade', 'email', 'dataNascimento', 'hasPicture', 'acessarSistema',
        'rg', 'cpf'
    )
    fieldsets = (
        ('Dados Pessoais', {
            'fields': ('primeiroNome', 'ultimoNome', 'idade', 'email', 'dataNascimento')
        }),
        ('Dados Complementares', {
            'classes': ('collapse', 'open'),
            'fields': ('profile', 'acessarSistema', 'rg', 'cpf')
        })
    )
    list_filter = ('acessarSistema', 'idade')




admin.site.register(DocumentoCPF)
admin.site.register(DocumentoRG)
admin.site.register(Funcionario, funcionarioAdmin)
