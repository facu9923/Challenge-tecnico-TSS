# -*- coding: utf-8 -*-
import os
import shutil

def mover_pyc_a_directorio(directorio_pyc):
    # Asegurarse de que el directorio de destino existe
    if not os.path.exists(directorio_pyc):
        os.makedirs(directorio_pyc)
        
    for root, dirs, files in os.walk('.'):
        for archivo in files:
            if archivo.endswith('.pyc'):
                ruta_completa = os.path.join(root, archivo)
                
                ruta_destino = os.path.join(directorio_pyc, archivo)

                # Evitar mover archivos que ya están en el directorio de destino
                if os.path.abspath(ruta_completa) == os.path.abspath(ruta_destino):
                    continue
                
                # Si ya existe un archivo con el mismo nombre en el destino, lo reemplazamos
                if os.path.exists(ruta_destino):
                    os.remove(ruta_destino)
                
                # Mover el archivo
                shutil.move(ruta_completa, ruta_destino)
