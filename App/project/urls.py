"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from app.views import *

urlpatterns = [
    #GENERAL URLS
    path('admin/', admin.site.urls),
    path('', home),
    path('menu.html', navbar),

    
    #CREATE URLS
    path('cafeterias/cadastroCafeteria', CreateCafeteria.as_view(), name="cafeteria_create"),
    path('clientes/cadastroCliente', CreateCliente.as_view(), name="cliente_create"),
    path('empregados/cadastroEmpregado', CreateEmpregado.as_view(), name="empregado_create"),
    path('produtos/cadastroProduto', CreateProduto.as_view(), name="produto_create"),
    path('compras/realizarCompra', CreateCompra.as_view(), name="compra_create"),
    path('cafeterias/<int:id_cafeteria>/produtos_cafeteria/cadastroProduto', CreateProdutoCafeteria.as_view(), name="produto_cafeteria_create"),
    

    #READ URLS
    path('cafeterias', ReadCafeterias.as_view(), name="read_cafeterias"),
    path('clientes', ReadClientes.as_view(), name="read_clientes"),
    path('empregados', ReadEmpregados.as_view(), name="read_empregados"),
    path('produtos', ReadProdutos.as_view(), name="read_produtos"),
    path('compras', ReadCompras.as_view(), name="read_compras"),
    path('cafeterias/<int:id_cafeteria>/produtos_cafeteria', ReadProdutosCafeteria.as_view(), name="read_produtos_cafeteria"),
    


    #UPDATE URLS
    path('cafeteria/<int:pk>', UpdateCafeteria.as_view(), name="update_cafeteria"),
    path('cliente/<int:pk>', UpdateCliente.as_view(), name="update_cliente"),
    path('empregado/<int:pk>', UpdateEmpregado.as_view(), name="update_empregado"),
    path('produto/<int:pk>', UpdateProduto.as_view(), name="update_produto"),
    path('cafeterias/<int:pk>', UpdateProdutoCafeteria.as_view(), name="update_produto_cafeteria"),
    

    #DELETE URLS
    path('cafeteria/delete/<int:pk>', DeleteCafeteria.as_view(), name="delete_cafeteria"),
    path('cliente/delete/<int:pk>', DeleteCliente.as_view(), name="delete_cliente"),
    path('empregado/delete/<int:pk>', DeleteEmpregado.as_view(), name="delete_empregado"),
    path('produto/delete/<int:pk>', DeleteProduto.as_view(), name="delete_produto"),
    path('cafeterias/<int:pk>', DeleteProdutoCafeteria.as_view(), name="delete_produto_cafeteria"),
]
