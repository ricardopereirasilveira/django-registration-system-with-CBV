from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views



urlpatterns = [
    # path('listarFuncionario/', views.listarFuncionario, name='listFunc'),
    path('listarFuncionarios/', login_required(views.listarFuncionarios.as_view()), name='listFunc'),
    path('deletarFuncionario/<int:id>', views.deletarFuncionario, name='delFunc'),
    path('adicionarFuncionario/', views.adicionarFuncionario, name='addFunc'),
    path('editarFuncionario/<int:id>', views.editarFuncionario, name='editFunc'),
]