---
trigger: always_on
---

# Reglas de Seguridad y Estilo para Flask

## Seguridad de la Aplicación
* **Prohibido Hardcoding**: Nunca generes código que incluya claves secretas o credenciales directamente en los archivos `.py`. [cite_start]Siempre utiliza `os.getenv` o la librería `python-dotenv`[cite: 231, 232].
* **Configuración de Debug**: Al generar el bloque `if __name__ == "__main__":`, asegúrate de que `app.run(debug=True)` solo esté presente si se detecta un entorno de desarrollo local.

## Calidad del Código
* [cite_start]**Tipado Estricto**: Todo el código de Python generado debe incluir "type hints" (ej. `def index() -> str:`) para mejorar la legibilidad y mantenimiento[cite: 415, 595].
* [cite_start]**Manejo de Errores**: Cada ruta de Flask debe incluir un bloque `try-except` básico o un manejador de errores global para evitar caídas del servidor ante entradas inesperadas[cite: 231].
* [cite_start]**Separación de Intereses**: Si el agente detecta que una función de ruta excede las 30 líneas, debe sugerir mover la lógica de negocio a un archivo separado llamado `services.py`[cite: 597, 598].

## librerias
* para los entornos virtuales (python virtualenv) utiliza la carpeta '.venv/'

