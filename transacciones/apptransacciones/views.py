import email
import json
from traceback import print_tb
from django.shortcuts import render
from django.views import View
from .models import Usuarios, Empresas, Empleados, Transacciones
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

def loginusuario(request):
      if request.method=='POST':
         try:
            detalleusuarios=Usuarios.objects.get(usuario=request.POST['username'], password=request.POST['password'])
            #detalleusuario=Cliente.objects.get(documento=['documento'], correo=['correo'])
         #   cli=list(Cliente.objects.get(documento=detalleusuario.documento))
            cli=list(Cliente.objects.filter(documento=200).values())
            print(detalleusuario.documento)
           
            datos={"listadoclientes":cli}
            print(datos)
            aaaa=request.POST['username']
            print("datosssssssssssss", aaaa)
            if detalleusuario.rol=="admin":
               print("wwww", request.session['username'])
               request.session['username']=detalleusuario.nomusuario
               request.session['documento']=detalleusuario.documento
               return render(request, 'gestionc.html')
            elif detalleusuario.rol=="empleado":
               request.session['username']=detalleusuario.nomusuario
               return render(request, 'empleados.html')
            elif detalleusuario.rol=="cliente":
               request.session['username']=detalleusuario.nomusuario
               return render(request, 'clientes.html')   
         except Usuario.DoesNotExist as e:
            message.success(request,"No existe")
      return render(request,"login.html")


class UsuariosViews(View):
  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
      return super().dispatch(request, *args, **kwargs)

  def __get_auth(self, request):
    try:
      username=request.headers.get("Username")
      password=request.headers.get("Password")
      user=Usuarios.objects.filter(usuario=username, password=password).values()

      if len(user) > 0:
        return True
      return False
    except Exception as e:
      print(e)
      return False

  def get(self, request, id=""):
    try:
      if self.__get_auth(request):
        if id != "":
          usuario=Usuarios.objects.get(id=id)
          if usuario:
            response={"data": [model_to_dict(usuario)]}
          else:
            response={"message": "El usuario no existe"}
        else:
          usuario=Usuarios.objects.values()
          response={"data": list(usuario)}
      else:
        response={"message": "Usuario o contraseña incorrecta"}
    except Exception as e:
      print(e)
      response={"message": "Excepción"}
    return JsonResponse(response)

  def post(self, request):
    try:
      if self.__get_auth(request):
        data = json.loads(request.body)
        Usuarios.objects.create(
          email=data["email"],
          imagen=data["imagen"],
          usuario=data["usuario"],
          password=data["password"],
          roles=data["roles"]
        )
        response={"message": "Usuario creada"}
      else:
        response={"message": "Usuario o contraseña incorrecta"}
    except Exception as e:
      print(e)
      response={"message": "Excepción"}
    return JsonResponse(response)

  def delete(self,request,id):
    try:
      if self.__get_auth(request):
          usuario=Usuarios.objects.get(id=id)
          if usuario:
            usuario.delete()
            response={"message": "Usuario eliminado"}
          else:
            response={"message": "El usuario no existe"}
      else:
        response={"message": "Usuario o contraseña incorrecta"}
    except Exception as e:
      print(e)
      response={"message": "Excepción"}
    return JsonResponse(response)

class EmpresasViews(View):
  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)

  def __get_auth(self, request):
    try:
      username=request.headers.get("Username")
      password=request.headers.get("Password")
      user=Usuarios.objects.filter(usuario=username, password=password).values()

      if len(user) > 0:
        return True
      return False
    except Exception as e:
      print(e)
      return False

  def get(self, request, id=""):
    try:
      if self.__get_auth(request):
        if id != "":
          empresa=Empresas.objects.get(id=id)
          if empresa:
            response={"data": [model_to_dict(empresa)]}
          else:
            response={"message": "La empresa no existe"}
        else:
          empresas=Empresas.objects.values()
          response={"data": list(empresas)}
      else:
        response={"message": "Usuario o contraseña incorrecta"}
    except Exception as e:
      print(e)
      response={"message": "Excepción"}
    return JsonResponse(response)

  def post(self, request):
    try:
      if self.__get_auth(request):
        data = json.loads(request.body)
        Empresas.objects.create(
          nombre=data["nombre"],
          nit=data["nit"],
          ciudad=data["ciudad"],
          direccion=data["direccion"],
          telefono=data["telefono"],
          sector=data["sector"]
        )
        response={"message": "Empresa creada"}
      else:
        response={"message": "Usuario o contraseña incorrecta"}
    except Exception as e:
      print(e)
      response={"message": "Excepción"}
    return JsonResponse(response)

  def delete(self,request,id):
    try:
      if self.__get_auth(request):
          empresa=Empresas.objects.get(id=id)
          if empresa:
            empresa.delete()
            response={"message": "Empresa eliminada"}
          else:
            response={"message": "La empresa no existe"}
      else:
        response={"message": "Usuario o contraseña incorrecta"}
    except Exception as e:
      print(e)
      response={"message": "Excepción"}
    return JsonResponse(response)

  def put(self,request,id):
    try:
      if self.__get_auth(request):
          empresa=Empresas.objects.get(id=id)
          if empresa:
            data=json.loads(request.body)
            empresa.nombre=data["nombre"]
            empresa.nit=data["nit"]
            empresa.ciudad=data["ciudad"]
            empresa.direccion=data["direccion"]
            empresa.telefono=data["telefono"]
            empresa.sector=data["sector"]
            empresa.save()
            response={"message": "Empresa actualizada"}
          else:
            response={"message": "La empresa no existe"}
      else:
        response={"message": "Usuario o contraseña incorrecta"}
    except Exception as e:
      print(e)
      response={"message": "Excepción"}
    return JsonResponse(response)

class EmpleadosViews(View):
  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)

  def __get_auth(self, request):
    try:
      username=request.headers.get("Username")
      password=request.headers.get("Password")
      user=Usuarios.objects.filter(usuario=username, password=password).values()

      if len(user) > 0:
        return True
      return False
    except Exception as e:
      print(e)
      return False

  def get(self, request, id=""):
    try:
      if self.__get_auth(request):
        if id != "":
          empleado=Empleados.objects.get(id=id)
          if empleado:
            response={"data": [model_to_dict(empleado)]}
          else:
            response={"message": "Empleado no existe"}
        else:
          empleado=Empleados.objects.values()
          response={"data": list(empleado)}
      else:
        response={"message": "Usuario o contraseña incorrecta"}
    except Exception as e:
      print(e)
      response={"message": "Excepción"}
    return JsonResponse(response)

  def post(self, request):
    try:
      if self.__get_auth(request):
        data = json.loads(request.body)
        Empleados.objects.create(
          nombre=data["nombre"],
          apellido=data["apellido"],
          email=data["email"],
          telefono=data["telefono"],
          empresa=data["empresa"]
        )
        response={"message": "Empleado creado"}
      else:
        response={"message": "Usuario o contraseña incorrecta"}
    except Exception as e:
      print(e)
      response={"message": "Excepción"}
    return JsonResponse(response)

  def delete(self,request,id):
    try:
      if self.__get_auth(request):
          empleado=Empleados.objects.get(id=id)
          if empleado:
            empleado.delete()
            response={"message": "Empleado eliminado"}
          else:
            response={"message": "El empleado no existe"}
      else:
        response={"message": "Usuario o contraseña incorrecta"}
    except Exception as e:
      print(e)
      response={"message": "Excepción"}
    return JsonResponse(response)

class TransaccionesViews(View):
  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)

  def __get_auth(self, request):
    try:
      username=request.headers.get("Username")
      password=request.headers.get("Password")
      user=Usuarios.objects.filter(usuario=username, password=password).values()

      if len(user) > 0:
        return True
      return False
    except Exception as e:
      print(e)
      return False

  def get(self, request, id=""):
    try:
      if self.__get_auth(request):
        if id != "":
          transacion=Transacciones.objects.get(id=id)
          if transacion:
            response={"data": [model_to_dict(transacion)]}
          else:
            response={"message": "La empresa no existe"}
        else:
          transacion=Transacciones.objects.values()
          response={"data": list(transacion)}
      else:
        response={"message": "Usuario o contraseña incorrecta"}
    except Exception as e:
      print(e)
      response={"message": "Excepción"}
    return JsonResponse(response)

  def post(self, request):
    try:
      if self.__get_auth(request):
        data = json.loads(request.body)
        Transacciones.objects.create(
          concepto=data["concepto"],
          monto=data["monto"],
          tipo=data["tipo"],
          usuario=data["usuario"],
          empresa=data["empresa"]
        )
        response={"message": "Transaccion creada"}
      else:
        response={"message": "Usuario o contraseña incorrecta"}
    except Exception as e:
      print(e)
      response={"message": "Excepción"}
    return JsonResponse(response)

  def delete(self,request,id):
    try:
      if self.__get_auth(request):
          trasancion=Transacciones.objects.get(id=id)
          if trasancion:
            trasancion.delete()
            response={"message": "Transación eliminada"}
          else:
            response={"message": "La Transación no existe"}
      else:
        response={"message": "Usuario o contraseña incorrecta"}
    except Exception as e:
      print(e)
      response={"message": "Excepción"}
    return JsonResponse(response)

    