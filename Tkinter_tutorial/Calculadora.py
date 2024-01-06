#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 15:40:25 2023

@author: panasabena
"""

from tkinter import *

root = Tk()
root.title("Simple Calculator")


e = Entry(root, width= 35, borderwidth= 5)
e.grid(row = 0, column = 0, columnspan= 3, padx = 10, pady = 10)




#Funciones

def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)
    

def button_add():
    '''
    En este caso, global f_num se utiliza para que la variable f_num se almacene como una variable global y pueda ser accesible y modificada fuera de la función button_add. Sin la declaración global, Python asumiría que f_num es una variable local dentro de la función y no afectaría a una variable global con el mismo nombre.

    Por ejemplo, si más tarde en tu programa quieres acceder a f_num desde otra función o parte del código, necesitarás declararlo como global para poder modificar y acceder al mismo objeto.
    '''
    first_number = e.get() # first_number es una variable local que almacena el valor obtenido del widget de entrada ("Entry") "e"
    global f_num # global f_num indica que "f_num" es una variabl global, no una variable local. 
    global math
    math = "addition"
    f_num = int(first_number) # El valor de "first_number" se convierte a entero y se asigna a "f_num
    e.delete(0, END) # e.delete(0, END) "borra el contenido del widget de entrada para prepararse para la próxima entrada"
    
def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "substraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "divition":
        e.insert(0, f_num / int(second_number))
    #else:
    #    e.insert(0, f_num)

def button_substract():
    first_number = e.get() # first_number es una variable local que almacena el valor obtenido del widget de entrada ("Entry") "e"
    global f_num # global f_num indica que "f_num" es una variabl global, no una variable local. 
    global math
    math = "substraction"
    f_num = int(first_number) # El valor de "first_number" se convierte a entero y se asigna a "f_num
    e.delete(0, END) # e.delete(0, END) "borra el contenido del widget de entrada para prepararse para la próxima entrada"

def button_multiply():
    first_number = e.get() # first_number es una variable local que almacena el valor obtenido del widget de entrada ("Entry") "e"
    global f_num # global f_num indica que "f_num" es una variabl global, no una variable local. 
    global math
    math = "multiplication"
    f_num = int(first_number) # El valor de "first_number" se convierte a entero y se asigna a "f_num
    e.delete(0, END) # e.delete(0, END) "borra el contenido del widget de entrada para prepararse para la próxima entrada"
    
def button_divide():
    first_number = e.get() # first_number es una variable local que almacena el valor obtenido del widget de entrada ("Entry") "e"
    global f_num # global f_num indica que "f_num" es una variabl global, no una variable local. 
    global math
    math = "divition"
    f_num = int(first_number) # El valor de "first_number" se convierte a entero y se asigna a "f_num
    e.delete(0, END) # e.delete(0, END) "borra el contenido del widget de entrada para prepararse para la próxima entrada"
    
## Creando botones
"""
En este caso, la función lambda se utiliza para crear una función anónima en línea que será ejecutada cuando se haga clic en el botón button_1. La función lambda toma el argumento 1 y lo pasa como argumento a la función button_click(1).
Lo mismo se hace con el resto de numeros
"""

button_1 = Button(root, text = "1", padx = 41, pady = 20, command = lambda: button_click(1))
button_2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_click(3))
button_4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_click(6))
button_7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_click(9))
button_0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: button_click(0))
boton_suma = Button(root, text = "+", padx = 39, pady = 20, command = button_add)
boton_igual = Button(root, text = "=", padx = 101, pady = 20, command = button_equal)
boton_borrar = Button(root, text = "Clear", padx = 90, pady = 20, command = button_clear)

boton_resta = Button(root, text = "-", padx = 41, pady = 20, command = button_substract)
boton_multiplicacion = Button(root, text = "*", padx = 40, pady = 20, command = button_multiply)
boton_divicion = Button(root, text = "/", padx = 40, pady = 20, command = button_divide)

## Ubicaciones de los botones en la pantalla
button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)

button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)

button_0.grid(row = 4, column = 0)

boton_borrar.grid(row = 4, column = 1, columnspan= 2)
boton_suma.grid(row = 5, column = 0)
boton_igual.grid(row = 5, column = 1, columnspan= 2)

boton_resta.grid(row = 6, column = 0)
boton_multiplicacion.grid(row = 6, column = 1)
boton_divicion.grid(row = 6, column = 2)


root.mainloop()