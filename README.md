# Beer Order Application

Esta aplicación es una API para gestionar pedidos de cerveza en un bar. Implementa una arquitectura hexagonal y se ejecuta en un contenedor Docker con Python 3.11.

## Requisitos

- Docker
- Docker Compose

## Instalación

1. Construye la imagen Docker:

    ```sh
    docker-compose build
    ```

2. Ejecuta la aplicación:

    ```sh
    docker-compose up
    ```

   La aplicación estará disponible en `http://localhost:8000`.

## Estructura del Proyecto

## Estructura del Proyecto

```plaintext
beer_order/
    Dockerfile
    docker-compose.yml
    requirements.txt
    README.md
    manage.py
    beer_order/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    orders/
        __init__.py
        domain/
            __init__.py
            models.py
            repositories.py
        infrastructure/
            __init__.py
            repositories.py
        application/
            __init__.py
            services.py
        interfaces/
            __init__.py
            views.py
            urls.py
        tests.py


## Uso

### Endpoints

- `GET /order/status/` - Obtiene el estado de la orden actual.
- `GET /stock/` - Obtiene el stock de cervezas.

### Tests

Para ejecutar los tests unitarios:

```sh
docker-compose run web python manage.py test
```

## Arquitectura Hexagonal

La aplicación sigue los principios de la arquitectura hexagonal, también conocida como arquitectura de puertos y adaptadores. Esto significa que la lógica central de la aplicación (dominio) no depende de los detalles de implementación de los servicios externos (infraestructura) ni de los controladores (aplicación).

### Dominio

El dominio contiene las entidades centrales y las interfaces que definen el comportamiento del sistema:

- **`orders/domain/models.py`**: Define las entidades y los objetos de valor del dominio.
- **`orders/domain/repositories.py`**: Define las interfaces para los repositorios que gestionan la persistencia de las entidades del dominio.

### Infraestructura

La infraestructura implementa las interfaces definidas en el dominio y contiene la lógica para interactuar con sistemas externos, como bases de datos o APIs externas:

- **`orders/infrastructure/repositories.py`**: Implementa las interfaces de repositorio usando almacenamiento en memoria.

### Aplicación

La capa de aplicación contiene los casos de uso y coordina las interacciones entre el dominio y la infraestructura:

- **`orders/application/services.py`**: Contiene la lógica de los casos de uso y servicios de la aplicación.

### Interfaces

La capa de interfaces contiene los adaptadores y controladores que exponen los endpoints de la API:

- **`orders/interfaces/views.py`**: Define las vistas que manejan las solicitudes HTTP y responden con datos JSON.
- **`orders/interfaces/urls.py`**: Define las rutas de los endpoints de la API.

