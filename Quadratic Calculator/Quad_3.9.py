
import tkinter as tk
from math import sqrt

def solver(a,b,c):
    """ Solves quadratic equation and returns the result in formatted string """
    D = b*b - 4*a*c
    if D >= 0:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        text = "The discriminant is: %s \n X1 is: %s \n X2 is: %s \n" % (D, x1, x2)        
    else:
        text = "The discriminant is: %s \n This equation has no solutions" % D
    return text

def inserter(value):
    """ Inserts specified value into text widget """
    output.delete("0.0","end")
    output.insert("0.0",value)    

def clear(event):
    """ Clears entry form """
    caller = event.widget
    caller.delete("0", "end")

def handler():
    """ Get the content of entries and passes result to the text """
    try:
        # make sure that we entered correct values
        a_val = float(a.get())
        b_val = float(b.get())
        c_val = float(c.get())
        inserter(solver(a_val, b_val, c_val))
    except ValueError:
        inserter("Make sure you entered 3 numbers")

root = tk.Tk()
root.title("Quadratic calculator")
root.minsize(325,230)
root.resizable(width=False, height=False)


frame = tk.Frame(root)
frame.grid()

a = tk.Entry(frame, width=3)
a.grid(row=1,column=1,padx=(10,0))
a.bind("<FocusIn>", clear)
a_lab = tk.Label(frame, text="x²+").grid(row=1,column=2)

b = tk.Entry(frame, width=3)
b.bind("<FocusIn>", clear)
b.grid(row=1,column=3)
b_lab = tk.Label(frame, text="x+").grid(row=1, column=4)

c = tk.Entry(frame, width=3)
c.bind("<FocusIn>", clear)
c.grid(row=1, column=5)
c_lab = tk.Label(frame, text="= 0").grid(row=1, column=6)

but = tk.Button(frame, text="Solve", command=handler).grid(row=1, column=7, padx=(10,0))

output = tk.Text(frame, bg="lightblue", font="Arial 12", width=35, height=10)
output.grid(row=2, columnspan=8)

root.mainloop()
