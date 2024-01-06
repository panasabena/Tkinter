#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 19:29:38 2024

@author: panasabena
"""

from tkinter import *
from PIL import ImageTk, Image
import requests
import json

# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=46774&distance=5&API_KEY=16F1D02C-E461-41B1-8FFC-5657FBD66A0A

root = Tk()
root.title("App de Clima")
# Imagen del icono del programa (que en mac no se ve)
root.iconbitmap("/Users/panasabena/Tkinter_tutorial/dashboard.ico")
root.geometry("600x100")


def zipLookup():
    #zip.get()
    #zipLabel = Label(root, text = zip.get())
    #zipLabel.grid(row = 1, column = 0, columnspan= 2)
    
    try:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" +  zip.get() +"&distance=5&API_KEY=16F1D02C-E461-41B1-8FFC-5657FBD66A0A")
        api = json.loads(api_request.content)
        city = api [0]['ReportingArea']
        quality = api[0]['AQI']
        category = api [0]['Category']['Name']
        
        if category == 'Good':
            weather_color = "#00e400"
        elif category == 'Moderate':
            weather_color = "#ffff00"
        elif category == 'Unhealthy for Sensitive Groups':
            weather_color = "#ff7e00"
        elif category == 'Unhealthy':
            weather_color = "#ff0000"
        elif category == 'Very Unhealthy':
            weather_color = "8f3f97"
        elif category == 'Hazardous':
            weather_color = "#7e0023"    

        root.configure(background = weather_color)
        
        myLabel = Label(root, text = city + " Air Quality: " +str(quality) + " ,Category: " + category, font = ("Helvetica", 20), background = weather_color)
        myLabel.grid(row = 1, column = 0, columnspan = 2)  
        
    except Exception as e:
        api = "Error..."

zip = Entry(root)
zip.grid(row = 0, column = 0, stick = W+E+N+S)

zipButton = Button(root, text = "Lookup Zipcode", command = zipLookup)
zipButton.grid(row = 0, column = 1)


# La api trae un diccionario en json que tiene 3 elementos y podemos traer lo que le ordenemos, por ejemplo traemos api[0]
# Tambien le podemos ordenar que traiga un determinado elemento del diccionario

#myLabel_1 = Label(root, text = city)
#myLabel_2 = Label(root, text = quality)
#myLabel_3 = Label(root, text = category)

#myLabel_1.pack()
#myLabel_2.pack()
#myLabel_3.pack()


root.mainloop()