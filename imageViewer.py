from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')

image_0 = ImageTk.PhotoImage(Image.open('images/avodha0.jpg').resize((450,350), Image.ANTIALIAS))
image_1 = ImageTk.PhotoImage(Image.open('images/avodha1.jpeg').resize((450,350), Image.ANTIALIAS))
image_2 = ImageTk.PhotoImage(Image.open('images/avodha2.jpeg').resize((450,350), Image.ANTIALIAS))
image_3 = ImageTk.PhotoImage(Image.open('images/avodha3.jpeg').resize((450,350), Image.ANTIALIAS))
image_4 = ImageTk.PhotoImage(Image.open('images/avodha4.jpg').resize((450,350), Image.ANTIALIAS))

image_list = [image_0, image_1, image_2, image_3, image_4]

status_bar = Label(root, text= f'Image 1 of {len(image_list)}', bd=1, relief=SUNKEN, anchor=E)
# to create status bar, bd- border for the box when it sunken. anchor is direction, E for east

my_label = Label(image=image_0)
my_label.grid(row=0, column=0, columnspan=3)

def forword(image_num):
    global my_label    
    global button_next
    global button_back
    global status_bar 
    my_label.grid_forget()
    my_label = Label(image=image_list[image_num])
    button_next = Button(root, text='>>', command= lambda: forword(image_num+1))
    button_back = Button(root, text='<<', command = lambda:back(image_num))

    #update status bar number.
    status_bar = Label(root, text= f'Image {image_num+1} of {len(image_list)}', bd=1, relief=SUNKEN, anchor=E)
    if image_num == len(image_list)-1:
        button_next = Button(root, text='>>', state= DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_next.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    status_bar.grid(row=2, column=0, columnspan=3, sticky = W+E)

def back(image_num):
    global my_label 
    global button_back 
    global button_next
    global status_bar
    my_label.grid_forget
    my_label = Label(image=image_list[image_num - 1])
    button_next = Button(root, text='>>', command= lambda: forword(image_num))
    button_back = Button(root, text='<<', command = lambda:back(image_num-1))
    status_bar = Label(root, text= f'Image {image_num} of {len(image_list)}', bd=1, relief=SUNKEN, anchor=E)
    if image_num == 1:
        button_back = Button(root, text='<<', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_next.grid(row=1, column=2)
    status_bar.grid(row=2, column=0, columnspan=3, sticky = W+E)

button_next = Button(root, text='>>', command= lambda: forword(1))
button_back = Button(root, text='<<', command = back, state=DISABLED)
button_quit = Button(root, text='Exit', command=root.quit)


button_next.grid(row=1, column=2)
button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1, pady=10) # pady is to make a space btw status bar and the last row 
status_bar.grid(row=2, column=0, columnspan=3, sticky = W+E)
# sticky - for making the sunken box from west to east.

root.mainloop()
