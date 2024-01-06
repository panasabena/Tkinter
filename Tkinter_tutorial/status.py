#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 19:02:45 2023

@author: panasabena
"""

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Creating Dossier app")
root.iconbitmap("/Users/panasabena/Tkinter_tutorial/dashboard.ico")

my_img = ImageTk.PhotoImage(Image.open("/Users/panasabena/Tkinter_tutorial/dashboard.png"))
my_img_1 = ImageTk.PhotoImage(Image.open("/Users/panasabena/Tkinter_tutorial/dashboard1.jpeg"))
my_img_2 = ImageTk.PhotoImage(Image.open("/Users/panasabena/Tkinter_tutorial/dashboard2.jpeg"))
my_img_3 = ImageTk.PhotoImage(Image.open("/Users/panasabena/Tkinter_tutorial/dashboard3.png"))
my_img_4 = ImageTk.PhotoImage(Image.open("/Users/panasabena/Tkinter_tutorial/dashboard4.png"))
my_img_5 = ImageTk.PhotoImage(Image.open("/Users/panasabena/Tkinter_tutorial/dashboard5.jpeg"))

image_list = [my_img, my_img_1, my_img_2, my_img_3, my_img_4, my_img_5]

## Barra de estado
status = Label(root, text = "Image 1 of " + str(len(image_list)), bd = 1, relief= SUNKEN, anchor = E)


my_label = Label(image = my_img)
my_label.grid(row = 0, column = 0, columnspan= 3)


## Funcion de el boton que va para adelante
def forward(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image = image_list[image_number-1])
    button_forward = Button(root, text = ">>", command = lambda: forward(image_number+1))
    button_back = Button(root, text = "<<", command = lambda: back(image_number-1))
    
    if image_number == 5:
        button_forward = Button(root, text = ">>", state = DISABLED)
    
    my_label.grid(row = 0, column = 0, columnspan= 3) 
    button_back.grid(row = 1, column = 0)
    button_forward.grid(row = 1, column = 2)
    
    # Update Status
    status = Label(root, text = "Image " + str(image_number) + " of " + str(len(image_list)), bd = 1, relief= SUNKEN, anchor = E)
    status.grid(row = 2, column = 0, columnspan = 3, sticky = W+E)

# Funcion del boton que va para atras
def back(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image = image_list[image_number-1])
    button_forward = Button(root, text = ">>", command = lambda: forward(image_number+1))
    button_back = Button(root, text = "<<", command = lambda: back(image_number-1))    

    if image_number == 1:
        button_back = Button(root, text = "<<", state = DISABLED)

    # Update Status
    status = Label(root, text = "Image " + str(image_number) + " of " + str(len(image_list)), bd = 1, relief= SUNKEN, anchor = E)
    status.grid(row = 2, column = 0, columnspan = 3, sticky = W+E)


    my_label.grid(row = 0, column = 0, columnspan= 3) 
    button_back.grid(row = 1, column = 0)
    button_forward.grid(row = 1, column = 2)

# Funcion para salir del programa
def salir_programa():
    root.destroy()

button_back = Button(root, text = "<<", command = lambda: back, state = DISABLED)
button_exit = Button(root, text = "Exit Program", command = salir_programa, state = DISABLED )
button_forward = Button(root, text = ">>", command = lambda: forward(2))

button_back.grid(row = 1, column = 0)
button_exit.grid(row = 1, column = 1)
button_forward.grid(row = 1, column = 2)
status.grid(row = 2, column = 0, columnspan = 3, sticky = W+E)

root.mainloop()