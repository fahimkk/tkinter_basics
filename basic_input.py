from tkinter import *

root = Tk()

entry = Entry(root, width = 50,fg='blue', bg='yellow', borderwidth = 5)
entry.pack()
# insert a default text inside the box. 0 is the index, 
# only when box means index is 0.
entry.insert(0,'Enter your name')

def clickme():
    hello = 'Hello ' + entry.get()
    # get is the function used to use the input text
    label1 = Label(root, text=hello)
    label1.pack()

myButton = Button(root, text='Enter your Name', padx=30, pady=10, command=clickme,)

myButton.pack()
root.mainloop()