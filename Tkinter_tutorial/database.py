#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 00:45:55 2023

@author: panasabena
"""

from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
# Titulo del programa principal
root.title("Windows")
# Imagen del icono del programa (que en mac no se ve)
root.iconbitmap("/Users/panasabena/Tkinter_tutorial/dashboard.ico")
root.geometry("450x450")



'''
# Create table
c.execute(""" 
          CREATE TABLE addresses (
              first_name text, 
              last_name text, 
              address text, 
              city text, 
              state text, 
              zipcode integer
              )
          """)
'''
def update():
      ## nos conectamos a la dataase de nuevo
      # Create a database or connect to one
      conn = sqlite3.connect('address_book.db')
      # create cursor
      c = conn.cursor()
      
      record_id =  delete_box.get()
      
      c.execute("""
                UPDATE addresses SET 
                first_name = :first, 
                last_name = :last, 
                address = :address, 
                city = :city, 
                state = :state, 
                zipcode = :zipcode
                
                WHERE oid = :oid""", 
                {"first": f_name_editor.get(),
                 "last": l_name_editor.get(),
                 "address": address_editor.get(),
                 "city": city_editor.get(),
                 "state": state_editor.get(),
                 "zipcode": zipcode_editor.get(),
                 "oid": record_id
                    })
      
      # Commit changes
      conn.commit()
      
      # Close connection
      conn.close()

      editor.destroy()
      
# Create Edit function to update a record
def edit():
        global editor
        editor = Tk()
        # Titulo del programa principal
        editor.title("Update A Record")
        # Imagen del icono del programa (que en mac no se ve)
        editor.iconbitmap("/Users/panasabena/Tkinter_tutorial/dashboard.ico")
        editor.geometry("450x450")
        
        ## nos conectamos a la dataase de nuevo
        # Create a database or connect to one
        conn = sqlite3.connect('address_book.db')
        # create cursor
        c = conn.cursor()
        
        record_id = delete_box.get()
        
        
        # Query the database
        # el oid es la primary key
        c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
        
        records = c.fetchall()
        
        ## Create Global variables for text box names
        global f_name_editor
        global l_name_editor
        global address_editor
        global city_editor
        global state_editor
        global zipcode_editor

        ## Create Text Boxes
        f_name_editor = Entry(editor, width = 30)
        f_name_editor.grid(row = 0, column = 1, padx = 20, pady = (10, 0))

        l_name_editor = Entry(editor, width = 30)
        l_name_editor.grid(row = 1, column = 1)

        address_editor = Entry(editor, width = 30)
        address_editor.grid(row = 2, column = 1)

        city_editor = Entry(editor, width = 30)
        city_editor.grid(row = 3, column = 1)

        state_editor = Entry(editor, width = 30)
        state_editor.grid(row = 4, column = 1)

        zipcode_editor = Entry(editor, width = 30)
        zipcode_editor.grid(row = 5, column = 1)


        ## Create Text Box Labels
        f_name_label = Label(editor, text = "First Name")
        f_name_label.grid(row = 0, column = 0, pady = (10, 0))

        l_name_label = Label(editor, text = "Last Name")
        l_name_label.grid(row = 1, column = 0)

        address_label = Label(editor, text = "Address")
        address_label.grid(row = 2, column = 0)

        city_label = Label(editor, text = "City")
        city_label.grid(row = 3, column = 0)

        state_label = Label(editor, text = "State")
        state_label.grid(row = 4, column = 0)

        zipcode_label = Label(editor, text = "Zipcode")
        zipcode_label.grid(row = 5, column = 0)
 
        # Loop thru results
        
        for record in records:
            f_name_editor.insert(0, record[0])
            l_name_editor.insert(0, record[1])
            address_editor.insert(0, record[2])
            city_editor.insert(0, record[3])
            state_editor.insert(0, record[4])
            zipcode_editor.insert(0, record[5])       
 
        ## Create a save Button
        edit_btn = Button(editor, text = "Save Record", command = update)
        edit_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 125)





## Crear funcion para borrar un record
def delete():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # create cursor
    c = conn.cursor()    

    # Delete a record (oid es la primary key de la tabla, que sería el ID number de cada registro que hayamos hecho)
    c.execute("DELETE from addresses WHERE oid = " + delete_box.get())
    
    delete_box.delete(0, END)
    
    # Commit changes
    conn.commit()
    
    # Close connection
    conn.close()
    
    # Clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)



## Create submit function for database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # create cursor
    c = conn.cursor()

    ## Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(), 
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
                  }) 
    
    # Commit changes
    conn.commit()
    # Close connection
    conn.close()


    # Clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

## Create Query Function
def query():
    ## nos conectamos a la dataase de nuevo
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # create cursor
    c = conn.cursor()
    # Query the database
    # el oid es la primary key
    c.execute("SELECT *, oid FROM addresses")
    # este comando nos muestra todo lo que traigamos, puede ser de varias formas, como por ejemplo:
    # c.fetchone()
    # c.fetchmany(con el numero deseado)
    # c.fetchall()
    records = c.fetchall()
    #print(records)
    
    # Loop Thru results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[2]) + "," + "   Id number: " + str(record[6]) + "\n"
        
    
    query_label = Label(root, text = print_records)
    query_label.grid(row = 12, column = 0, columnspan = 2)
    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

## Create Text Boxes
f_name = Entry(root, width = 30)
f_name.grid(row = 0, column = 1, padx = 20, pady = (10, 0))

l_name = Entry(root, width = 30)
l_name.grid(row = 1, column = 1)

address = Entry(root, width = 30)
address.grid(row = 2, column = 1)

city = Entry(root, width = 30)
city.grid(row = 3, column = 1)

state = Entry(root, width = 30)
state.grid(row = 4, column = 1)

zipcode = Entry(root, width = 30)
zipcode.grid(row = 5, column = 1)

delete_box = Entry(root, width = 30)
delete_box.grid(row = 9, column = 1, pady = 5)

## Create Text Box Labels
f_name_label = Label(root, text = "First Name")
f_name_label.grid(row = 0, column = 0, pady = (10, 0))

l_name_label = Label(root, text = "Last Name")
l_name_label.grid(row = 1, column = 0)

address_label = Label(root, text = "Address")
address_label.grid(row = 2, column = 0)

city_label = Label(root, text = "City")
city_label.grid(row = 3, column = 0)

state_label = Label(root, text = "State")
state_label.grid(row = 4, column = 0)

zipcode_label = Label(root, text = "Zipcode")
zipcode_label.grid(row = 5, column = 0)

delete_box_label = Label(root, text = "Select ID")
delete_box_label.grid(row = 9, column = 0, pady = 5)

## Create submit Button
submit_btn = Button(root, text = "Add Record to Database", command = submit)
submit_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 90)


## Create a Query Button
query_btn = Button(root, text = "Show records", command = query)
query_btn.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 122)

## Create a delete button
delete_btn = Button(root, text = "Delete Record", command = delete)
delete_btn.grid(row = 10, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 120)

## Create an update Button
edit_btn = Button(root, text = "Edit Record", command = edit)
edit_btn.grid(row = 11, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 125)




root.mainloop()

#%%
# Me confundí cuando cree la tabla, le puse un espacio de más

'''

# Connect to the SQLite database
conn = sqlite3.connect('address_book.db')
c = conn.cursor()

# Use the ALTER TABLE statement to rename the column
c.execute("""
          ALTER TABLE addresses
          RENAME COLUMN "first" TO first_name
          """)

# Commit the changes
conn.commit()

# Close the connection
conn.close()

#%%

# Me confunfí de vuelta y tipié mal el nombre de addresses
# Connect to the SQLite database
conn = sqlite3.connect('address_book.db')
c = conn.cursor()

# Use the ALTER TABLE statement to rename the column
c.execute("""
          ALTER TABLE addresses
          RENAME COLUMN "adsress" TO address
          """)

# Commit the changes
conn.commit()

# Close the connection
conn.close()


#%%

# Connect to the SQLite database
conn = sqlite3.connect('address_book.db')
c = conn.cursor()


# Ejecutar una consulta SELECT para obtener todos los datos de la tabla addresses
c.execute("SELECT * FROM addresses")

# Obtener los nombres de las columnas
column_names = [description[0] for description in c.description]

# Imprimir los nombres de las columnas
print(column_names)

# Obtener todos los resultados
rows = c.fetchall()

# Imprimir los resultados
for row in rows:
    print(row)

# Cerrar la conexión
conn.close()
'''

