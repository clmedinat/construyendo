from django.urls import path
from .views import UsuariosViews
from .views import EmpresasViews
from .views import EmpleadosViews
from .views import TransaccionesViews
from . import views



urlpatterns=[


  path('usuarios', UsuariosViews.as_view(),name="Listar"),
  path('usuarios/<int:id>', UsuariosViews.as_view(),name="actualizar"),

  path('empresas', EmpresasViews.as_view(), name="Listar"),
  path('empresas/<int:id>',EmpresasViews.as_view(),name="actualizar"),

  path('empleados', EmpleadosViews.as_view(),name="Listar"),
  path('empleados/<int:id>',EmpleadosViews.as_view(),name="Actualizar"),

  path('transacciones', TransaccionesViews.as_view(),name="listar"),

  path('login/',views.loginusuario, name="loginusu" ),


]