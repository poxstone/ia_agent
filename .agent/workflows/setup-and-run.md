# Workflow: Configurar y Lanzar App

## Objetivo
Preparar el entorno virtual, instalar dependencias y abrir la aplicación en el navegador para validación visual.

## Pasos
1. **Instalación**: 
   - Verificar si existe un archivo `requirements.txt`.
   - Si no existe, créalo basándote en las importaciones del proyecto.
   - Ejecutar `pip install -r requirements.txt`.
2. **Ejecución**: 
   - Iniciar el servidor de Flask ejecutando `python app.py`.
   - Identificar el puerto local (usualmente 5000).
3. **Navegador**: 
   - Usar el **Browser Agent** para abrir `http://127.0.0.1:5000`.
   - Realizar una captura de pantalla de la Home para confirmar que cargó correctamente.
