from django.urls import path, include
from . import views
from .views import RegistroUsuario, UserList

urlpatterns = [
    path('menu',views.Menu, name=("menu")),
    path('registrar', RegistroUsuario.as_view(), name="registrar"),
    path('listar', UserList.as_view(), name="list_user"),
    path('editar_user/<int:pk>', views.editar_user.as_view() ,name="editar_user"),
    path('borrar_user/<int:pk>', views.borrar_user.as_view(), name="borrar_user"),
    
]
