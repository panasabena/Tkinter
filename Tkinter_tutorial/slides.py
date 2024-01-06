#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 22:56:08 2023

@author: panasabena
"""

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
# Titulo del programa principal
root.title("Windows")
# Imagen del icono del programa (que en mac no se ve)
root.iconbitmap("/Users/panasabena/Tkinter_tutorial/dashboard.ico")
root.geometry("400x400")

vertical = Scale(root, from_ = 0, to = 400)
vertical.pack()

def slide():
    my_label = Label(root, text = horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

horizontal = Scale(root, from_ = 0, to = 400, orient = HORIZONTAL)
horizontal.pack()

my_label = Label(root, text = horizontal.get()).pack()



my_btn = Button(root, text = "Click Me!", command = slide).pack()

root.mainloop()