############################################   -== INFORMATION ==-   ############################################

#### THE PROGRAM WAS CREATED AND PUBLISHED BY:
#### https://github.com/viktorsynek
#### https://www.linkedin.com/in/viktor-synek/

#############################################   -== PROGRAM ==-   ###############################################

#IMPORT LIBRARIES
import tkinter
from tkinter import *

app = tkinter.Tk()

def delete():
        a = entry.get()
        entry.delete(first=len(a)-1,last="end")
def fresult():
        if entry.get() == "":
                pass
        elif entry.get()[0] == "0":
                entry.delete(0,"end")
        else:
                c_res = entry.get()
                c_res = eval(c_res)
                clearf()
                entry.insert("end",c_res)
def clearf():
        entry.delete(0,"end")

# GRAPHICAL USER INTERFACE STUFF - TKINTER
app.geometry("170x230")
app.title("Calculator")

entry = Entry(app, width=16, borderwidth=3, relief=RIDGE)
entry.grid(pady=10,row=0,sticky="w",padx=15)

clean = Button(app,text="C",width=2,command=clearf,bg="green",fg="white",relief=RIDGE)
clean.grid(row=0,sticky="w",padx=125)
nine = Button(text="9",width=2,command=lambda : entry.insert("end","9"),borderwidth=3,relief=RIDGE)
nine.grid(row=1,sticky="w",padx=15)
eight = Button(text="8",width=2,command=lambda : entry.insert("end","8"),borderwidth=3,relief=RIDGE)
eight.grid(row=1,sticky="w",padx=45)
seven = Button(app,text="7",width=2,command=lambda : entry.insert("end","7"),borderwidth=3,relief=RIDGE)
seven.grid(row=1,sticky="w",padx=75)
plus = Button(app,text="+",width=2,command=lambda : entry.insert("end","+"),borderwidth=3,relief=RIDGE)
plus.grid(row=1,sticky="e",padx=125)
six = Button(text="6",width=2,command=lambda : entry.insert("end","6"),borderwidth=3,relief=RIDGE)
six.grid(row=2,sticky="w",padx=15,pady=5)
five = Button(text="5",width=2,command=lambda : entry.insert("end","5"),borderwidth=3,relief=RIDGE)
five.grid(row=2,sticky="w",padx=45,pady=5)
four = Button(app,text="4",width=2,command=lambda : entry.insert("end","4"),borderwidth=3,relief=RIDGE)
four.grid(row=2,sticky="w",padx=75,pady=5)
minus = Button(app,text="-",width=2,command=lambda : entry.insert("end","-"),borderwidth=3,relief=RIDGE)
minus.grid(row=2,sticky="e",padx=125,pady=5)
three = Button(text="3",width=2,command=lambda : entry.insert("end","3"),borderwidth=3,relief=RIDGE)
three.grid(row=3,sticky="w",padx=15,pady=5)
two = Button(text="2",width=2,command=lambda : entry.insert("end","2"),borderwidth=3,relief=RIDGE)
two.grid(row=3,sticky="w",padx=45,pady=5)
one = Button(app,text="1",width=2,command=lambda : entry.insert("end","1"),borderwidth=3,relief=RIDGE)
one.grid(row=3,sticky="w",padx=75,pady=5)
multiply = Button(app,text="*",width=2,command=lambda : entry.insert("end","*"),borderwidth=3,relief=RIDGE)
multiply.grid(row=3,sticky="e",padx=125,pady=5)
zero = Button(text="0",width=2,command=lambda : entry.insert("end","0"),borderwidth=3,relief=RIDGE)
zero.grid(row=4,sticky="w",padx=15,pady=5)
double_zero = Button(text="00",width=2,command=lambda : entry.insert("end","00"),borderwidth=3,relief=RIDGE)
double_zero.grid(row=4,sticky="w",padx=45,pady=5)
dot = Button(app,text=".",width=2,command=lambda : entry.insert("end","."),borderwidth=3,relief=RIDGE)
dot.grid(row=4,sticky="w",padx=75,pady=5)
divide = Button(app,text="/",width=2,command=lambda : entry.insert("end","/"),borderwidth=3,relief=RIDGE)
divide.grid(row=4,sticky="e",padx=125,pady=5)
result = Button(app,text="=",width=10,command=fresult,bg="green",fg="white",borderwidth=3,relief=RIDGE)
result.grid(row=5,sticky="w",padx=15,pady=5)
modulus = Button(app,text="%",width=2,command=lambda : entry.insert("end","%"),borderwidth=3,relief=RIDGE)
modulus.grid(row=5,sticky="e",padx=125,pady=5)
delete = Button(app,text="del",width=2,command=delete,borderwidth=3,relief=RIDGE)
delete.grid(row=5,sticky="w",padx=80,pady=5)

app.mainloop()
