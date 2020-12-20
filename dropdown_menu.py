from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('file dialog box')
root.geometry('400x400')

var = StringVar()
var.set('mon')
# to make mon as default

drop_menu = OptionMenu(root, var, 'mon','tue','wed','thu','fri')
# to use a list for menu, *listname (ie use * before list name)
drop_menu.pack()
def show():
    Label(root, text = var.get()).pack()

Button(root, text='click', command=show).pack()


root.mainloop()