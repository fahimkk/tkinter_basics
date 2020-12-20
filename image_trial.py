from tkinter import *
from PIL import ImageTk, Image

root = Tk()

button_exit = Button(root, text='Exit', command = root.quit)
button_exit.pack()

# to add icon on the top left of the bar. we need an ico format image
#root.iconbitmap('filename.ico')

# we can add both jpg or png image.
my_image = ImageTk.PhotoImage(Image.open("fahim.jpg"))
my_label = Label(image=my_image)
my_label.pack()

root.mainloop()