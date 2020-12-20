from tkinter import *

root = Tk()

myLabel1 = Label(root, text='Hello world')
myLabel2 = Label(root, text='Welcome to the window')
myLabel3 = Label(root, text='Welcome to the window end')
myLabel4 = Label(root, text='Welcome 4 to the window end')

myLabel1.grid(row = 0, column=0)
myLabel2.grid(row = 1, column=1)
myLabel3.grid(row = 5, column=2)
myLabel4.grid(row = 4, column=2)

root.mainloop()