from django.contrib import admin
from .models import Funcionario, DocumentoRG, DocumentoCPF, Vendas, Produtos


admin.site.register(DocumentoCPF)
admin.site.register(DocumentoRG)
admin.site.register(Funcionario)
admin.site.register(Vendas)
admin.site.register(Produtos)
