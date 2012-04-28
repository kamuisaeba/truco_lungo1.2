from models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.template.loader import get_template
from django.core import serializers
# Devolvemos todas las categorias de un producto dado
#en la request le decimos el nombre del producto
# Return lista de categorias
def cargar_categorias(request,nombre):
  #espero no estar haciendo una burrada
  #Traduccion: dame las categorias cuyo nombre de producto comience con "nombre"
  categorias =ProductoSuper.objects.filter(producto__nombre__startswith = nombre);
  return json_serializer.serialize(categorias, ensure_ascii=False, stream=response)
def cargar_productos(request):
	return None

#Esto de momento no sirve.. las listas se cargan	
def cargar_listas(request):
  listas = Lista.objects.all()
  t = get_template('app/listas.html')
  c = RequestContext(request, {"listas":listas})
  return HttpResponse(t.render(c))
  
