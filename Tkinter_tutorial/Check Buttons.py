#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 23:27:50 2023

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



def show():
        myLabel = Label(root, text = var.get()).pack()


var = StringVar()

c = Checkbutton(root, text = "Check this box, I dare you!", variable = var, onvalue = "On", offvalue = "Off")
c.deselect()
c.pack()


myButton = Button(root, text = "Show Selection", command = show).pack()

root.mainloop()