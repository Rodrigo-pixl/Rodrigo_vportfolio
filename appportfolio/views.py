# -*- coding: utf-8 -*-
from http.cookiejar import reach
from lib2to3.fixes.fix_metaclass import find_metas
from multiprocessing.connection import Client
from time import process_time_ns

from __future__ import unicode_literals

from lib2to3.fixes.fix_input import context
from pydoc import pager

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger	#paginacion
from datetime import datetime
from django.utils import timezone
from django.shortcuts import render
from appportfolio.models import *

from django.shortcuts import  redirect
from django.shortcuts import render, redirect, get_objet_or_404
from .models import Persona
# Create your views here.
# Es una funcion ya que esta fuera de una clase

from django.shortcuts import render
import urllib

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, get_user_model, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login,logout as auth_logout
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.models import User
from django.conf import settings

def home (request):
    global DEBUG
    print("Hola estoy en home")
    nombreProyecto = 'PORTAFOLIO'
    fechaCreacion = '23/09/2024'
    context ={'nombreProyecto': nombreProyecto, 'fechaCreacion': fechaCreacion}
    # Modificamos el apartado home con el nuevo codigo proporcionado
    actual=request.user
    idusuario=0
    idusuario=actual.id
    request.session['idusuario']=idusuario
    numconectados=0
    dato= ""
    #ip externa o pública
    lista= "0123456789."
    ip= ""
    #ip externa o pública
    lista = "0123456789."
    ip = ""
    '''
    #dato = urllib.urlopen("http://checkip.dyndns.org").read() ojo hasta 28/7/2021 usada siempre da error
    #dato = urllib.urlopen("https://free-proxy-list.net").read() esta no vacía
    #dato = urllib.urlopen("https://whatismyip.org").read()
    #dato = urllib.urlopen('https://ident.me').read().decode('utf8') #python 3 este es bueno 28/7/2021
    #https://checkip.amazonaws.com
    '''

    try:
        #dato = urllib.request.urlopen('https://www.wikipedia.org').headers.get('X-Client-IP')
        dato =urllib.request.urlopen('https://www.wikipedia.org').headers[X-Client-IP]
        print("IP PUBLICA= "+ str(dato))
    except:
        print("Error en la Libreria de la IP")
        dato= ""
    finally:
        print("USUARIO ACTUAL....("+str(actual)+"]")
    for x in str(dato):
        if x in lista:
            ip += x

    if str(actual)=="AnonymousUser":
        request.session ['tipousurio']= 'anonimo'
        print("IP ANONIMO ....+ str"(ip))
    usuario='prueba'
    context = {'usuario':usuario}
    return render(request,'home.html', context=context)


def sobremi(request):
    print("Hola estoy en sobremi")
    nombre = 'rodrigo'
    edad = 22
    telefono ='3434334'
    cargo ='Peon Caminero'

    #selct * from Categoria
    listaCategorias=Categoria.objects.all().order_by('-nombre_categoria')
    for r in listaCategorias:
        #str siempre
        print(str(r.nombre_categoria))
    context = {'nombre':nombre, 'edad':edad, 'telefono':telefono, 'cargo':cargo, 'listaCategorias':listaCategorias}
    return render(request, 'sobremi.html', context=context)
def habilidades(request):
    print("Estoy en habilidades")
    lista_habilidades = habilidades.objects.all()  # select * from Categorias;
    page = request.GET.get('page')
    # 2 registros por página
    paginator = Paginator(lista_habilidades, 15)
    if page == None:
        print(" page recibe fuera de get o post NONE=" + str(page))
        page = paginator.num_pages
        request.session["pagina"] = page
    else:
        # Guarda la variable
        print(" page recibe esle del none de geo o post=" + str(page))
        request.session["pagina"] = page
        # Recibe la variable
    if request.method == 'GET':
        pagina = request.session["pagina"]
        print(" page recibe en GET=" + str(pagina))
    if request.method == 'POST':
        pagina = request.session["pagina"]
        print(" page recibe en POST=" + str(pagina))

    # Condición muy importqante para saber si existe la variable en la sesión
    if "pagina" in request.session:
        page = request.session["pagina"]
        print(" page recibe de sesion=" + str(page))

    try:
        lista_habilidades = paginator.get_page(page)
    except PageNotAnInteger:
        lista_habilidades = paginator.page(1)
    except EmptyPage:
        lista_habilidades = paginator.page(paginator.num_pages)

    context = {'lista_habilidades': lista_habilidades}
    return  render(request,'habilidades.html')

#listar
def categorias(request):
    #obtenemos un objeto queryset del modelo de categorias
    lista_categorias = Categoria.objects.all()  # select * from Categorias;
    page = request.GET.get('page')
    # 2 registros por página
    paginator = Paginator(lista_categorias, 5)
    if page == None:
        print(" page recibe fuera de get o post NONE=" + str(page))
        page = paginator.num_pages
        request.session["pagina"] = page
    else:
        #Guarda la variable
        print(" page recibe esle del none de geo o post=" + str(page))
        request.session["pagina"] = page
        #Recibe la variable
    if request.method == 'GET':
        pagina = request.session["pagina"]
        print(" page recibe en GET=" + str(pagina))
    if request.method == 'POST':
        pagina = request.session["pagina"]
        print(" page recibe en POST=" + str(pagina))

    #Condición muy importqante para saber si existe la variable en la sesión
    if "pagina" in request.session:
        page = request.session["pagina"]
        print(" page recibe de sesion=" + str(page))

    try:
        lista_categorias = paginator.get_page(page)
    except PageNotAnInteger:
        lista_categorias = paginator.page(1)
    except EmptyPage:
        lista_categorias = paginator.page(paginator.num_pages)

    context = {'lista_categorias': lista_categorias}
    return render(request,'categorias.html', context=context)

def estudios(request):
    print("Estoy En Estudios")
    lista_estudios = estudios().objects.all()  # select * from Categorias;
    page = request.GET.get('page')
    # 2 registros por página
    paginator = Paginator(lista_estudios,15)
    if page == None:
        print(" page recibe fuera de get o post NONE=" + str(page))
        page = paginator.num_pages
        request.session["pagina"] = page
    else:
        # Guarda la variable
        print(" page recibe esle del none de geo o post=" + str(page))
        request.session["pagina"] = page
        # Recibe la variable
    if request.method == 'GET':
        pagina = request.session["pagina"]
        print(" page recibe en GET=" + str(pagina))
    if request.method == 'POST':
        pagina = request.session["pagina"]
        print(" page recibe en POST=" + str(pagina))

    # Condición muy importqante para saber si existe la variable en la sesión
    if "pagina" in request.session:
        page = request.session["pagina"]
        print(" page recibe de sesion=" + str(page))

    try:
        lista_estudios = paginator.get_page(page)
    except PageNotAnInteger:
        lista_estudios= paginator.page(1)
    except EmptyPage:
        lista_estudios= paginator.page(paginator.num_pages)

    context = {'lista_estudios': lista_estudios}
    return render(request,'estudios.html',context=context)

def ver_experiencia(request,id):
    expe_id=id
    experiencia = Experiencia.objects.get(id=expe_id)
    context = {'experiencia': experiencia}
    return render(request,'ver_experiencia.html',context=context)

def experiencia(request):
    lista_experiencias = Experiencia.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(lista_experiencias, 15)
    if page == None:
        print(" page recibe fuera de get o post NONE=" + str(page))
        page = paginator.num_pages
        request.session["pagina"] = page
    else:
        print("page recibe esle del none de geo o post=" + str(page))
        request.session["pagina"] = page
        if request.method == "GET":
            pagina = request.session["pagina"]
            print(" page recibe en GET=" + str(pagina))
        if request.method == "POST":
            pagina = request.session["pagina"]
            print(" page recibe en POST=" + str(pagina))
            request.session["pagina"] = page

def eliminarExperiencia(request, pk) :
    print("Eliminar")
    expe_id=pk
    experiencia= Experiencia.objects.get(id=expe_id)
    if request.method == "POST":
        experiencia.delete()
        return redirect('estudios')
    return render(request, 'eliminar_experiencia.html',{'experiencia': experiencia})

def ver_habilidad(request,id):
    habilidad_id=id
    habilidad =Habilidad.objects.get(id=habilidad_id)
    context = {'habilidad': habilidad}
    return render(request, 'ver_habilidad.html',context=context)

def eliminarHabilidad(request, pk) :
    print("Eliminar Habilidad")
    hablidad_id=pk
    hablidad=Habilidad.objects.get(id=hablidad_id)
    if request.method == "POST":
        hablidad.delete()
        return redirect('estudios')
    return  render(request, 'eliminar_experiencia.html',{'habilidad': hablidad})

def crear_Persona(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        ap1 = request.POST.get('ap1')
        ap2 = request.POST.get('ap2')
        edad = request.POST.get ('edad')
        persona = Persona(nombre=nombre, ap1=ap1, ap2=ap2, edad=edad)
        persona.save()
        return redirect('lista_personas')  # Redirige a la lista de personas o a otra página
        return render(request, 'crear_persona.html')

        # Vista para editar una persona existente
def editar_persona(request, persona_id):
        persona = get_object_or_404(Persona, id=persona_id)

        if request.method == 'POST':
            persona.nombre = request.POST.get('nombre')
            persona.ap1 = request.POST.get('ap1')
            persona.ap2 = request.POST.get('ap2')
            persona.edad = request.POST.get('edad')
            persona.save()
            return redirect('lista_personas')  # Redirige a la lista de personas o a otra página

            return render(request, 'editar_persona.html', {'persona': persona})

def login_view(request):
    print("Logi_view")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST ['pasword']
        user = authenticate (request, username=username, password=password)
        if user is not None:
            login(request,user)
            actual= request.user
            idusuario=0
            idusuario= actual.id
            request.session['idusuario']= idusuario
            print("idusuario="+ str(idusuario))
            entrevistador=Entrevistador.objects.get(user=idusuario)
            idEntrevistador = entrevistador.id
            print("idEntrevistador="+ str(idEntrevistador))
            print("FOTO= "+ str(entrevistador.avatar))
            fotoperfil = settings.MEDIA_URL + str(entrevistador.avatar) if entrevistador.avatar else settings.MEDIA_URL +"MONEDA3.jpg"
            print("avatar=" + str(fotoperfil))
            context = {'fotoperfil': fotoperfil}
            return  render(request, 'home.html', context=context)
            #return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
        return  render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pasword']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('login')
    return render (request,'register.html')

def cerrar(request):
    username = request.user.username
    password = request.user.password
    idusuario = request.user.id
    print("logout................." + username + "clave=" + str(password) + "id=" + str(idusuario))
    user = authenticate(request,username=username, password=password)

    logout(request)
    return redirect('/')

def subir_imagenes(request):
    idUsuario=request.session['idusuario']
    if request.method == 'POST':
        imagenes = request.FILES.getlist('imagenes')

        for imagen in imagenes:
            if imagen.name.endswith(('.png', '.jpg', '.jpeg', '.gif', '.jfif')):
                img=Imagen()
                img.imagen=imagen
                img.save()
        return redirect('subir_imagenes')
    imagenes = Imagen.objects.all()
    return render(request, 'subir_imagenes.html',{'imagenes': imagenes})

def subir_videos(request):
    if request.method == 'POST' and request.FILES['videos']:
        videos = request.FILES.getlist('videos')

        for video in videos:
            if video.name.endswith(('mp3','.mp4','.mov','.avi', '.mkv')):
                v=Video()
                v.save()
        return  redirect('subir_videos')
    videos = Video.objects.all()
    return render (request,'subir_videos.html', {'videos' : videos})

def eliminar_imagen(request, imagen_id):
    imagen = get_object_or_404(Imagen, id=imagen_id)
    if request.method == 'POST':
        imagen.delete()
        return redirect('subir_imagenes') # Redirige a la galeria de imágenes
    return redirect('subir_imagenes') # Redirige a la galeria de imágenes


def editar_imagen(request,imagen_id):
    imagen = get_object_or_404(Imagen, id=imagen_id)

    if request.method == 'POST' and request.FILES.get('nueva_imagen'):
        #Actualizamos la imagen
        imagen.imagen = request.FILES['nueva_imagen']
        imagen.save()
        return redirect('subir_imagenes') #Redirige a la galeria de imagenes
    return redirect('subir_imagenes')

def eliminar_video(request, video_id):
    video = get_object_or_404(Video,id=video_id)
    if request.method == 'POST':
        video.delete()
        return redirect('subir_videos')
    return redirect('subir_videos')

def editar_videos(request, video_id):
    video = get_objet_or_404(Video, id=video_id)
    if request.method == 'POST' and request.FILES.get('nuevo_video'):
        #Actualizamos la imagen
        video.video = request.FILES['nuevo_video']
        video.save()
        return  redirect('subir-videos')
    return redirect('subir_videos')

