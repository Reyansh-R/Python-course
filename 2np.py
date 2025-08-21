from tkinter import*
from tkinter import messagebox

def m():
    try:
        r = float(entry1.get())
        l = float(entry2.get())
        p = r * l
        result_label.config(text=f"Product: {p}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")


window = Tk()
window.title("Multiply Two Numbers")
window.geometry("300x200")


window.Label(window="Enter first number:").pack(pady=5)
entry1 = window.Entry(window)
entry1.pack()

window.Label(window="Enter second number:").pack(pady=5)
entry2 = window.Entry(window)
entry2.pack()


window.Button(window="Multiply", command=m).pack(pady=10)


result_label = window.LabeL( window="Product: ")
result_label.pack(pady=5)


window.mainloop()           