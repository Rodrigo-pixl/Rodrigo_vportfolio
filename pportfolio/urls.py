# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.urls import path, include, re_path
from appportfolio import views
from appportfolio.views import *

# servicio de ficheros estaticos durante el desarrollo
from django.conf import  settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
# servicios de ficheros estaticos durante el servidor
from django.views.static import serve

from django.urls import path
from . import views
from tkinter.font import names
from appportfolio import views
from appportfolio.views import *


urlpatterns = [
path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    #path('', views.home, name='home'),
    re_path(r'^$', views.home, name ='home'),
    path( 'sobremi/', views.sobremi , name ='sobremi'),
    path('habilidades/', views.habilidades, name = 'habilidades'),

    path('categorias/', views.categorias, name = 'categorias'),

    path ('estudios/', views.estudios, name = 'estudios'),
    re_path(r'^(?P<id>\d+)/ver_experiencia$',
    views.ver_experiencia,name='ver_experiencia'),

    path ('eliminarExperiencia/<int:pk>/',views.eliminarExperiencia, name='eliminarExperiencia'),

    path('persona/nueva/', views.crear_Persona, name='crear_persona'),
    path('persona/editar/<int:persona_id>/', views.editar_persona, name='editar_persona'),
    path ('login/', login_view, name='login'),
    path ('register/', register_view, name='register'),
    #re_path(r'^login/$', auth_views.LoginViews.as_view(template_name="registration/login.html"),name="login"),
    ###IMGEN Y VIDEO
    path('subir_imagenes/', subir_imagenes,name='subir_imagenes'),
    path('subir_videos/', subir_videos, name='subir_videos'),
    path('imagen/editar/<int:imagen_id>/', views.editar_imagen,name='editar_imagen'),
    path('imagen/eliminar/<int:imagen_id>/', views.eliminar_imagen, name='eliminar_imagen'),
    path('video/editar/<int:video_id>/', views.editar_videos, name='editar_video'),
    path('video/eliminar/<int:video_id>', views.eliminar_video,name='eliminar_video'),
    path('contacto/', views.contacto,name='contacto'),
    #Genrear pdf_Entrevistadores
    path('generar_pdf/<int:entrevistador_id>/', views.generar_pdf, name = 'generar_pdf'),
    #Listar_Entrevistadores
    path('listar_entrevistadores/', views.listar_entrevistadores,name = 'listar_entreviatadores'),
    #CURRICULUM
    path('agregar_curriculum/', views.agregar_Curriculum, name='agregar_Curriculum'),
    path('curriculum/<int:id>/', views.detalle_curriculum, name='detalle_curriculum'),
    path('agregar/', views.agregar_curriculum,name='agregar_curriculum'),
    path('ver/<int:pk>/', views.ver_Curriculum ,name='ver_curriculum'),
    path ('generar-pdf/<int:pk>/', views.generar_pdf, name = 'generar_pdf'),
    path ('lista_noticias/' , views.lista_noticias, name='lista_noticias'),
    path ('crear_noticia/' , views.crear_noticia, name='crear_noticia'),
    #Valoraciones
    path('listar_valoraciones/', views.listar_Valoraciones,name='listar_valoraciones'),
    path('actualizar_valoracion/<int.pk>/edit/', views.actualizar_valoracion, name='actualizar_valoracion'),
    path('añadir_valoracion/add/', añadir_valoracion, name='añadir_valoracion'),
    # CHAT ENTREVISTADOR
    path('chat_view/<int:entrevistador_id>/', views.chat_view, name='chat_view'),
    path('chat/enviar/', views.enviar_mesaje, name='enviar_mensajes'),

    # Tareas
    path('listar_tareas/', views.listar_tareas(), name='listar_tareas'),
    path('crear_tarea/', views.crear_tarea, name= 'crear_tarea'),
    path('editar_tarea/', views.editar_tarea, name='editar_tarea'),
    path('eliminiar_tarea/', views.eliminar_tarea, name= 'eliminar_tarea'),
    #Noticia
    path('crear_noticia1/', views.crear_noticia1, name='crear_noticia1'),
    #Nota
    path('añadir-nota/', views.añadir_nota, name='añadir_nota'),
    path('ver-notas/', views.ver_notas, name='ver_notas'),
    #Proyecto
    path('ver_proyectos/', views.ver_proyectos, name='ver_proyectos'),
    path('listar_proyectos/', views.listar_proyectos, name='listar_proyectos'),
    path('añadir_proyectos/', views.agregar_proyectos, name='añadir_proyectos'),
    path('modificar_proyectos/', views.editar_proyectos, name='modificar_proyectos'),
    path('eliminar_proyectos/', views.eliminar_proyectos, name='eliminar_proyectos'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    re_path(r'^media/ (?P<path>.*)$',serve,{
        'document_root' : settings.MEDIA_ROOT,
    })
]

