import os
import shutil

def mover_pyc_a_directorio(directorio_pyc):
    # Asegurarse de que el directorio de destino existe
    if not os.path.exists(directorio_pyc):
        os.makedirs(directorio_pyc)

    # Recorrer los archivos en el directorio actual
    for archivo in os.listdir('.'):
        # Comprobar si es un archivo y termina en .pyc
        if os.path.isfile(archivo) and archivo.endswith('.pyc'):
            # Ruta completa del archivo
            ruta_completa = os.path.join('.', archivo)
            # Ruta de destino
            ruta_destino = os.path.join(directorio_pyc, archivo)
            
            # Si ya existe un archivo con el mismo nombre en el destino, lo reemplazamos
            if os.path.exists(ruta_destino):
                os.remove(ruta_destino)
            
            # Mover el archivo
            shutil.move(ruta_completa, ruta_destino)
