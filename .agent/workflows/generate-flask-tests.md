# Workflow: Generador de Pruebas para Flask

## Objetivo
Generar una suite de pruebas completa para las rutas de Flask existentes y verificar que no haya regresiones.

## Instrucciones
1. [cite_start]**Analizar el proyecto**: Identifica todos los archivos que contienen rutas de Flask (Blueprints o app.py)[cite: 599].
2. [cite_start]**Generar Archivos**: Crea archivos de prueba en una carpeta llamada `tests/` con el prefijo `test_` para cada módulo identificado.
3. **Casos de Prueba**:
    * [cite_start]Generar un test para cada ruta que verifique el código de estado 200[cite: 610].
    * Simular entradas de formulario si la ruta acepta métodos POST.
    * Utilizar el cliente de pruebas de Flask (`app.test_client()`).
4. [cite_start]**Validación**: Una vez creados los archivos, ejecuta los tests usando `pytest` en la terminal (siempre pidiendo permiso antes de ejecutar)[cite: 543].
5. **Reporte**: Informa cuántos tests pasaron y si se encontró algún error en la lógica de las rutas.
