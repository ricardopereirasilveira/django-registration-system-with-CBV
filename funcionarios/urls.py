from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views



urlpatterns = [
    path('listarFuncionarios/', login_required(views.listarFuncionarios.as_view()), name='listFunc'),
    path('deletarFuncionario/<int:pk>', login_required(views.deletarFuncionario.as_view()), name='delFunc'),
    path('adicionarFuncionario/', login_required(views.adicionarFuncionario.as_view()), name='addFunc'),
    path('editarFuncionario/<int:pk>', login_required(views.editarFuncionario.as_view()), name='editFunc'),
]