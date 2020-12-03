from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import RegistroForm
from django.urls import path, include
from django.shortcuts import render


# Create your views here.
def Menu(request):
    return render(request, "home.html", {})

class RegistroUsuario(CreateView):
    model = User
    template_name = "Usuario/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('menu')

class UserList(ListView):
    model = User
    template_name = 'Usuario/list_user.html'

class editar_user(UpdateView):
    model = User
    form_class = RegistroForm
    template_name = 'Usuario/registrar.html'
    success_url = reverse_lazy('list_user')

class borrar_user(DeleteView):
    model = User
    template_name = 'Usuario/borrar_user.html'
    success_url = reverse_lazy('list_user')
