from tkinter import *

def sumar():
    a = int(real_a.get())
    b = int(img_a.get())
    a1 = int(real_b.get())
    b1 = int(img_b.get())
    n1 = complex(a,b)
    n2 = complex(a1,b1)
    r = n1+n2
    resultado.set(r)

def res():
    a = int(real_a.get())
    b = int(img_a.get())
    a1 = int(real_b.get())
    b1 = int(img_b.get())
    n1 = complex(a,b)
    n2 = complex(a1,b1)
    r = n1-n2
    resultado.set(r)
def mul():
    a = int(real_a.get())
    b = int(img_a.get())
    a1 = int(real_b.get())
    b1 = int(img_b.get())
    n1 = complex(a,b)
    n2 = complex(a1,b1)
    r = n1*n2
    resultado.set(r)
def div():
    a = int(real_a.get())
    b = int(img_a.get())
    a1 = int(real_b.get())
    b1 = int(img_b.get())
    n1 = complex(a,b)
    n2 = complex(a1,b1)
    r = n1/n2
    resultado.set(r)

      
v = Tk()
v.geometry('500x500')
v.title("Calculadora Complejos")
resultado = StringVar()
lbl_1 = Label(v,text='j')
lbl_1.pack()
lbl_1.place(x=280,y=5)
real_a = Entry(v)
real_a.pack()
real_a.place(x=5,y=5)
img_a = Entry(v)
img_a.pack()
img_a.place(x=150,y=5)

real_b = Entry(v)
real_b.pack()
real_b.place(x=5,y=40)
img_b = Entry(v)
img_b.pack()
img_b.place(x=150,y=40)
lbl_1 = Label(v,text='j')
lbl_1.pack()
lbl_1.place(x=280,y=40)

btn_suma = Button(v,text='Sumar',command=sumar)
btn_suma.pack()
btn_suma.place(x= 5, y = 70)
btn_restar = Button(v,text='Resta',command=res)
btn_restar.pack()
btn_restar.place(x= 105, y = 70)
btn_mul = Button(v,text='Multiplicar',command=mul)
btn_mul.pack()
btn_mul.place(x= 205, y = 70)
btn_div = Button(v,text='Div', command=div)
btn_div.pack()
btn_div.place(x= 305, y = 70)

resul = Label(v,textvariable=resultado)
resul.pack()
resul.place(x= 5, y = 100)

