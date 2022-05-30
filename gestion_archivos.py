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

