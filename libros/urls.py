from django.urls import path
from . import views

urlpatterns = [
    # Página de inicio
    path('', views.inicio, name='inicio'),

    # CRUD para Autor
    path('autor/', views.autor_list, name='autor_list'),  # Listar autores
    path('autor/crear/', views.autor_create, name='autor_create'),  # Crear autor
    path('autor/<int:pk>/editar/', views.autor_update, name='autor_update'),  # Editar autor
    path('autor/<int:pk>/eliminar/', views.autor_delete, name='autor_delete'),  # Eliminar autor

    # CRUD para Género
    path('genero/', views.genero_list, name='genero_list'),  # Listar géneros
    path('genero/crear/', views.genero_create, name='genero_create'),  # Crear género
    path('genero/<int:pk>/editar/', views.genero_update, name='genero_update'),  # Editar género
    path('genero/<int:pk>/eliminar/', views.genero_delete, name='genero_delete'),  # Eliminar género

    # CRUD para Libro
    path('libro/', views.libro_list, name='libro_list'),  # Listar libros
    path('libro/crear/', views.libro_create, name='libro_create'),  # Crear libro
    path('libro/<int:pk>/editar/', views.libro_update, name='libro_update'),  # Editar libro
    path('libro/<int:pk>/eliminar/', views.libro_delete, name='libro_delete'),  # Eliminar libro
]
