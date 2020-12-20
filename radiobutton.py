from tkinter import *

root = Tk()

option = IntVar()
option.set(1)

def clicked(val):
    Label(root, text=val).pack()

Radiobutton(root, text='Option 1', variable=option, value=1, command=lambda: clicked(option.get())).pack()
Radiobutton(root, text='Option 2', variable=option, value=2, command=lambda: clicked(option.get())).pack()

Button(root, text='Click Me ! ', command= lambda: clicked(option.get())).pack()

Label(root, text=option.get()).pack()

root.mainloop()