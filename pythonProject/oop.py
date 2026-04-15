from tkinter import *
import tkinter.messagebox
T=Tk()
T.title("Student info")
T.maxsize(width=500,height=500)
T.configure(width=600,height=600,bg="red",pady=10,padx=10)

name=Label(T,text="Name:").grid(row=0,column=0)
n=Entry(T,width=30)
n.grid(row=0,column=1,pady=10)
age=Label(T,text="Age:").grid(row=1,column=0)
a=Entry(T,width=30)
a.grid(row=1,column=1,pady=10)
Major=Label(T,text="Major:",value=majors).grid(row=2,column=0)
m=Entry(T,width=30)
m.grid(row=2,column=1,pady=10,height=30)
year=Label(T,text="Year:").grid(row=3,column=0)
y=Entry(T,width=30)
y.grid(row=3,column=1,pady=10)


T.mainloop()