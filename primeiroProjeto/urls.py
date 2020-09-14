"""primeiroProjeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import helloNome, rastrearEncomenda, contaAdicao, contaSubtracao, horario24Horas
from funcionarios import urls as funcURL
from home import urls as homeURL


urlpatterns = [
    path('', include(homeURL)),
    path('funcionarios/', include(funcURL)),
    path('conta/soma/<int:valor1>/<int:valor2>', contaAdicao),
    path('conta/subtracao/<int:valor1>/<int:valor2>', contaSubtracao),
    path('correios/<str:codigo>/', rastrearEncomenda),
    path('hello/<str:nome>/', helloNome),
    path('horario-24-horas/<str:horario>/', horario24Horas, name='Horario24Horas'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
