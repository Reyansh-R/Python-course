from tkinter import *
from datetime import date

root = Tk()

root.title('Getting started with Widgets')

root.geometry('400x300')

lbl = Label(text="Hi", fg="white", bg = "#123456", height=1, width=300)

name_lbl = Label(text="Full name", bg="#543245")

name_entry = Entry()

def d():
    name = name_entry.get()
    global message
    message = "Welcome to the application, Today's date is "
    greet = "Hello "+name+"/n"

    Textbox.insert(END, greet)
    Textbox.insert(END, message)
    Textbox.insert(END, date.today())

Textbox = Text(height=3)

btn = Button(text="Begin", command=d, height=1, bg="#1261A0", fg='white')

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
Textbox.pack()

root.mainloop()






