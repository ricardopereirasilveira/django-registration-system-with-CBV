from django.urls import path
from . import views


urlpatterns = [
    path('deletarFuncionario/<int:id>', views.deletarFuncionario, name='delFunc'),
    path('adicionarFuncionario/', views.adicionarFuncionario, name='addFunc'),
    path('listarFuncionario/', views.listarFuncionario, name='listFunc'),
    path('editarFuncionario/<int:id>', views.editarFuncionario, name='editFunc'),
]