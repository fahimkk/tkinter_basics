from tkinter import *

root = Tk()
def clickme():
    label1 = Label(root, text='click me button clicked')
    label1.pack()

myButton = Button(root, text='click me', padx=50, pady=20, command=clickme,fg='blue',bg='red')
# we can use state=DISABLED to disable the button, 
# padx=50 to give x axis width pady=value for y axis, 
# command=functionName - to call a function, dont use () after function name
# fg ="color name" for forground color.- color of the text.
# bg = 'color' for background color, we can also use hexa color code.

myButton.pack()
root.mainloop()