#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 00:27:10 2023

@author: panasabena
"""

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Popups")
root.iconbitmap("/Users/panasabena/Tkinter_tutorial/dashboard.ico")


"""
There are differents types of messages:
    showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
"""

def popup():
    response = messagebox.askokcancel("This is my popup!", "Hello world")
    # Esta linea de Label (etiqueta) imprime un 1 o un 0 para los tipos de errores askquestion y ok cancel de acuerdo a si se clieckea si o no y lo guarda en la variable local Label
    #Label(root, text = response).pack()
    if response == 1:
        Label(root, text = "You clicked yes!").pack()
    else:
        Label(root, text = "You clicked no!").pack()
        

Button(root, text = "Popup", command = popup).pack()


mainloop()