from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('file dialog box')
root.geometry('400x400')

var = IntVar()
# when clicked it return 1 otherwise 0.
# to change this put onvalue='wat you want', offvalue='your value' inside the Checkbutton
# and change the var type to StringVar()
Checkbutton(root, text='check 1', variable=var).pack()
# when using var=StringVar() the box by defaul checked, but dont return anything
# to make by default unchecked, c=Checkbutton(arguments) , c.deselect()

def show():
    Label(root, text = var.get()).pack()

Button(root, text='click', command=show).pack()


root.mainloop()