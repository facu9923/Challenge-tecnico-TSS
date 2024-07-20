import os
import shutil

def mover_pyc_a_directorio(directorio_pyc):
    if not os.path.exists(directorio_pyc):
        os.makedirs(directorio_pyc)

    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.pyc'):
                ruta_completa = os.path.join(root, file)
                nuevo_directorio = os.path.join(directorio_pyc, os.path.relpath(root, '.'))
                if not os.path.exists(nuevo_directorio):
                    os.makedirs(nuevo_directorio)
                shutil.move(ruta_completa, os.path.join(nuevo_directorio, file))

mover_pyc_a_directorio('pyc_files')