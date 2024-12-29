from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor, Genero, Libro
from .forms import AutorForm, GeneroForm, LibroForm
from django.contrib import messages

# Página de inicio
def inicio(request):
    return render(request, 'base.html')

# CRUD para Autor
def autor_list(request):
    autores = Autor.objects.all()
    return render(request, 'libros/autor_list.html', {'autores': autores})

def autor_create(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor creado exitosamente.')
            return redirect('autor_list')
    else:
        form = AutorForm()
    return render(request, 'libros/autor_form.html', {'form': form})

def autor_update(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor actualizado exitosamente.')
            return redirect('autor_list')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'libros/autor_form.html', {'form': form})

def autor_delete(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        messages.success(request, 'Autor eliminado exitosamente.')
        return redirect('autor_list')
    return render(request, 'libros/autor_confirm_delete.html', {'object': autor})

# CRUD para Género
def genero_list(request):
    generos = Genero.objects.all()
    return render(request, 'libros/genero_list.html', {'generos': generos})

def genero_create(request):
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Género creado exitosamente.')
            return redirect('genero_list')
    else:
        form = GeneroForm()
    return render(request, 'libros/genero_form.html', {'form': form})

def genero_update(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    if request.method == 'POST':
        form = GeneroForm(request.POST, instance=genero)
        if form.is_valid():
            form.save()
            messages.success(request, 'Género actualizado exitosamente.')
            return redirect('genero_list')
    else:
        form = GeneroForm(instance=genero)
    return render(request, 'libros/genero_form.html', {'form': form})

def genero_delete(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    if request.method == 'POST':
        genero.delete()
        messages.success(request, 'Género eliminado exitosamente.')
        return redirect('genero_list')
    return render(request, 'libros/genero_confirm_delete.html', {'object': genero})

# CRUD para Libro
def libro_list(request):
    libros = Libro.objects.all()
    return render(request, 'libros/libro_list.html', {'libros': libros})

def libro_create(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro creado exitosamente.')
            return redirect('libro_list')
    else:
        form = LibroForm()
    return render(request, 'libros/libro_form.html', {'form': form})

def libro_update(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro actualizado exitosamente.')
            return redirect('libro_list')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/libro_form.html', {'form': form})

def libro_delete(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        messages.success(request, 'Libro eliminado exitosamente.')
        return redirect('libro_list')
    return render(request, 'libros/libro_confirm_delete.html', {'object': libro})
