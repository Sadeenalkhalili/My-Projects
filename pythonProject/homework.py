from tkinter import *
T= Tk()
T.title("mini calculator")
T.maxsize(height= 400 , width = 400)
fir= Label(T, text= "First").grid(row = 0 , column = 1)
m1=Entry(T,width=30)
m1.grid(row = 1 , column = 1)
sec= Label(T, text= "Second").grid(row = 2, column = 1)
m2=Entry(T, width = 30)
m2.grid(row = 3 , column = 1)
fin= Label(T, text= "Final").grid(row = 4 , column = 1)
m3 = Entry(T, width = 30)
m3.grid(row = 5 , column = 1)
pro= Label(T, text= "Project").grid(row = 6 , column = 1)
m4 = Entry(T, width = 30)
m4.grid(row = 7 , column = 1)
s= Button(T, text="sum of grades" , command =b)
s.grid(row = 8 , column = 1)
m= Button(T, text="Minimum mark", command = min)
m.grid(row = 9 , column = 1)
d = Button(T, text="Quit",  command= T.destroy)
d.grid(row = 10 , column = 1)
def b():
    f1=float(m1.get())
    f2=float(m2.get())
    f3=float(m3.get())
    f4=float(m4.get())
    sum=f1+f2+f3+f4
    print("sum=",sum)
def min():
    l=[]
    min=0
    l.append(m1.get())
    l.append(m2.get())
    l.append(m3.get())
    l.append(m4.get())
    for i in l:
       if i < min:
           min = i
    print("Minimum number=" , min)
T.mainloop()