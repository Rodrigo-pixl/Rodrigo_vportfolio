# test.py
import os #Usado para intercambiar con el sistema de archivos, como la eliminacion de archivos.
from django.test import TestCase

#Permite sobrescribir configuraciones en un entorno de prueba, como MEDIA_ROOT para evitar usar el sistema de archivos real.
from django.test import override_settings

from appportfolio.models import *

#Facilita la creacion de archivos simulados que se pueden cargar en el modelo
from django.core.files.uploadedfile import SimpleUploadedFile

from os.path import basename #Extrae el nombre base del archivo (sin la ruta)
import tempfile #Usado para crear directorios temporales donde almacenar los archivos durante las pruebas.
from uuid import uuid4 #Genera un identificador unico para evitar colisiones en los nombres de los archivos

from pportfolio.settings import MEDIA_ROOT


#decorador que cambia la ruta solo para pruebas
@override_settings(MEDIA_ROOT=tempfile.gettempdir())
class NoticiaModelTest(TestCase):
    def tearDown(self): #etodo especial de django para eliminar archivos después de las pruebas
        for noticia in Noticia.objects.all():
            if noticia.imagen and os.path.exists(noticia.imagen.path):
                os.remove(noticia.imagen.path)
        super().tearDown()
    def test_creacion_noticia_sin_imagen(self):
        """
        Prueba que una noticia se puede crear sin proporcionar una imagen.
        """
        noticia = Noticia.objects.create(
            titulo="Noticia sin imagen",
            contenido= "Contenido de prueba sin imagen"
        )
        self.assertEqual(noticia.titulo, "Noticia sin imagen")
        self.assertEqual(noticia.contenido, "Contenido de prueba sin imagen")
        self.assertFalse(noticia.imagen) # Verificar que no se asignó imagen
    def test_creacion_noticia_con_imagen(self):
        """
        Prueba que una noticia se puede crear una imagen cargada.
        """
        unique_filename = f'test_image_{uuid4().hex}-jpg'
        image_data = SimpleUploadedFile(
            name=unique_filename,
            content=b'algun contenido de la imagen',
            content_type='image/jpeg'
        )
        noticia = Noticia.objects.create(
            titulo = "Noticia con imagen",
            contenido = "Contenido con imagen",
            imagen=image_data
        )
        self.assertEqual(noticia.titulo, "Noticia con imagen")
        self.assertEqual(noticia.contenido, "Contenido con imagen")
        self.assertIsNotNone(noticia.imagen) #La imagen no deberia estar vacia
        # Comparar con el nombre dinámico generado
        self.assertEqual(basename(noticia.imagen.name),unique_filename)
