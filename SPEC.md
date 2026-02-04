# Especificación del Proyecto: Sitio Web NeeuroVic

## 1. Información General
* **Nombre de la Marca:** NeeuroVic
* **Propietario:** Victor Manuel Tovar Salazar
* **Profesión:** Neuropsicólogo Clínico
* **Tecnologías:** Python, Flask, Jinja2, HTML5/CSS3.

## 2. Arquitectura del Sitio (5 Páginas)
El agente debe crear las siguientes rutas y sus respectivos archivos de plantilla:

1.  **Home (`/` -> `home.html`):** * Sección Hero con mensaje de bienvenida.
    * Resumen breve de los servicios de neuropsicología.
    * Botón de llamada a la acción (CTA) hacia "Contáctenos".
2.  **Quiénes Somos (`/nosotros` -> `about.html`):**
    * Perfil profesional de Victor Manuel Tovar Salazar.
    * Misión y visión de la marca NeeuroVic enfocada en salud mental y tecnología.
3.  **Servicios (`/servicios` -> `services.html`):**
    * Listado de servicios (Evaluación, Rehabilitación, Consultoría).
    * Diseño basado en tarjetas (cards) limpias.
4.  **Blog (`/blog` -> `blog.html`):**
    * Layout tipo lista para futuros artículos sobre neurociencia y tecnología.
    * Uso de placeholders para las miniaturas de imágenes.
5.  **Contáctenos (`/contacto` -> `contact.html`):**
    * Formulario con campos: Nombre, Correo, Motivo de consulta y Mensaje.
    * Información de contacto y redes sociales en el pie de página.

## 3. Requerimientos Técnicos y Diseño
* **Template Base:** Crear un archivo `layout.html` que contenga la barra de navegación (navbar) y el pie de página (footer) persistentes. Todas las demás páginas deben heredar de este.
* **Estilo:** Diseño moderno, minimalista y responsive (móvil-primero); Para el look and feel del sitio web utiliza la referencia de la imagen `./MOCKUP.jpg` . Se recomienda el uso de un framework ligero como **Bootstrap 5** o **Tailwind CSS** (vía CDN) para agilizar el desarrollo.
* **Manejo de Errores:** Implementar una página de error 404 personalizada.