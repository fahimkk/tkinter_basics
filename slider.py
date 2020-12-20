from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('file dialog box')
root.geometry('400x400')
# to set the size of the window 

""" vertical = Scale(root, from_=0, to=200)
# we can not pack in the same line
vertical.pack()

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()

#Label(root, text=horizontal.get()).pack() # this label is not dynamic. it only shows the initial value .

def slide():
    Label(root, text=horizontal.get()).pack()     
    root.geometry(str(horizontal.get())+'x400')
Button(root, text="click", command = slide).pack()
 """

vertical = Scale(root, from_=0, to=200)
vertical.pack()
def slide(var):
    Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + 'x400')
horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL, command=slide)
horizontal.pack()

root.mainloop()