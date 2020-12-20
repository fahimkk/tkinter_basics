from tkinter import *
from PIL import ImageTk, Image

home = Tk()
home.title('Home Screen')
""" def image_screen():
    img_screen = Toplevel()
    # Topleve() - is used to create windows
    img_screen.title('Image Screen')
    Label(img_screen, text='my image').pack()
    global img_label
    img_label = ImageTk.PhotoImage(Image.open('fahim.jpg').resize((450,350),Image.ANTIALIAS))
    Label(img_screen, image=img_label).pack()
    Button(image_screen, text='Close', command=image_screen.destroy).pack()
 """
def image_screen_1():
    top = Toplevel()
    # Topleve() - is used to create windows
    top.title('Image Screen')
    Label(top, text='my image').pack()
    global img_label
    img_label = ImageTk.PhotoImage(Image.open('fahim.jpg').resize((450,350),Image.ANTIALIAS))
    Label(top, image=img_label).pack()
    Button(top, text='Close', command=top.destroy).pack()

Label(home, text='To see image Click below').pack()
Button(home, text='Image', command= image_screen_1).pack()

home.mainloop()
