#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 23:47:02 2023

@author: panasabena
"""

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learning something about radio buttons")
root.iconbitmap("/Users/panasabena/Tkinter_tutorial/dashboard.ico")

#r = IntVar()
#r.set("2")

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text = text, variable = pizza, value = mode).pack(anchor=W)
        

def clicked(value):
    myLabel = Label(root, text = value)
    myLabel.pack()

#Radiobutton(root, text = "Option 1", variable = r, value = 1, command = lambda: clicked(r.get())).pack()
#Radiobutton(root, text = "Option 2", variable = r, value = 2, command = lambda: clicked(r.get())).pack()

#myLabel = Label(root, text = pizza.get())
#myLabel.pack()

myButton = Button(root, text = "Click here", command = lambda: clicked(pizza.get()))
myButton.pack()

mainloop()