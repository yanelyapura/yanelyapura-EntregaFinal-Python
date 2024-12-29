from django import forms
from .models import Autor, Genero, Libro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre del autor'
            }),
            'nacionalidad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la nacionalidad del autor'
            }),
        }
        labels = {
            'nombre': 'Nombre del Autor',
            'nacionalidad': 'Nacionalidad',
        }

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre del género'
            }),
        }
        labels = {
            'nombre': 'Nombre del Género',
        }

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el título del libro'
            }),
            'autor': forms.Select(attrs={
                'class': 'form-control',
            }),
            'genero': forms.Select(attrs={
                'class': 'form-control',
            }),
            'fecha_publicacion': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
        }
        labels = {
            'titulo': 'Título del Libro',
            'autor': 'Autor',
            'genero': 'Género',
            'fecha_publicacion': 'Fecha de Publicación',
        }
