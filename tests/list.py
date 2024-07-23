# -*- coding: utf-8 -*-
mi_lista = []

# Añadir elementos a la lista
valor1 = "valor1"
mi_lista.append({'clave': 'clave1', 'atributo' : valor1})
mi_lista.append({'clave': 'clave2', 'atributo': 'valor2'})
mi_lista.append({'clave': 'clave3', 'atributo': 'valor3'})

# Imprimir la lista
for elemento in mi_lista:
    print("Clave: {}, Atributo: {}".format(elemento['clave'], elemento['atributo']))