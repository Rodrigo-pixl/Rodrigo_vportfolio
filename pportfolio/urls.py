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

    re_path ('eliminarExperiencia/<int:pk>/',views.eliminarExperiencia, name='eliminarExperiencia'),

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

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    re_path(r'^media/ (?P<path>.*)$',serve,{
        'document_root' : settings.MEDIA_ROOT,
    })
]

