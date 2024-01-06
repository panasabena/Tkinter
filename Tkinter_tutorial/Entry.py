#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 14:58:35 2023

@author: panasabena
"""

from tkinter import *

root = Tk()

e = Entry(root)
e.pack()
## Otra cosa extra, pero no indispensable es, poner un texto de fondo que indica para que es la ventana de texto
e.insert(0, "Ingrese su nombre")
# Se le puede cambiar el tamaño y el background a la ventana para ingresar texto
e1=Entry(root, width = 50, borderwidth = 5, fg='blue')
e1.pack()

e2=Entry(root, width = 50, borderwidth = 5, fg='blue', bg = "red")
e2.pack()

def myClick():
    myLabel = Label(root, text = "Look! I clicked a Button !!")
    myLabel.pack()
    
myButton = Button(root, text = "Apretá", command = myClick)
myButton.pack()

def myClick2():
    myLabel = Label(root, text = e.get())
    myLabel.pack()    
    
## Tambien se puede sumar un texto antes del e.get()
def myClick3():
    myLabel = Label(root, text = "Hola " + e.get())
    myLabel.pack()  
    
myButton2 = Button(root, text = "Enter your name", command = myClick2)
myButton2.pack()

myButton3 = Button(root, text = "Enter your name", command = myClick3)
myButton3.pack()


root.mainloop()