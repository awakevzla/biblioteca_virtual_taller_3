# Biblioteca Virtual - API REST

Sistema de gestión de biblioteca virtual desarrollado con Django REST Framework. Permite la administración de libros, usuarios y préstamos a través de una API RESTful.

## 📋 Descripción del Proyecto

Esta aplicación proporciona una API REST completa para gestionar una biblioteca virtual con las siguientes funcionalidades:

- **Gestión de Libros**: CRUD completo para administrar el catálogo de libros
- **Gestión de Usuarios**: Sistema de autenticación y perfiles de usuario
- **Gestión de Préstamos**: Control de préstamos de libros con fechas de devolución
- **Autenticación**: Sistema de autenticación basado en tokens

## 🏗️ Arquitectura

El proyecto está organizado en tres aplicaciones Django:

- **libros**: Manejo del catálogo de libros
- **usuarios**: Gestión de usuarios y autenticación
- **prestamos**: Control de préstamos y devoluciones

## 🛠️ Tecnologías

- Python 3.9.6
- Django 4.2.27
- Django REST Framework 3.16.1
- SQLite (desarrollo)
- Docker & Docker Compose

## 📦 Requisitos Previos

### Para ejecución local:
- Python 3.9.6 o superior
- pip (gestor de paquetes de Python)
- virtualenv (recomendado)

### Para ejecución con Docker:
- Docker
- Docker Compose

## 🚀 Instalación y Ejecución

### Opción 1: Ejecución Local

#### 1. Clonar el repositorio

```bash
git clone <repository-url>
cd drf-taller3
```

#### 2. Crear y activar entorno virtual

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En macOS/Linux:
source venv/bin/activate
# En Windows:
# venv\Scripts\activate
```

#### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

#### 4. Aplicar migraciones

```bash
cd biblioteca_virtual
python manage.py makemigrations
python manage.py migrate
```

#### 5. Crear superusuario

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para crear el usuario administrador.

#### 6. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

La API estará disponible en: `http://localhost:8000`

### Opción 2: Ejecución con Docker

#### 1. Clonar el repositorio

```bash
git clone <repository-url>
cd drf-taller3
```

#### 2. Construir y ejecutar con Docker Compose

```bash
docker-compose up --build
```

El contenedor automáticamente:
- Instalará las dependencias
- Aplicará las migraciones
- Creará un superusuario por defecto (usuario: `admin`, contraseña: `admin`)
- Iniciará el servidor en el puerto 8000

La API estará disponible en: `http://localhost:8000`

#### 3. Comandos útiles de Docker

```bash
# Detener los contenedores
docker-compose down

# Ver logs
docker-compose logs -f

# Ejecutar comandos dentro del contenedor
docker-compose exec web python biblioteca_virtual/manage.py <comando>

# Acceder al shell de Django
docker-compose exec web python biblioteca_virtual/manage.py shell

# Crear migraciones
docker-compose exec web python biblioteca_virtual/manage.py makemigrations

# Aplicar migraciones
docker-compose exec web python biblioteca_virtual/manage.py migrate
```

## 🔐 Autenticación

La API utiliza autenticación por token. Para obtener un token:

1. Crea un usuario o usa las credenciales del superusuario
2. Realiza una petición POST al endpoint de autenticación
3. Incluye el token en el header de tus peticiones:

```
Authorization: Token <tu-token>
```

## 📚 Endpoints Principales

### Libros
- `GET /api/libros/` - Listar todos los libros
- `POST /api/libros/` - Crear un nuevo libro
- `GET /api/libros/{id}/` - Obtener detalle de un libro
- `PUT /api/libros/{id}/` - Actualizar un libro
- `DELETE /api/libros/{id}/` - Eliminar un libro

### Usuarios
- `GET /api/usuarios/` - Listar usuarios
- `POST /api/usuarios/` - Crear un nuevo usuario
- `GET /api/usuarios/{id}/` - Obtener detalle de un usuario
- `PUT /api/usuarios/{id}/` - Actualizar un usuario

### Préstamos
- `GET /api/prestamos/` - Listar préstamos
- `POST /api/prestamos/` - Crear un nuevo préstamo
- `GET /api/prestamos/{id}/` - Obtener detalle de un préstamo
- `PUT /api/prestamos/{id}/` - Actualizar un préstamo

## 🔍 Administración

Accede al panel de administración de Django en:
- **URL**: `http://localhost:8000/admin`
- **Usuario por defecto (Docker)**: admin
- **Contraseña por defecto (Docker)**: admin

⚠️ **Importante**: Cambia estas credenciales en producción.

## 📝 Estructura del Proyecto

```
drf-taller3/
├── biblioteca_virtual/          # Directorio principal del proyecto
│   ├── biblioteca_virtual/      # Configuración del proyecto Django
│   │   ├── settings.py         # Configuración
│   │   ├── urls.py             # URLs principales
│   │   └── wsgi.py             # WSGI config
│   ├── libros/                 # App de libros
│   ├── usuarios/               # App de usuarios
│   ├── prestamos/              # App de préstamos
│   ├── manage.py               # Script de gestión Django
│   └── db.sqlite3              # Base de datos SQLite
├── docker-compose.yml          # Configuración Docker Compose
├── Dockerfile                  # Imagen Docker
├── entrypoint.sh              # Script de inicialización
├── requirements.txt           # Dependencias Python
└── README.md                  # Este archivo
```
