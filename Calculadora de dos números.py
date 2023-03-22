from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk,Image
root = Tk()

ventana = Frame(root).grid()

titulo = Label(ventana,text="CALCULADORA DE DOS NÚMEROS",font=("Roboto",10,"bold")).grid(row=1,column=2,padx=2,pady=2)
n1 = StringVar()
n2= StringVar()
r= StringVar()
borrar = StringVar()

def borrar():
   n1.set("")
   n2.set("")
   r.set("")

def sumar():
   r.set(float(n1.get())+float(n2.get()))

def resta():
   r.set(float(n1.get())-float(n2.get()))

def multiplicar():
   r.set(float(n1.get())*float(n2.get()))

def dividir():
   r.set(float(n1.get())/float(n2.get()))

numeroA = Label(root, text="Numero A").grid(row=3,column=1)
entradaA = Entry(root,textvariable=n1).grid(row=3,column=2)

numeroB = Label(root, text="Numero B").grid(row=4,column=1)
entradaB = Entry(root,textvariable=n2).grid(row=4,column=2)

resultado = Label(root, text="Resultado").grid(row=5,column=1)
resultadoo = Entry(root,textvariable=r).grid(row=5,column=2)

Bsuma = Button(root, text="     +     ",command=sumar).grid(row=6,column=1)
Bmult = Button(root, text="     X     ",command=multiplicar).grid(row=6,column=2)
Bborrar = Button(root, text="     C     ",command=borrar).grid(row=6,column=3)
Bdiv = Button(root, text="     /     ",command=dividir).grid(row=7,column=1)
Brest = Button(root, text="     -     ",command=resta).grid(row=7,column=2)
Bigual = Button(root, text="     =     ").grid(row=7,column=3)

root.mainloop()