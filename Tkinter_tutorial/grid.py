#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 14:25:56 2023

@author: panasabena
"""

from tkinter import *
## Lo primero que tenemos que hacer es crear la ventana raiz:
root = Tk()
## Creamos una etiqueta>
myLabel1 = Label(root, text = "Hola Mundo!")
myLabel2 = Label(root, text = "Mi nombre es Alfredo")

# Imprimimos las etiquetas, observar que cuando ponemos las coordenadas de las columnas, estas no se imprimen con una distancia de 4 columnas, porque en el medio no hay nada. Entonces no se tiene en cuenta

myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 5)

root.mainloop()