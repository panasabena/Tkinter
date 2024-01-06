#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 14:23:23 2023

@author: panasabena
"""

from tkinter import *
## Lo primero que tenemos que hacer es crear la ventana raiz:
root = Tk()
## Creamos una etiqueta>
myLabel = Label(root, text = "Hola Mundo!")

# Imprimimos el texto "Hola Mundo!" al medio

myLabel.pack()

root.mainloop()