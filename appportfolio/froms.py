# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from appportfolio.models import *
from django import forms

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'contenido', 'imagen']  # Especifica los campos que deseas incluir
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Contenido'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
class NotaForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = ['asignatura', 'nota']
        labels = {
            'asignatura': 'Asignatura',
            'nota': 'Nota',
        }
        widgets = {
            'nota': forms.NumberInput(attrs={'step': '0.01'}),
        }