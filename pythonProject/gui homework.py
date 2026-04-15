import tkinter.messagebox
from tkinter import *
import re
top = Tk()
top.title("Student info")
top.maxsize(width=500,height=500 )
top.configure(width=500,height=600,bg="#89CFF0",padx=10, pady=10)
name=Label(top,text="Student name:",bg="#F4C2C2").grid(row=0, column=1)
ii1= Entry(top, width=30,bg="#F4C2C2")
ii1.grid(row=0, column=2)
ID=Label(top, text="ID:", bg="#F4C2C2").grid(row=1, column=1)
ii2= Entry(top, width=30,bg="#F4C2C2")
ii2.grid(row=1, column=2)
age=Label(top, text="Age:", bg="#F4C2C2").grid(row=2, column=1)
ii3= Entry(top, width=30,bg="#F4C2C2")
ii3.grid(row=2, column=2)
email=Label(top, text="email:", bg="#F4C2C2").grid(row=3, column=1)
ii4= Entry(top, width=30,bg="#F4C2C2")
ii4.grid(row=3, column=2)
def check():
    lis=[]
    f = open("student_info.txt","a")
    na=ii1.get()
    id=ii2.get()
    ag=ii3.get()
    ema=ii4.get()
    n=re.compile("[A-Z]{1}[a-z]{2,}\s[A-Z]{1}[a-z]{2,}")
    i=re.compile("[0-9]{9}")
    a=re.compile("[0-9]{2}")
    e=re.compile('[A-Za-z0-9.-]+@[A-Za-z0-9.-]+\.(com|edu|net)')
    if re.match(n, na):
        lis.append(na)
    if re.match(i, id):
        lis.append(id)
    if re.match(a, ag):
        lis.append(age)
    if re.match(e,ema):
        lis.append(ema)

    if len(lis)==4:
        f.write(f"{na},{id},{ag},{ema}")
        tkinter.messagebox.showinfo("student Information in the text file u created ","written successfully")
    else:
        tkinter.messagebox.showinfo("Invalid values","check it")
    f.close()
c=Button(top,text="print",bg="#F4C2C2", command=check).grid(row=4, column=2)
top.mainloop()