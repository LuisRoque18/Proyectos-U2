from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk,Image
root = Tk()

ventana = Frame(root,bg="#a0a0a0").grid()
titlulo = Label(ventana, text="Registro",font=("Roboto",10)).grid(row=3,column=2)
titlulo2 = Label(ventana, text="Producto",font=("Roboto",10)).grid(row=4,column=2)

img = Image.open("correo.png")
imagen = img.resize((75,50))
imagenP = ImageTk.PhotoImage(imagen)
Ponerimagen = Label(ventana, image=imagenP).grid(row=5,column=2,columnspan=1,rowspan=2)

titulo3 = Label(ventana, text="Producto:", font=("Roboto",10)).grid(row=10,column=1)
titulo4 = Label(ventana, text="SKU:", font=("Roboto",10)).grid(row=11,column=1)
registro = Entry(ventana, font=("Roboto",10)).grid(row=10,column=2, padx=1,pady=5)
productos = Entry(ventana, font=("Roboto",10)).grid(row=11,column=2, padx=1,pady=5)
depto = Label(ventana, text=("Depto:"),font=("Roboto",10)).grid(row=13,column=1)
c1 = tk.Checkbutton(ventana, text="A",font=("Roboto",10)).grid(row=15,column=1)
c2 = tk.Checkbutton(ventana, text="B",font=("Roboto",10)).grid(row=15,column=2)
c3 = tk.Checkbutton(ventana, text="C",font=("Roboto",10)).grid(row=15,column=3)

provedor = Label(ventana, text="Proveedor:", font=("Roboto",10)).grid(row=16,column=1)
lista_desplegable = ttk.Combobox(ventana,width=17)
lista_desplegable.grid(row=16,column=2)
opciones = ["NIKE", "ADIDAS", "PUMA"]
lista_desplegable['values']=opciones
  
idioma = Label(ventana, text="Idioma:", font=("Roboto",10)).grid(row=17,column=1)
c4 = tk.Checkbutton(ventana, text="EN",font=("Roboto",10)).grid(row=18,column=1)
c5 = tk.Checkbutton(ventana, text="ESP",font=("Roboto",10)).grid(row=18,column=2)

registrar = Button(ventana, text=("Registrar"), font=("Roboto",10),width=20,height=1).grid(row=25,column=2,padx=1,pady=5)

root.mainloop()