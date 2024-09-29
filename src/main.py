import os
import argparse

class Parametros(object):
    def __init__(self):
        self.direccion = None
        self.elog = False
        self._parsear_argumentos()

    # Método para parsear los argumentos de la línea de comandos
    def _parsear_argumentos(self):
        parser = argparse.ArgumentParser(description="Procesa un archivo Markdown y le genera un indice.")
        parser.add_argument("--direccion", type=self.validar_direccion_y_markdown,
                            required=True, help="Archivo Markdown a procesar.")
       
        parser.add_argument("--elog", action='store_true',
                            help="Habilitar logging de depuración.")

        args = parser.parse_args()

        self.direccion = args.direccion
        self.elog = args.elog

    # Función para validar si la dirección es un archivo válido
    def validar_direccion(self, direccion):
        if not os.path.isfile(direccion):
            raise argparse.ArgumentTypeError(f"'{direccion}' no es una dirección de archivo válida.")
        return direccion
    
    # Función para validar si el archivo es de tipo Markdown
    def validar_markdown(self, direccion):
        if not direccion.endswith('.md'):
            raise argparse.ArgumentTypeError(f"El archivo '{direccion}' no es un archivo Markdown (.md).")
        return direccion

    # Función combinada que valida ambas condiciones
    def validar_direccion_y_markdown(self, direccion):
        direccion = self.validar_direccion(direccion)   # Valida que sea una dirección de archivo válida
        direccion = self.validar_markdown(direccion)    # Valida que sea un archivo Markdown
        return direccion
