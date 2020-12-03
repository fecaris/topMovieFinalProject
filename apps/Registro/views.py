from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import Actor,Pelicula
from .forms import ActorForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

#api2
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ApiSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 




# # las importaciones para la API 
# from rest_framework import generics
# from .serializers import ApiSerializer


class agregar_actor(CreateView):
    model = Actor
    form_class = ActorForm
    template_name = 'Registro/agregar_actor.html'
    success_url = reverse_lazy("listar_actores")

class listar_actores(ListView):
    model = Actor
    template_name = 'Registro/listar_actores.html'

class editar_actor(UpdateView):
    model = Actor
    form_class = ActorForm
    template_name = 'Registro/agregar_actor.html'
    success_url = reverse_lazy('listar_actores')

class borrar_actor(DeleteView):
    model = Actor
    template_name = 'Registro/borrar_actor.html'
    success_url = reverse_lazy('listar_actores')


# API 
# class API_objects(generics.ListCreateAPIView):
#     queryset = Actor.objects.all()
#     serializer_class = ApiSerializer
    
# class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Actor.objects.all()
#     serializer_class = ApiSerializer


#API2
@api_view(['GET','POST'])
def actor_collection(request):
    if request.method == 'GET':
        actor = Actor.objects.all()
        serializer = ApiSerializer(actor, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def actor_element(request, pk):
    actor = get_object_or_404(Actor, id=pk)

    if request.method == 'GET':
        serializer = ApiSerializer(actor)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT': 
        actor_new = JSONParser().parse(request) 
        serializer = ApiSerializer(actor, data=actor_new) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#paginas antiguas
def noticias(request):
    return render(request, "Paginas/noticias.html", {})

def top2020(request):
    return render(request, "Paginas/top2020.html", {})











