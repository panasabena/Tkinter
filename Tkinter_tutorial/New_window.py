#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 00:57:27 2023

@author: panasabena
"""

from tkinter import *
from PIL import ImageTk, Image


root = Tk()
# Titulo del programa principal
root.title("Windows")
# Imagen del icono del programa (que en mac no se ve)
root.iconbitmap("/Users/panasabena/Tkinter_tutorial/dashboard.ico")

def open():    
    global my_img
    top = Toplevel()
    top.title("My Second Window")
    top.iconbitmap("/Users/panasabena/Tkinter_tutorial/dashboard.ico")
    my_img = ImageTk.PhotoImage(Image.open("/Users/panasabena/Tkinter_tutorial/dashboard.png"))
    my_label = Label(top, image = my_img).pack()
    btn2 = Button(top, text = "Close Window", command = top.destroy).pack()

btn = Button(root, text = "Open Second Window", command = open).pack()

## Titulo de la ventana emergente
#root.title("Ventana emergente")
# Imagen del icono del programa (que en mac no se ve)
#root.iconbitmap("/Users/panasabena/Tkinter_tutorial/dashboard.ico")


#lbl = Label(top, text = "Hello World").pack()
#my_label = Label(top, image = my_img).pack()

mainloop()