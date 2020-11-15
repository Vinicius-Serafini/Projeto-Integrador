"""ajudaAi URL Configuration

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
from django.urls import path, include
from . import views

app_name ="main"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("cadastrar/", views.cadastrar, name="cadastrar"),
    path("nova_publicacao/", views.nova_publicacao, name="nova_publicacao"),
    path("publicacao_detalhes/<int:id>", views.publicacao_detalhes, name="publicacao_detalhes"),
]
