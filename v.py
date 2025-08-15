from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

def msg():
    messagebox.showwarning("Alert", "Stop, virus found!")

b = Button(root, text="Scan for Virus", command=msg)
b.place(x=40, y=80)

root.mainloop()
