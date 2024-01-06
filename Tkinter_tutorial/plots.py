#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 00:42:31 2024

@author: panasabena
"""

from tkinter import *
from PIL import ImageTk, Image
import requests
import json
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title("Plots")
# Imagen del icono del programa (que en mac no se ve)
root.iconbitmap("/Users/panasabena/Tkinter_tutorial/dashboard.ico")
root.geometry("400x200")

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    ## Si queremos otro gráfico lo que tenemos que hacer es escirbir el tipo de gráfico, ejemplo
    # plt.polar(house_prices, 50)
    plt.hist(house_prices, 50)
    plt.show()

my_button = Button(root, text = "Graph It!", command = graph)
my_button.pack()


root.mainloop()