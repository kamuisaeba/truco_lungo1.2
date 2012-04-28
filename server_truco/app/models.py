# -*- coding: utf-8 -*-
from django.db import models

# ChangeLog: 28-03-2012 Antonio Castillo Lora
# Reestructuración modelo

# saeba: podriamos poner aquí nombre o id para la marca blanca
class Supermercado(models.Model):
	nombre = models.CharField(max_length=30, verbose_name=u'Nombre Supermercado')
	cp = models.IntegerField(verbose_name = u'Código postal') # codigo postal del supermercado.. Por si hay diferencias entre las diferente tiendas
#	ciudad = models.CharField(max_length=30, verbose_name=u'Ciudad')
#	distintivo = 
#	direccion = 
#	localizacion = models.GeoLocationField..() soñando despierto xD
	def __unicode__(self):
		return unicode(self.nombre)

#saeba: Las categorías se recogen del propio scrapping.. ya veremos como
# Si no, las creamos nosotros que no hay problem tampoco
class Categoria(models.Model):
	nombre = models.CharField(max_length=255)
	def __unicode__(self):
		return unicode(self.nombre)
#saeba: Hay que decidir como obtener las marcas blancas.
#Como las categorías.. las vamos incorporando dese el scrapping
class Marca(models.Model):
	nombre= models.CharField(max_length=255)
	def __unicode__(self):
		return unicode(self.nombre)
class Producto(models.Model):
	nombre = models.CharField(max_length = 255, verbose_name = u'Nombre Producto')
	descripcion = models.TextField(verbose_name = u'Descripcion Producto',blank=True)

#	booleano para saber si son marcas blancas propias de cada supermercado o no.
#	image = models.ImageField() -> cliente mejor?
	def __unicode__(self):
		return unicode(self.nombre)

# saeba: Todo producto tiene:
# -->Super al que pertenece
# -->Categoría a la que pertenece
# -->Marca (aunque sea marca blanca)
# -->Precio unidad
# no me gusta que no existan primary keys multiples, pero bueno
class ProductoSuper(models.Model):
	precio = models.FloatField(verbose_name = u'Precio')
#	cantidad -> no hace falta, es informativo, no nos interesa el stock..
	producto = models.ForeignKey(Producto, verbose_name=u'Producto')
	supermercado = models.ForeignKey(Supermercado, verbose_name=u'Supermercado')
	categoria = models.ForeignKey(Categoria,verbose_name=u'Categoría')
	marca = models.ForeignKey(Marca,verbose_name=u'Marca')
	unique_together= (("producto","supermercado","categoria","marca"),)
	def __unicode__(self):
		return unicode(self.supermercado) + u' vende ' + unicode(self.producto) + u' por ' + unicode(self.precio) + u' euros'

#saeba: Esto se aparca de momento.. el servidor no guarda las listas de los usuarios
class Lista(models.Model):
	nombre = models.CharField(max_length=255)
	nota = models.CharField(max_length=255)

	def __unicode__(self):
		return unicode(self.nombre)
