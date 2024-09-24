from django.shortcuts import render, get_object_or_404
from multiprocessing import context
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *


# Create your views here.
def home(request):
    return HttpResponse('Hello World')

def navbar(request):
    return render(request, "menu.html")

# CREATE

class CreateCafeteria(CreateView):
    template_name="cafeterias/cafeteria_create.html"
    model = Cafeteria
    fields=["nome_cafeteria", "local"]
    success_url = reverse_lazy("read_cafeterias")

class CreateCliente(CreateView):
    template_name="cliente/cliente_create.html"
    model = Cliente
    fields=["nome_cliente", "cpf", "telefone"]
    success_url = reverse_lazy("read_clientes")

class CreateEmpregado(CreateView):
    template_name="empregados/empregados_create.html"
    model = Empregado
    fields=["nome_empregado", "cpf", "telefone", "salario", "id_cafeteria"]
    success_url = reverse_lazy("read_empregados")

class CreateProduto(CreateView):
    template_name="produtos/produtos_create.html"
    model = Produto
    fields=["nome_produto", "preco"]
    success_url = reverse_lazy("read_produtos")

class CreateProdutoCafeteria(CreateView):
    template_name="cafeterias/produto_cafeteria/produto_cafeteria_create.html"
    model = Produto_Cafeteria
    fields=["id_produto","quantidade"]
    success_url = reverse_lazy("read_produtos")

    def get_queryset(self):
        self.id_cafeteria = get_object_or_404(Cafeteria, pk=self.kwargs['id_cafeteria'])
        return Produto_Cafeteria.objects.filter(id_cafeteria_id=self.id_cafeteria)
    
class CreateCompra(CreateView):
    template_name="compras/compra_create.html"
    model = Compra
    fields=["datahora_compra", "id_cliente", "id_empregado", "id_cafeteria_empregado", "id_produto"]
    success_url = reverse_lazy("read_compras")

'''def create_compra_produto(request):
    new_id_produto = request.POST[""]
    new_id_compra = request.POST[""]
    new_quantidade = request.POST[""]
    compra_produto = Compra_Produto(id_produto = new_id_produto, id_compra = new_id_compra, quantidade = new_quantidade)
    compra_produto.save()'''

'''def create_compra(request):
    new_datahora_compra = request.POST[""]
    new_id_cliente = request.POST[""]
    new_id_empregado = request.POST[""]
    new_id_cafeteria = request.POST[""]
    new_id_produto = request.POST[""]
    compra = Compra(datahora_compra = new_datahora_compra, id_cliente = new_id_cliente, id_empregado = new_id_empregado, 
                    id_cafeteria = new_id_cafeteria, id_produto = new_id_produto)
    compra.save()'''

#UPDATE

class UpdateCliente(UpdateView):
    template_name="cliente/cliente_update.html"
    model = Cliente
    fields=["nome_cliente", "cpf", "telefone"]
    success_url = reverse_lazy("read_clientes")

class UpdateEmpregado(UpdateView):
    template_name="empregados/empregados_update.html"
    model = Empregado
    fields=["nome_empregado", "cpf", "telefone", "salario", "id_cafeteria"]
    success_url = reverse_lazy("read_empregados")

class UpdateCafeteria(UpdateView):
    template_name="cafeterias/cafeteria_update.html"
    model = Cafeteria
    fields=["nome_cafeteria", "local"]
    success_url = reverse_lazy("read_cafeterias")

class UpdateProduto(UpdateView):
    template_name="produtos/produtos_update.html"
    model = Produto
    fields=["nome_produto", "preco"]
    success_url = reverse_lazy("read_produtos")

class UpdateProdutoCafeteria(UpdateView):
    template_name="cafeterias/produto_cafeteria/produto_cafeteria_update.html"
    model = Produto_Cafeteria
    fields=["quantidade"]
    success_url = reverse_lazy("read_produtos_cafeteria")

#READ

class ReadCafeterias(ListView):
    template_name = "cafeterias/cafeteria_list.html"
    model = Cafeteria
    context_object_name="cafeterias_list"

class ReadClientes(ListView):
    template_name = "cliente/clientes_list.html"
    model = Cliente
    context_object_name="clientes_list"

class ReadEmpregados(ListView):
    template_name = "empregados/empregados_list.html"
    model = Empregado
    context_object_name="empregados_list"

class ReadProdutos(ListView):
    template_name = "produtos/produtos_list.html"
    model = Produto
    context_object_name="produtos_list"

class ReadCompras(ListView):
    template_name = "compras/compras_list.html"
    model = Compra
    context_object_name="compras_list"

def read_compra_produto(request):
    pass

class ReadProdutosCafeteria(ListView):
    template_name = "cafeterias/produto_cafeteria/produto_cafeteria_list.html"
    model = Produto_Cafeteria
    context_object_name="produtos_cafeteria_list"

    def get_queryset(self):
        saved_id_cafeteria = get_object_or_404(Cafeteria, pk=self.kwargs['id_cafeteria'])
        return Produto_Cafeteria.objects.filter(id_cafeteria_id=saved_id_cafeteria)


def read_compra(request):
    return render(request, "compras/readView.html")

#DELETE

class DeleteCliente(DeleteView):
    template_name = "cliente/cliente_delete.html"
    model = Cliente
    success_url = reverse_lazy("read_clientes")
    

class DeleteEmpregado(DeleteView):
    template_name = "empregados/empregados_delete.html"
    model = Empregado
    success_url = reverse_lazy("read_empregados")

class DeleteCafeteria(DeleteView):
    template_name = "cafeterias/cafeteria_delete.html"
    model = Cafeteria
    success_url = reverse_lazy("read_cafeterias")

class DeleteProduto(DeleteView):
    template_name = "produtos/produtos_delete.html"
    model = Produto
    success_url = reverse_lazy("read_produtos")

def delete_compra_produto(request, id):
    pass

class DeleteProdutoCafeteria(DeleteView):
    template_name = "cafeterias/produto_cafeteria/produto_cafeteria_delete.html"
    model = Produto_Cafeteria
    success_url = reverse_lazy("read_produtos_cafeteria")

def delete_compra(request, id):
    pass

