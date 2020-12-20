from tkinter import *

root = Tk()
# root is a kind of window, which uses to shows everything

# creating a label widget, and pass the root into it.
# label is used for text
myLabel = Label(root, text='Hello world')

myLabel.pack()
# pack is used to show the label widget into the screen.

root.mainloop()
# this is for countinous looping.