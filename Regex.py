from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Expresiones Regulares")
root.geometry("400x200")
root.resizable(0,0)
myframe = Frame(width=380, height=190)
myframe.pack()
myframe.config(bd=1, relief="solid")
res = StringVar()

titulo = Label(root, text="Validador REGEX", font=("Arial",12))
titulo.place(x=130, y=30)

tituloexp = Label(myframe, text ="Ingresa la expresión: ",font=("Arial",10))
tituloexp.place(x=20, y=70)

ent_expresion = Entry(myframe, width=30)
ent_expresion.place(x=160, y=70)

validar = Button(myframe, text="Validar",fg='white', background='lime green', width=8, font=("Arial",10), command=val_expresion)
validar.place(x=160, y=110)

cerrar = Button(myframe, text="Cerrar",fg='white', background='red', width=8, font=("Arial",10), command=cerrar)
cerrar.place(x=240, y=110)

resultado = Label(myframe, textvariable=res, font=("Arial",10))
resultado.place(x=160, y=150)
root.mainloop()