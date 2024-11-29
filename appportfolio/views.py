# -*- coding: utf-8 -*-
import ctypes.wintypes
from http.client import responses
from http.cookiejar import reach
from lib2to3.fixes.fix_metaclass import find_metas
from logging import fatal, currentframe
from multiprocessing.connection import Client
from tempfile import template
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
from django.views.decorators.csrf import csrf_exempt

#email
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
#pfd's
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
#CURRUCULUM
# Estudios
from .models import DetalleCurriculumEstudios, Curriculum, Estudios
#Experiencia
from .models import DetalleCurriculumExperiencia,Curriculum,Experiencia

# curriculum con reportlab
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib import  colors
from reportlab.lib.utils import ImageReader
import os

from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse
from appportfolio.models import *
# from .models import *

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger #paginacion
from django.contrib.auth import authenticate, get_user_model
login,logout #todas son por defecto
from django.contrib.auth.decorators import login_required
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.models import User
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

#email
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages

#curriculum con reportlab
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
import os

#para el chat
from django.http import  JsonResponse
#para la clase tareas
from .models import Tarea


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
    print("Subir imagenes")
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

def contacto(request):
    if request.method =="POST":
        nombre= request.POST.get('nombre')
        email= request.POST.get ("email")
        asunto= request.POST.get("asunto")
        mensaje= request.POST.get("mensaje")

        context={'nombre': nombre,'email': email,'asunto': asunto, 'mensaje': mensaje}
        template = render_to_string('email_template.html', context = context)

        email=EmailMessage(asunto, template, settings.EMAIL_HOST_USER, ['rodrigoenviar12@gmail.com'])
        email.fail_silenty=False #que no marque error en gmail.
        email.send()

        messages.success(request,'Se ha enviado tu email')
        return redirect('home')
    return render(request, 'correo.html')

#Parte de Listar_Entrevistadores para generar PDF
def listar_entrevistadores(request):
    entrevistadores= Entrevistador.objects.all()
    return render(request, 'listar_entrevistadores.html', {'entrevistadores': entrevistadores})

def generar_pdf(request, entrevistador_id):
    entrevistador = Entrevistador.objects.get(id=entrevistador_id)

    #Crear una repuesta HTTP con contenido tipo PDF
    response= HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename= "entrevistador_{entrevistador.id}.pdf"'

    #Crear el objeto canvas de ReportLab
    p=canvas.Canvas(response,pagesize=letter)

    #Configuración del título
    p.setFont("Helvetica_Bold", 16)
    p.setFillColor(color.darkblue)
    p.drawCentredString(300, 770, "Reporte de Entrevistador")

    #Volver al tamaño de fuente normal
    p.setFont("Helvetica", 12)
    p.setFillColor(colors.black)

    # Datos del entrevistador
    p.drawString(100, 720, f"ID: {entrevistador.id}")
    p.drawString(100, 700, f"Empresa: {entrevistador.empresa or 'N/A'}")
    p.drawString(100, 680, f"Fecha de Entrevista: {entrevistador.fecha_entrevista or 'N/A'}")
    p.drawString(100, 660, f"Conectado: {'Si' if entrevistador.conectado else 'No'}")
    p.drawString(100, 640, f"Seleccionado: {'Si' if entrevistador.seleccionado else 'NO'}")
    p.drawString(100, 620, f"Usuario: {entrevistador.user.username if entrevistador.user else 'N/A'}")

    # Añadir avatar si existe
    if entrevistador.avatar:
        avatar_path = entrevistador.avatar.path
        p.drawImage(avatar_path,100, 500, width=100, height=100)

    # Guardar el PDF
    p.showPage()
    p.save()

    return response

#CURRICULUM
def crear_detalle(request):
    estudio_id = request.GET.get('estudio_id')
    curriculum_id = request.GET.get('curriculum_id')

    # Verifica si los parámetros están presentes y válidos
    if estudio_id and curriculum_id:
        try:
            estudio = Estudios.objects.get(id=estudio_id)
            curriculum = Curriculum.objects.get(id=curriculum_id)
            # Crea el detalle
            DetalleCurriculumEstudios.objects.create(estudio=estudio, curriculum=curriculum)
            return redirect('detallecurriculumestudios_list')
        except Estudios.DoesNotExist:
            # Maneja el caso en que el ID de estudio no existe
            return render(request, 'error.html', {'error': 'El estudio especificado no existe.'})
        except Curriculum.DoesNotExist:
            # Maneja el caso en que el ID de curriculum no existe
            return render(request, 'error.html', {'error': 'El curriculum especificado no existe.'})

    return render(request, 'detallecurriculumestudios_form.html')

def detalle_detallecurriculumestudios(request):
    detalle_id = request.GET.get('id')
    detalle = get_object_or_404(DetalleCurriculumEstudios, id=detalle_id)
    return render(request, 'detallecurriculumestudios_detail.html', {'detalle': detalle})

# PARTE DEL CURRICULUM HECHO POR EL PROFESOR
def agregar_Curriculum(request):
        if request.method == "POST":
            # Obtiene el objeto 'Personal' con id=1 (modifica este criterio según tu lógica)
            try:
                P = Personal.objects.get(id=1)
            except Personal.DoesNotExist:
                return render(request, 'error.html', {'error': 'El registro de Personal no existe'})

            # Asigna los valores de Personal al nuevo Curriculum
            nombre = P.nombre
            ap1 = P.apellido1
            ap2 = P.apellido2
            email = request.POST.get("email")
            telefono = request.POST.get("telefono")

            # Crea y guarda el nuevo Curriculum
            c = Curriculum()
            c.nombre = nombre
            c.apellido1 = ap1
            c.apellido2 = ap2
            c.email = email
            c.telefono = telefono
            c.save()

            # Redirige después de guardar el Curriculum
            return redirect('agregar_Curriculum')

        # Renderiza el formulario si el método es GET
        return render(request, 'alta_Curriculum.html')

def agregar_curriculum(request):
    if request.method== 'POST':
        nombre  = request.POST.get ('nombre')
        ap1 = request.POST.get('ap1')
        ap2 = request.POST.get('ap2')
        email= request.POST.get('ap1')
        telefono = request.POST.get('telefono')

        curriculum = Curriculum(nombre = nombre,ap1=ap1, ap2=ap2, email = email, telefono = telefono)
        curriculum.save()
        return redirect('ver_curriculum', pk=curriculum.pk)

    return rende (request, 'agregar_curriculum.html')

def ver_Curriculum(request, pk):
    curriculum = get_object_or_404(Curriculum, pk=k)
    estudios = DetalleCurriculumEstudio.objects.fitrer (curriculum=curriculum)
    experiencia = DetalleCurriculumExperiencia.objects.filter(curriculum= curriculum)
    context={'curriculum': curriculum, 'estudios': estudios, 'experiencias': experiencia,}

    return render(request, 'ver_curriculum.html', context=context)

#Controlador que genera el pdf
def generar_pdf(request, pk):
    curriculum = get_object_or_404(Curriculum, pk=pk)
    estudios = DetalleCurriculumEstudio.objects.fitrer(curriculum=curriculum)
    experiencia = DetalleCurriculumExperiencia.objects.filter(curriculum=curriculum)

    # Crear la representa HttpResponse con tipo de contenido PDF
    responses = HttpResponse(content_type = 'application/pdf')
    responses ['Content-Dispositio'] = f'attachment; filename="curriculum_{curriculum.nombre}_{curriculum.apellido1}.pdf"'

    #Crear un objeto canvas de ReportLab para generar el PDF
    c=canvas.Canvas(responses, pagesize=letter)
    width, height = letter # Tamaño de la pagina

    #Cargar imagen de avatar

    try:
        #avatar_path = "C:/vportfolio/pportfolio/media/MEDIA/moneda3.jpg"
        avatar_path = os.path.join(settings.MEDIA_ROOT, "MEDIA/moneda3.jpg")
        avatar = ImageReader(avatar_path)
        c.drawImage(avatar, width - 150, height -150, width=100, height=100)
    except Exception as e:
        print((f"No se pudo cargar la imagen: {e}"))
        pass #Si no se encuentra la imagen, el PDF se generará sin ella
# Titulo del curriculum en color
c.setFont("Helvetica-Bold", 20)
c.setFillColor(colors.HexColor("#4B8BBE")) #Cambia a cualquier color hex que prefieras
c.drawString(100, height - 100, f"Curriculum de {curriculum.nombre} {curriculum.apellido1}")

# Informacion de contacto en color diferentr
c.setFont("Helvetica", 12)
csetFillcolor(colors.HexColor("#306998")) # otro color para variar
c.drawString(100, height - 130, f"Email: {curriculum.email}")
c.drawString(100, height - 150, f"Telefono: {curriculum.telefono}")

# Seccion de estudios en otro color
y_positon = height -200
c.setFont("Helvetica-Bold", 14)
c.setFillColor(colors.HexColor("#FFD43B"))
c.drawString(100, y_position, "Estudios:")

#Mostrar cada estudio con detalles
c.setFont("Helvetica", 12)
y_positon -=20
for estudio in estudios:
    c.setFillColor(colors.black)
    c.drawString (100, y_positon, f"{estudio.titulacion} en {estudio.institucion} ({estudio.fechaInicio} - {estudio.fechaFin})")
    y_positon -=20

# Seccion de experiencia laboral
y_positon -=40
c.setFont("Helvetica-Bold", 14)
c.setFillColor(colors.HexColor("#306998"))
c.drawString(100, y_positon, "Experiencia laboral:")
y_positon -=20
c.setFont("Helvetica",12)
for experiencia in experiencias:
    c.setFillColor(colors.black)
    c.drawString(100, y_positon,f"{experiencia.puesto} en {experiencia.empresa} ({experiencia.fechaInicio} - {experiencia.fechaFin})")
    y_positon -=20

# Finalizar el PDF
c.showPage() #si tienes mas paginas
c.save()
#return response


# Vista para ver las noticias
def lista_noticias(request):
    noticias = Noticia.objects.all().order_by('-fecha_creacion')
    return  render (request, 'lista_noticias.html' , {'noticias' : noticias})
# Vista para crear una nueva noticias
def crear_noticia(request):
        if request.method == 'POST':
            titulo = request.POST.get('titulo')
            contenido = request.POST.get('contenido')
            imagen = request.FILES.get('imagen')

            if titulo and contenido:
                noticia = Noticia.objects.create(titulo=titulo, contenido=contenido, imagen=imagen)
                return redirect('listar_noticias')
            else:
                return HttpResponse("Error: El titulo y el contenido son obligatorios.", status=400)

            return render(request, 'crear_noticia.html')

#VALORACIONES
def listar_Valoraciones(request):
    valoraciones = Valoracion.objects.all()
    return render(request, 'list.html', {'valoraciones': valoraciones})
def actualizar_valoracion(request, pk):
    valoracion = get_object_or_404(Valoracion, pk=pk)
    if request.method == 'POST':
        votos_entrevista = int(request.POST.get('votos_entrevista', valoracion.votos_entrevista))
        votos_empresa = int(request.POST.get('votos_empresa', valoracion.votos_empresa))

        # Actualizar los votos y recalcular la media
        valoracion.votos_entrevista = votos_entrevista
        valoracion.votos_empresa = votos_empresa
        valoracion.media_aspectos = (votos_entrevista + votos_empresa) /2
        valoracion.save()

        return redirect('listar_valoraciones')

    return render(request, 'update.html', {'valoracion': valoracion})

def añadir_valoracion(request):
    if request.method == 'POST':
        entrevista = request.POST.get('entrevista')
        empresa = request.POST.get('empresa')
        votos_entrevista = int (request.POST.get('votos_entrevista', 0))
        votos_empresa = int(request.POST.get('votos_empresa', 0))

        # Calcular la media de los aspectos
        media_aspectos = (votos_entrevista + votos_empresa) /2
        #Crear y guardar la nueva valoración
        nueva_valoracion = Valoracion.objects.create(
            entrevista=entrevista,
            votos_entrevista=votos_entrevista,
            votos_empresa=votos_empresa,
            media_aspectos= media_aspectos
        )
        return redirect('listar_valoraciones')
    return render(request, 'add.html')

@login_required
def chat_view(request, entrevistador_id):
    entrevistador = get_object_or_404(Entrevistador, id=entrevistador_id)
    mensajes = Mensaje.objects.filter(
        (models.Q(remitente=request.user) & models.Q(destinatario= entrevistador.user)) |
        (models.Q(remitente=entrevistador.user) & models.Q(destinatario=request.user))
    )
    # Agregar la propiedad 'clase' para usarla en el template
    for mensaje in mensajes:
        mensaje.clase = 'enviado' if mensaje.remitente == request.user else 'recibido'

    # Renderizar solo el chat para la respuesta AJAX
    if request.headers.get('X_Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'mensajesHtml': render_to_string('chat_mensajes.html', {'mensajes': mensajes}),
        })
    return render(request, 'chat.html', {'entrevistador': entrevistador, 'mensajes':mensajes})
@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        destinatario_id = request.POST.get('destinatario_id')
        destinatario = get_object_or_404(User, id=destinatario_id)

        mensaje = Mensaje.objects.create(
            remitente= request.user,
            destinatario = destinatario,
            contenido=contenido
        )
        return JsonResponse({'status': 'success', 'mensaje': mensaje.contenido,
                             'fecha_envio': mensaje.fecha_envio})
    return JsonResponse({'status': 'error', 'message' : 'Método no permitido'})




# Listar tareas
def listar_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'tareas/listar_tareas.html', {'tareas': tareas})

# Crear una nueva tarea
def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tareas')
    else:
        form = TareaForm()
    return render(request, 'tareas/crear_tarea.html', {'form': form})

# Editar una tarea
def editar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('listar_tareas')
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'tareas/editar_tarea.html', {'form': form})

# Eliminar una tarea
def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    if request.method == 'POST':
        tarea.delete()
        return redirect('listar_tareas')
    return render(request, 'tareas/eliminar_tarea.html', {'tarea': tarea})

