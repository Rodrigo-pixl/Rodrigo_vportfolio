# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from doctest import master
from idlelib.debugger_r import close_subprocess_debugger
from math import trunc
from tkinter.ttk import Treeview

from appportfolio.views import estudios
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
################################################
# Habilidades
################################################

class Habilidad(models.Model):
    id = models.AutoField(primary_key=True)
    habilidad = models.CharField("Habilidad",max_length=25, null=True, blank=True)
    nivel= models.IntegerField("Nivel",null=True, blank=True) #1-10
    comentario = models.TextField("Comentario",max_length=255,null=True, blank=True)
 # Se crea la tabla comentarion con extension 255.
    class Meta:
        verbose_name = "Habilidad" #puede ser otro nombre
        verbose_name_plural = "Habilidades"
        ordering = ['habilidad']

    def __str__(self):
        return '%s,%s' % (self.habilidad, self.nivel)
 
class Personal (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField("Nombre", max_length=25, null=True, blank=True)
    apellido1= models.CharField("Primer apellido", max_length=25, null=True, blank=True)
    apellido2 = models.CharField("Segundo apellido", max_length=25, null=True, blank=True)
    edad = models.IntegerField("Edad", null= True, blank= True)
    usuario = models.ForeignKey(User,related_name='datos_usuario', null= True, blank=True, on_delete=models.PROTECT())
    class Meta:
        verbose_name = "Personal"
        verbose_name_plural = "Personales"
        ordering = ['nombre']
    def __str__(self) :
        return '%s,%s,%s,%s,%s,%s' % (self.id,self.nombre,self.apellido1,self.apellido2,self.edad,self.usuario)


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField("Puesto de trabajo",max_length=30, null=True, blank=True)

    class Meta:
        verbose_name = 'Categoria' #puede ser otro nombre
        verbose_name_plural = 'Categorias'
        ordering = ['nombre_categoria']

    def __str__(self):
        return "%s,%s" % (self.id,self.nombre_categoria)

class Estudio(models.Model):
        id = models.AutoField(primary_key=True)
        titulacion = models.CharField("Titulacion", max_length=25, null=True, blank=True)
        fechaInicio = models.CharField("Fecha Inicio", max_length=25, null=True, blank=True)
        fechaFin = models.CharField("Fecha Fin", max_length=25, null=True, blank=True)
        notaMedia = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
        lugarEstudio = models.CharField("Lugar de estudio", max_length=25, null=True, blank=True)
        nombreLugar = models.CharField("Nombre del lugar", max_length=25, null=True, blank=True)
        ciudad = models.CharField("Ciudad", max_length=100, null=True, blank=True)
        presencial = models.BooleanField(default=True)
        observaciones = models.TextField( null=True, blank=True)
        estudio = models.ForeignKey(Estudio, related_name='estudio_imagen', null=True, blank=True)

        class Meta:
            verbose_name = "Estudio"
            verbose_name_plural = "Estudios"
            ordering = ['titulacion']

        def __str__(self):
            return '%s,%s,%s,%s' % (self.id, self.titulacion,self.notaMedia,self.estudio)

class Experiencia(models.Model):
    id= models.AutoField(primary_key=True)
    empresa= models.CharField("Empresa", max_length=25, null=True, blank=True)
    fechaInicio= models.CharField("Fecha Inicio", max_length=25, null=True, blank=True)
    fechaFin= models.CharField("Fecha Fin", max_length=25, null=True, blank=True)
    observaciones= models.TextField( null=True, blank=True)
    categoria=models.ForeignKey(Categoria, related_name='expe_categorias' ,on_delete=models.PROTECT)
    class Meta:
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencias"
        ordering = ['empresa']

    def __str__(self):
        return '%s,%s,%s,%s,%s,%s' % (self.id,self.empresa,self.fechaInicio,self.fechaFin,self.observaciones,self.categoria)

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    ap1 = models.CharField(max_length=100)
    ap2 = models.CharField(max_length=100)
    edad = models.IntegerField()

    def __str__(self):
        return  f'{self.nombre} {self.ap1} {self.ap2}'


class Entrevistador (models.Model):
    id= models.AutoField(primary_key= True)
    avatar = models.ImageField('Avatar',blank=True,null=True,upload_to="media/")
    empresa = models.CharField('Empresa', max_length=30, null= True, blank=True)
    fecha_entrevista = models.DateField('Fecha Entrevista', null=True,blank=True)
    conectado = models.BooleanField('Conectado', null=True, blank=True)
    seleccionado = models.BooleanField('Seleccionado', null=True, blank=True)
    # forteings key requerido desde django 2.0
    user = models.ForeignKey(User, related_name='entrevistados_usuario',
                             null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Entrevistador'
        verbose_name_plural = 'Entrevistadores'
        ordering = ['empresa']

    def __str__(self):
        return "%s,%s,%s,%s,%s,%s" % (self.id, self.empresa,self.fecha_entrevista,self.conectado,
                                      self.seleccionado,self.user)

class Imagen(models.Model):
    id= models.AutoField(primary_key=True)
    imagen = models.ImageField("Imagen", blank=True, null=True, upload_to="imagenes/")
    comentario = models.CharField('Comentario', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural= 'Imagenes'
        ordering = ['id']
    def __str__(self):
        return "%s,%s,%s" % (self.id, self.imagen, self.comentario)

    #####################################
    #videos
    #####################################
class Video (models.Model):
    id = models.AutoField(primary_key=True)
    video = models.FileField("Video", blank=True, null=True, upload_to="videos/")
    comentario = models.CharField('Comentario',max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
        ordering = ['id']
    def __str__(self):
        return "%s,%s,%s" % (self.id, self.video, self.comentario)

class Curriculum (models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField("Nombre", max_length=25, null=True, blank=True)
    apellido1 = models.CharField("Primer apellido", max_length=25, null=True, blank=True)
    apellido2 = models.CharField("Segundo apellido", max_length=25, null=True, blank=True)
    email = models.CharField("Email", max_length=30, null= True, blank=True)
    telefono = models.CharField("Telefono", max_length=9 , null=True, blank=True)

    class Meta:
        verbose_name = "Curriculum"
        verbose_name_plural = "Curriculums"
        ordering = ['nombre']

    def __str__(self):
        return '%s,%s,%s,%s' % (self.id, self.nombre, self.apellido1, self.apellido2)

class DeatteCurriculumEstudio(models.Model):
    id = models.AutoField(primary_key=True)
    Estudio = models.ForeignKey(Estudio, on_delete=models.CASCADE, verbose_name="Estudio")
    Curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE, verbose_name="Curriculum")

    class Meta:
        verbose_name = "Detalle de Curriculum y Estudio"
        verbose_name_plural = "Detalles de Curriculums y Estudios"

    def __str__(self):
        return  '%s,%s,%s' % (self.id, self.Curriculum, self.Estudio)


class DeatteCurriculumExperiencia(models.Model):
    id = models.AutoField(primary_key=True)
    Experiencia = models.ForeignKey(Estudio, on_delete=models.CASCADE, verbose_name="Estudio")
    Curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE, verbose_name="Curriculum")

    class Meta:
        verbose_name = "Detalle de Curriculum y Experiencia"
        verbose_name_plural = "Detalles de Curriculums y Experiencias"

    def __str__(self):
        return  '%s,%s,%s' % (self.id, self.Curriculum, self.Experiencia)

class DetalleCurriculumEstudio(models.Model):
    id = models.AutoField(primary_key=True)
    Estudio = models.ForeignKey(Estudio,on_delete=models.CASCADE, verbose_name="Estudio")
    Curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE, verbose_name="Curriculum")

    class Meta:
        verbose_name = "Detalle de Curriculum y Estudio"
        verbose_name_plural = "Detalles de Curriculums y Estudios"

    def __str__(self):
        return '%s, Estudio: %s, Curriculum: %s' % (self.id, self,estudios,self.Curriculum)

class Estudio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Curroculum(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ap1 = models.CharField(max_length=100)
    ap2 = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.ap1} {self.ap2}"

class DetalleCurriculumExperiencia(models.Model):
    id = models.AutoField(primary_key=True)
    experiencia = models.ForeignKey(Experiencia, on_delete=models.CASCADE)
    Curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.experiencia.empresa} para {self.curriculum.nombre}"

class DetalleCurriculumEstudio(models.Model):
    id = models.AutoField(primary_key=True)
    estudio = models.ForeignKey(Estudio, on_delete=models.CASCADE)
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.estudio.nombre} para {self.curriculum.nombre}"


class Noticia (models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField("Titulo", max_length=200, null=True, blank=True)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField('Imagen', blank=True, null=True, upload_to="media/")

    def __str__(self):
        return self.titulo