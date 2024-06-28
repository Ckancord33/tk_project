from tkinter import *
from tkinter import ttk  # para combo y pestañas Notebook
import tkinter.font as tkFont

import numpy

matriz = numpy.array([[""] * 3] * 20, dtype=object)
posF = 0


def funcionIngresar():
  global posF
  if (eNombre.get() == "" or eSalario.get() == "" or cbCargo.get() == ""
      or posF >= len(matriz)):
    lRespuesta.config(text="NO SE PUEDE INGRESAR UN TRABAJADOR", fg="red")
  else:
    matriz[posF][0] = eNombre.get()
    matriz[posF][1] = cbCargo.get()
    matriz[posF][2] = eSalario.get()
    posF += 1
    lRespuesta.config(text="Trabajador ingresado con éxito", fg="blue")


def funcionBorrar():
  eNombre.delete(0, END)
  eSalario.delete(0, END)
  lRespuesta.config(text="")
  cbCargo.set("")


def mostrar():
  acumulador = "Los trabajadores ingresados son:\n"
  for f in range(0, len(matriz)):
    for c in range(0, len(matriz[0])):
      acumulador += matriz[f][c] + "\t\t"
    acumulador += "\n"
  area.delete("1.0", END)
  area.insert(INSERT, acumulador)


def limpiar():
  area.delete("1.0", END)


ventana = Tk()
ventana.geometry("600x300")
ventana.title("Ventana con Combo pestañas y area de texto")

panel = ttk.Notebook(ventana)
panel.pack(fill="both", expand="yes")

tab1 = Frame(panel)
tab2 = Frame(panel)

panel.add(tab1, text="Ingreso de datos")
panel.add(tab2, text="Resultados obtenidos")

fuenteT = tkFont.Font(family="Tempus Sans ITC", size=15, weight="bold")
fuente = tkFont.Font(family="Comic Sans MS", size=10)

################################################
#-------------- PESTAÑA 1 --------------------#
################################################

pIngreso = Frame(tab1)
lNombre = Label(pIngreso, text="Nombre: ")
lCargo = Label(pIngreso, text="Cargo: ")
lSalario = Label(pIngreso, text="Salario: ")
eNombre = Entry(pIngreso, width=23)
eSalario = Entry(pIngreso, width=23)
cbCargo = ttk.Combobox(pIngreso,
                       values=["Operario", "Coordinador", "Funcionario"])
bIngresar = Button(pIngreso, text="Ingresar", command=funcionIngresar)
bBorrar = Button(pIngreso, text="Borrar", command=funcionBorrar)

lTitulo = Label(tab1, text="Ingreso de datos del trabajador")
lRespuesta = Label(tab1, text="No se ve")

foto = PhotoImage(file="foEmp.png")
lImagen = Label(tab1, image=foto)

#------------- CONFIGURACIONES----------------
tab1.config(bg="white")
pIngreso.config(bg="azure2", relief="sunken", bd=1)
lTitulo.config(fg="red", font=fuenteT, bg="white")
lNombre.config(font=fuente, bg="azure2")
lCargo.config(font=fuente, bg="azure2")
lSalario.config(font=fuente, bg="azure2")
eNombre.config(font=fuente)
eSalario.config(font=fuente)
cbCargo.config(font=fuente)
bIngresar.config(font=fuente, bg="green3", height=1, width=15)
bBorrar.config(font=fuente, bg="orange red", height=1, width=15)
lRespuesta.config(font=fuente)
#-----------------------------------------

lNombre.grid(row=0, column=0, padx=5, pady=5)
lCargo.grid(row=1, column=0, padx=5, pady=5)
lSalario.grid(row=2, column=0, padx=5, pady=5)
eNombre.grid(row=0, column=1, padx=5, pady=5)
cbCargo.grid(row=1, column=1, padx=5, pady=5)
eSalario.grid(row=2, column=1, padx=5, pady=5)
bIngresar.grid(row=3, column=1, padx=5, pady=5)
bBorrar.grid(row=3, column=0, padx=5, pady=5)

#ubicar los componentes dentro del frame del tab
lTitulo.place(x=30, y=20)
pIngreso.place(x=20, y=80)
lRespuesta.place(x=20, y=240)
lImagen.place(x=380, y=20)

################################################
#-------------- PESTAÑA 2 --------------------#
################################################

pBotones = Frame(tab2, bg="white", relief=RIDGE, bd=5)
bMostrar = Button(pBotones, text="Mostrar", command=mostrar)
bLimpiar = Button(pBotones, text="Limpiar", command=limpiar)
area = Text(tab2)

#----- configuraciones -------
tab2.config(bg="white")
bMostrar.config(font=fuente, width=25, height=1, bg="khaki2")
bLimpiar.config(font=fuente, width=25, height=1, bg="turquoise3")

bMostrar.grid(row=0, column=0, padx=40, pady=5)
bLimpiar.grid(row=0, column=1, padx=40, pady=5)

pBotones.pack(fill="x")
area.pack(pady=10)

ventana.mainloop()  #fin codigo
