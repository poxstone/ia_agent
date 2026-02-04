import os
import sys

def create_blueprint(name):
    base_path = f"modules/{name}"
    os.makedirs(base_path, exist_ok=True)
    
    # Crear el archivo de rutas del Blueprint
    with open(f"{base_path}/routes.py", "w") as f:
        f.write(f"from flask import Blueprint\n\n")
        f.write(f"{name}_bp = Blueprint('{name}', __name__)\n\n")
        f.write(f"@{name}_bp.route('/')\ndef index():\n    return 'Módulo {name} funcionando'")

    print(f"Estructura para el Blueprint '{name}' creada con éxito en {base_path}.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        create_blueprint(sys.argv[1])
        