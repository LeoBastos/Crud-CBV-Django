from django.shortcuts import render
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Cliente
from .forms import ClienteModelForm
from django.urls import reverse_lazy



class IndexView(ListView):
    models = Cliente
    template_name = 'clientes/index.html'
    queryset = Cliente.objects.all()
    context_object_name = 'clientes'

class ClienteDetailView(DetailView):    
    model = Cliente
    template_name = 'clientes/detail_cliente.html'
    

class CreateClienteView(CreateView):
    model = Cliente
    template_name = 'clientes/cliente_form.html'
    fields = ['nome', 'email', ]
    success_url = reverse_lazy('clientes/index')


class UpdateClienteView(UpdateView):
    model = Cliente
    template_name = 'clientes/cliente_form.html'
    fields = ['nome' , 'email',]
    success_url = reverse_lazy('clientes/index')


class DeleteClienteView(DeleteView):
    model = Cliente
    template_name = 'clientes/cliente_del.html'
    success_url = reverse_lazy('clientes/index')



