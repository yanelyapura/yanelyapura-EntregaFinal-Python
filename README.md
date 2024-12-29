### README - Biblioteca (Proyecto en Django)

Este proyecto fue desarrollado en **Django** como parte de la práctica de la cursada, simulando una biblioteca donde se pueden agregar autores, géneros y libros, además de realizar búsquedas de los libros cargados en la base de datos. Está diseñado para demostrar el manejo de modelos, formularios, vistas y plantillas en Django, acompañado de un diseño responsive básico utilizando **Bootstrap 4**.

---

### Instalación y Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/yanelyapura/yanelyapura-TercerPreEntrega .
   ```

2. **Crear y activar el entorno virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplicar las migraciones de la base de datos:**
   ```bash
   python manage.py migrate
   ```

5. **Correr el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

6. **Acceder a la aplicación:** Abrir el navegador y entrar a `http://127.0.0.1:8000/`.

---

### Funcionalidades y Orden para Probarlas

#### **1. Agregar Datos**
- **Ruta:** `/agregar/`
- Página donde se pueden cargar:
  - **Autores:** Nombre y Nacionalidad.
  - **Géneros:** Nombre.
  - **Libros:** Título, Autor, Género y Fecha de Publicación.
- Cada formulario está separado y al guardar muestra un mensaje de confirmación utilizando los mensajes de Django.

> **Probar:** 
> 1. Primero cargar autores y géneros, ya que los libros dependen de estos datos.
> 2. Luego cargar libros seleccionando autores y géneros previamente creados.

---

#### **2. Buscar Libros**
- **Ruta:** `/buscar/`
- Permite buscar libros por título, mostrando:
  - Título.
  - Autor.
  - Género.
  - Fecha de Publicación.
- Si no se encuentran resultados, muestra un mensaje indicando que no hay coincidencias.

> **Probar:** 
> 1. Realizar búsquedas parciales (ej.: "El").
> 2. Verificar que aparecen correctamente los resultados con los datos cargados.

---

#### **3. Página de Inicio**
- **Ruta:** `/`
- Página principal del sitio que incluye enlaces a las demás secciones.

> **Probar:**
> 1. Verificar que redirige correctamente a las secciones de "Agregar Datos" y "Buscar Libros".

---

### Detalles Técnicos

- **Framework:** Django 4.x.
- **Diseño Frontend:** Bootstrap 4.
- **Base de Datos:** SQLite (configuración predeterminada).
- **Mensajes Flash:** Utiliza los mensajes de Django para feedback al usuario.
- **Responsividad:** El diseño es responsive y se adapta a distintos tamaños de pantalla.

---

### Consideraciones para la Corrección

1. **Código:** 
   - Las vistas, modelos y formularios están organizados siguiendo las mejores prácticas vistas en clase.
   - El proyecto utiliza plantillas extendidas para evitar duplicación de código.

2. **Estilo y Usabilidad:**
   - Las plantillas fueron estilizadas con **Bootstrap 4**.
   - Las validaciones de los formularios y los mensajes son claros para el usuario.

3. **Funcionalidad Completa:**
   - Todas las funcionalidades solicitadas están implementadas y probadas.
   - Se verificó el correcto manejo de dependencias (Autores/Géneros antes de cargar un Libro).

4. **Extensibilidad:** El proyecto está preparado para agregar más funcionalidades si se desea.
