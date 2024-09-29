#!/bin/bash

# Ruta al entorno virtual
VENV_PATH="../env"  # Cambia esta ruta según la ubicación de tu entorno virtual

# Verificar si el entorno virtual existe
if [ ! -d "$VENV_PATH" ]; then
    echo "El entorno virtual no se encontró en $VENV_PATH. Por favor, crea uno antes de continuar."
    exit 1
fi

echo "Activando el entorno virtual..."
source "$VENV_PATH/Scripts/activate"  # Para Linux/macOS
# source "$VENV_PATH/Scripts/activate"  # Para Windows, si usas Git Bash o WSL

echo "Ejecutando el script de Python..."

# Ejecutar el script de Python y pasarle los parámetros que se reciban en el script Bash
python ../src/main.py "$@"

# Verificar el código de salida
if [ $? -eq 0 ]; then
    echo "El script de Python se ejecutó correctamente."
else
    echo "Hubo un error al ejecutar el script de Python."
    exit 1  # Salir con un código de error
fi

# Desactivar el entorno virtual después de la ejecución
deactivate
