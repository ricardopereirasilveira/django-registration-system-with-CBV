from django.contrib import admin
from .models import Funcionario, DocumentoRG, DocumentoCPF, Vendas, Produtos, itemDoPedido

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


class itemDoPedidoInLine(admin.TabularInline):
    model = itemDoPedido
    extra = 1


class vendasAdmin(admin.ModelAdmin):
    inlines = [itemDoPedidoInLine]
    exclude = ['valor']
    search_fields = ['id', 'numero']
    readonly_fields = ['valorCompra', 'aPagar']
    raw_id_fields = ['person']
    list_display = ('id',
        'numero', 'nomeCompleto', 'valorCompra', 'desconto',
        'imposto', 'aPagar'
    )
    list_filter = ('numero', 'produtos__produto')


class produtosAdmin(admin.ModelAdmin):
    list_display = ('id', 'produto', 'preco')


admin.site.register(DocumentoCPF)
admin.site.register(itemDoPedido)
admin.site.register(DocumentoRG)
admin.site.register(Funcionario, funcionarioAdmin)
admin.site.register(Vendas, vendasAdmin)
admin.site.register(Produtos, produtosAdmin)
