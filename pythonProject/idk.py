import tkinter.messagebox

import re

from tkinter import *

top  = Tk()

top.title("Student Project")

top.maxsize(width=500, height=500)

top.configure(width=500,height=600,bg="#befaf2",padx=10, pady=10)

def ok_click():

    p=re.compile(r'([A-Z][a-z]{3,}) ([A-Z][a-z]{3,})')

    if p.match(name.get()):

        fh= open("Data.txt","at")

        fh.writelines(f"{name.get()},{age.get()}\n")

        fh.close()

        tkinter.messagebox.showerror("Information", "Student saved to file!")

    else:

        tkinter.messagebox.showerror("Invalid Information","Name is invalid!")

majors = ['IS','CS','DS']

name = StringVar()

age = StringVar()

major = StringVar(value=majors)

year= StringVar()

lb1= Label(top,text="Name: ",pady=10).grid(row=0, column=0)

lb2= Label(top,text="Age: ",pady=10).grid(row=1, column=0)

lb3= Label(top,text="Major: ",pady=10).grid(row=2, column=0)

lb4= Label(top,text="Year: ",pady=10).grid(row=3, column=0)

e1 = Entry(top, textvariable= name).grid(row=0, column=1)

e2 = Entry(top, textvariable= age).grid(row=1, column=1)

lst1 = Listbox(top)

lst1.insert(0,"CS")

lst1.insert(1,"DS")

lst1.grid(row=2, column=1)

b1 = Button(top, text="Add",pady=10, command=ok_click).grid(row=5, column=1)

top.mainloop()