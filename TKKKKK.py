from tkinter import*

from tkinter.filedialog import asksaveasfile

root = Tk()
root.geometry('200x150')

def s():
    files = [('All Files','*.*'),
             ('Python Files','*.py'),
             ('text files','*.txt')]
    
    file = asksaveasfile(filetypes=files, defaultextension=files)

btn = Button(root, text='Save', command = lambda : s())

btn.pack(side=TOP)

mainloop()
    
