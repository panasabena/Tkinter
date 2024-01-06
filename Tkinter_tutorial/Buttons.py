#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 14:30:43 2023

@author: panasabena
"""

from tkinter import *
## Lo primero que tenemos que hacer es crear la ventana raiz:
root = Tk()
## Crea un boton
myButton = Button(root, text = "Click Me!")
myButton.pack()
## Crea un boton que no funciona o está deshabilitado
myButton1 = Button(root, text = "BOTON DESHABILITADO!", state = DISABLED)
myButton1.pack()
# Crea un boton que tiene un ancho de 50 en el eje x
myButton2 = Button(root, text = "BOTON", padx = 50)
myButton2.pack()
# Crea un boton que tiene un ancho y largo de 50x50 
myButton3 = Button(root, text = "BOTON", padx = 50, pady = 50)
myButton3.pack()

# Crea un boton que tiene un ancho por defecto y un largo de 50
myButton4 = Button(root, text = "BOTON", pady = 50)
myButton4.pack()

# Ahora para que el boton haga algo lo que tenemos que hacer es crear una funcion
def myClick():
    myLabel = Label(root, text = "Apretaste el boton")
    myLabel.pack()
    
myButton5 = Button(root, text = "Apretá", command = myClick)
myButton5.pack()
## Ahora este boton imprime el texto en azul
myButton6 = Button(root, text = "Apretá", command = myClick, fg = "blue")
myButton6.pack()
## Ahora este boton imprime el boton de color azul y el fondo de color rojo
myButton7 = Button(root, text = "Apretá", command = myClick, fg = "blue", bg = "red")
myButton7.pack()

root.mainloop() 