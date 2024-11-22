# -*- coding: utf-8 -*-
from dataclasses import field

from django.contrib import admin
from appportfolio.models import *
from django.contrib.auth.models import User
from __future__ import unicode_literals

from .models import DetalleCurriculumEstudio,DetalleCurriculumExperiencia,Curriculum

admin.site.site_header = "Sitio web Salmantino"  #este es el título
admin.site.site_title = "Portal de Saludos"
admin.site.index_title = "Bienvenidos al portal de Administración"
admin.site.register(Curriculum)
admin.site.register(Estudio)
admin.site.register(DetalleCurriculumEstudio)
admin.site.register(DetalleCurriculumExperiencia)


class HabilidadAdmin(admin.ModelAdmin):
    list_display = [co.name for co in Habilidad._meta.get_fields()]
    search_fields = ('id','habilidad') #siempre tienen que ser una tupla
    list_filter   = ('id','habilidad') #siempre tienen que ser una tupla
admin.site.register(Habilidad, HabilidadAdmin)

class PersonalAdmin(admin.ModelAdmin):
    list_display = [co.name for co in Personal._meta.get_fields()]
    search_fields = ('id','nombre', 'apellido1', 'apellido2') #siempre tienen que ser una tupla
    list_filter   = ('id','nombre') #siempre tienen que ser una tupla
admin.site.register(Personal, PersonalAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    #list_display = [c.name for c in categoria._meta.get_fields()]
    list_display = ['id','nombre_categoria']
    search_fields = ('id','nombre_cateforia')
    list_filter = ('id', 'nombre_categoria')
admin.site.register(Categoria, CategoriaAdmin)

#class ExperienciaAdmin(admin.ModelAdmin):
    #list_display = [c.name for c in Experiencia._meta.get_fields]
    #list_display = ['id','empresa']
    #search_fields = ('id', 'empresa')
    #ist_filter = ('id', 'empreasa')
#admin.site.registe(Experiencia, ExperoenciaAdmin)

class EstudioAdmin(admin.ModelAdmin):
    list_display = [co.name for co in Estudio._meta.get_fields()]
    search_fields = ('id', 'titulacion','fechaIncion', 'fechaFin','notaMedia','lugarEstudio','nombreLugar', 'ciudad','precencial','obsevaciones')
    list_filter = ('id','titulacion','ciudad')
admin.site.register(Estudio, EstudioAdmin)

class EntrevistadorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Entrevistador._meta.get_fields()if hasattr(field,'verbose_name')]
    search_fields = ('id', 'empresa')
    admin.site.register(Entrevistador, EntrevistadorAdmin)

class ImagenAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Imagen._meta.get_fields() if hasattr(field, 'verbose_name')]
    search_fields = ('id', 'imagen')
admin.site.register(Imagen, ImagenAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Video._meta.get_fields() if hasattr(field, 'verbose_name')]
    search_fields = ('id', 'video')
admin.register(Video, VideoAdmin)

class DetalleCurriculumEstudioAdmin(admin.ModelAdmin):
    list_display = ('id', 'estudio', 'curriculum')
    search_fields = ('id','estudio_titulacio', 'curriculum_nombre')
    list_filter = ('estudio', 'curriculum')
    ordering = ('id',)

class DeatteCurriculumExperienciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'Experiencia', 'Curriculum')
    search_fields = ('id', 'Experiencia__titulacion', 'Curriculum__nombre')
    list_filter = ('Experiencia', 'Curriculum')
    ordering = ('id',)

#class CurriculumAdmin(admin.ModelAdmin):
#    list_display = ('id', 'nombre', 'apellido', 'apellido2', 'email', 'email', ('telefono')

class NoticiaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Noticia._meta.get_fields() if hasattr(field, 'verbose_name')]
    search_fields = ('id', 'titulo')
    admin.site.register(Noticia, NoticiaAdmin)

#VALORACIONES

@admin.register(Valoracion)
class ValoracionAdmin(admin.ModelAdmin):
    list_display = ('id', 'votos_empresa', 'media_aspectos', 'timestamp')
    readonly_fields = ('media_aspectos',)
    def save_model(self,request,obj,form,change):
        # Calcula automaticamente la media
        if obj.votos_entrevista and obj.votos_empresa:
            obj.media_aspectos = (obj.votos_entrevista + obj.votos_empresa) /2
        super().save_model(request, obj,form,change)


#admin.site.register(Mensaje)



















































