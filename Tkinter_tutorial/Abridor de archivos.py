#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 23:38:16 2023

@author: panasabena
"""

""" 
Abridor de archivos
"""

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
# Titulo del programa principal
root.title("Windows")
# Imagen del icono del programa (que en mac no se ve)
root.iconbitmap("/Users/panasabena/Tkinter_tutorial/dashboard.ico")



def open():
    global my_image
    ## Esto abre el buscador de archivos con la ruta especificada y nos muestra los archivos disponibles para ser abiertos con las extensiones que les pasamos por defecto
    root.filename = filedialog.askopenfilename(initialdir = "/Users/panasabena/", title = "Select a file", filetypes = (("Png files","* .png"), ("Icns files","* .icns"), ("Jpeg files","* .jpeg"), ("Python files","* .py"),("Ico files","* .ico"),("Csv files", "* .csv"),("All files", "* .*")))
    ## Este comando nos arroja la ruta en donde está el archivo que seleccionamos
    my_label = Label(root, text = root.filename).pack()
    ## Esta variable toma la ruta de la imagen
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    ## Esta variable imprime la imagen
    my_image_label = Label(image = my_image).pack()    

my_btn = Button(root, text = "Open File", command = open).pack()

mainloop()