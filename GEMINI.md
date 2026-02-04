## Estándares de Ingeniería

- Lenguaje y Estilo: Todo el código debe seguir la guía de estilo PEP 8 para Python.
- Documentación: Cada nuevo método o clase debe incluir un docstring detallado explicando su propósito, argumentos y valores de retorno.
- Modularidad: No generes lógica compleja directamente en el punto de entrada (app.py o main.py). En su lugar, crea archivos de funcionalidad distintos (ej. routes.py, models.py) y llámalos desde el archivo principal.

## Protocolos de Seguridad y Ejecución

- Para mitigar riesgos durante la autonomía de los agentes, se aplican las siguientes medidas de seguridad:
- Desactivación de Auto-Ejecución: No ejecutes acciones del sistema o comandos de terminal sin una confirmación explícita del usuario en el chat.
- Límite de Alcance de Archivos: Restringe las operaciones únicamente a los archivos proporcionados o mencionados en la solicitud actual; no accedas a directorios del sistema fuera de este workspace.
- Advertencia de Comandos Destructivos: Cualquier comando que incluya rm, sudo o sentencias SQL como DROP TABLE debe ir precedido por el mensaje: "WARNING: POTENTIALLY DESTRUCTIVE".

## Restricciones de Flujo de Trabajo

- Validación de Esquema: Antes de implementar cualquier cambio en la base de datos, utiliza siempre el script de validación de esquemas para asegurar el cumplimiento de las políticas internas.
- Pruebas Unitarias: Prioriza la creación de pruebas unitarias para cada nueva funcionalidad antes de dar por completada una tarea.

## Organización del Workspace y Rutas
* **Raíz de la Aplicación**: Toda la lógica de Flask, modelos, rutas y recursos debe residir estrictamente dentro del directorio `app/`.
* **Punto de Entrada**: El archivo principal para ejecutar el servidor debe ser `app/main.py` (o `app/app.py`).
* **Recursos Visuales**:
    - Las plantillas HTML se encuentran en `app/templates/`.
    - Los archivos CSS, JS e imágenes se encuentran en `app/static/`.
* **Restricción de Escritura**: El agente no debe crear archivos de código fuera de la carpeta `app/`incluidos `requirements.txt` `configs.py`