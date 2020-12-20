from tkinter import *
from tkinter import messagebox

root = Tk()

# type of msg boxes: showinfo, showwarning,showerror, askquestion, askcancel, askyesno, askyesnocancel,askokcancel
def popup():
    response = messagebox.askyesnocancel('Popup Tile', "msg content: nothing")
    if response == 1:
        Label(root, text='Response yes').pack()
    elif response == None:
        Label(root, text='Response cancel').pack()
    else:
        Label(root, text='Response No').pack()

Button(root, text='click',command=popup).pack()

root.mainloop()