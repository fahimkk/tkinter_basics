from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('file dialog box')

def open_file():
    root.filename = filedialog.askopenfilename(initialdir='/home/fahim/Downloads', title='Select file', filetypes=(('Image files','*.jpeg'),('all files','*.*')))
    # root.filename only stores the path of the file that we selected to open.
    Label(root,text=root.filename).pack()
    global my_image
    my_image=ImageTk.PhotoImage(Image.open(root.filename).resize((400,350), Image.ANTIALIAS))
    Label(image=my_image).pack()

Button(root, text='Open file', command= open_file).pack()

root.mainloop()