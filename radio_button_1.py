from tkinter import *

root = Tk()

Modes = [('Pepperoni','Pepperoni'),
          ('Cheese','Cheese'),
          ('Mushroom','Mushroom'),
          ('Onion','Onion')]
pizza = StringVar()

def clickme(val):
    Label(root, text=val).pack()

for item, mode in Modes:
    Radiobutton(root, text=item, variable=pizza, value=mode).pack(anchor=W)
    # anchor is used to align all the options in west
Button(root, text='Click Me!', command=lambda:clickme(pizza.get())).pack()

root.mainloop()