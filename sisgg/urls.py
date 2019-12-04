"""sisgg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.views.generic import TemplateView
from core.views import Entrar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Entrar.as_view(),name='entrar'),
    #path('',  TemplateView.as_view(template_name='core/index.html')),
    path('core/',include('core.urls',namespace='core')),
    path('fornecedor/',include('fornecedor.urls',namespace='fornecedor')),
    path('produto/',include('produto.urls',namespace='produto')),
]
