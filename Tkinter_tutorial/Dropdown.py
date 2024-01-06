#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 00:33:13 2023

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

## Drop Down Boxes

def show():
    myLabel = Label(root, text = clicked.get()).pack()

options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

clicked = StringVar()
clicked.set("Elija un día de la semana")

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text = "Show Selection", command = show).pack()

root.mainloop()