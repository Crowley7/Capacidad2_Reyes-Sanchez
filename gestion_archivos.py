# -*- coding: utf-8 -*-
"""
Created on Mon May 30 16:40:36 2022

@author: admin
"""

import os
def crear_archivo(nombre,contenido):
        archivo = open(nombre,"at")
        archivo.write(contenido)
        archivo.close()

def eliminar_archivo(nombre):
    os.remove(nombre)

def agregar_contenido_archivo(nombre,contenido):
    archivo = open(nombre,"at")
    archivo.write("\n" + contenido)
    archivo.close()
    
