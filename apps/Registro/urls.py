from django.urls import path, include
from . import views

#API
from rest_framework.urlpatterns import format_suffix_patterns
from apps.Registro import views


urlpatterns = [
    #Nuevo Form 
    path('agregar_actor', views.agregar_actor.as_view(), name="agregar_actor"),
    path('listarActores', views.listar_actores.as_view(), name="listar_actores"),
    path('editar_actor/<int:pk>', views.editar_actor.as_view() ,name="editar_actor"),
    path('borrar_actor/<int:pk>', views.borrar_actor.as_view(), name="borrar_actor"),

    #API
    # path('api/', views.API_objects.as_view()),
    # path('api/<int:pk>/', views.API_objects_details.as_view()),

    #API2
    path('actores/',  views.actor_collection , name='actor_collection'),
    path('actores/<int:pk>/', views.actor_element ,name='actor_element'),

    path('noticias/',views.noticias,name='noticias'),
    path('top2020/',views.top2020,name='top2020'),



]

urlpatterns = format_suffix_patterns(urlpatterns)
