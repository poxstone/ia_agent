---
name: flask-blueprint-creator
description: Úsala cuando el usuario pida agregar una nueva sección, módulo o Blueprint a la aplicación Flask.
---

# Skill de Creación de Blueprints para Flask
Esta skill automatiza la creación de módulos siguiendo una arquitectura limpia y modular.

## Instrucciones
1. **Identificar el nombre**: Extrae el nombre del módulo que el usuario quiere crear (ej. "auth", "dashboard").
2. **Crear Estructura**: Utiliza el script `scripts/scaffold_blueprint.py` para generar la carpeta del módulo y los archivos base.
3. **Registrar**: Indica al usuario que debe importar y registrar el nuevo Blueprint en el archivo principal `app.py`.

## Ejemplo de Uso
Usuario: "Agrega un módulo de autenticación a mi app."
Agente: Ejecuta la creación del scaffold para el Blueprint 'auth'.