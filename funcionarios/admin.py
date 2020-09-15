from django.contrib import admin
from .models import Funcionario, DocumentoRG, DocumentoCPF


admin.site.register(DocumentoCPF)
admin.site.register(DocumentoRG)
admin.site.register(Funcionario)
