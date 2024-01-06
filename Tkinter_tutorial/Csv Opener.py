#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 01:00:03 2024

@author: panasabena
"""

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path

import pandas as pd
import json


root = tk.Tk()
root.title("CSV Opener")
# Imagen del icono del programa (que en mac no se ve)
root.iconbitmap("/Users/panasabena/Tkinter_tutorial/dashboard.ico")
root.geometry("500x500")
root.pack_propagate(False)
root.resizable(0, 0) # Esto no deja modificar el tamaño del programa


# Frame for TreeView
frame1 = tk.LabelFrame(root, text = "Excel Data")
frame1.place(heigh = 250, width = 500)

# Frame for open file dialog
file_frame = tk.LabelFrame(root, text = "Open File")
file_frame.place(heigh = 100, width = 400, rely = 0.65, relx = 0)

# Buttons
button1 = tk.Button(file_frame, text = "Browse a File") # Hacer command
button1.place(rely = 0.65, relx = 0.5)

button2 = tk.Button(file_frame, text = "Load File") # Hacer command
button2.place(rely = 0.65, relx = 0.3)

label_file = ttk.Label(file_frame, text = "No file Selected")
label_file.place(rely = 0, relx = 0)

## Treeview Widget
tv1 = ttk.Treeview(frame1)
tv1.place(relheight = 1, relwidth = 1)

treescrolly = tk.Scrollbar(frame1, orient ='vertical', command = tv1.yview)
treescrollx = tk.Scrollbar(frame1, orient ='horizontal', command = tv1.xview)
tv1.configure(xscrollcommand = treescrollx.set, yscrollcommand = treescrolly.set)
treescrollx.pack(side = "bottom", fill = "x")
treescrolly.pack(side = 'right', fill = 'y')


root.mainloop()