from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.title('Simple Calculator')

entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# columnspan - it uses the space of 3 column and adjust when there is a change

def button_click(number):
    current= entry.get()
    entry.delete(0,END)
    entry.insert(0,current + str(number))

def button_clear():
    entry.delete(0, END)

def button_add():
    first_num_str = entry.get()
    global first_num
    global operation 
    operation = 'addition'
    first_num = int(first_num_str)
    entry.delete(0, END)

def button_equal():
    second_num = int(entry.get())
    if operation == 'addition':
        result = first_num + second_num
    if operation == 'substraction':
        result = first_num - second_num
    if operation == 'multiplication':
        result = first_num * second_num
    if operation == 'division':
        result = first_num / second_num

    entry.delete(0,END)
    entry.insert(0, result)

def button_substraction():
    first_num_str = entry.get()
    global first_num
    global operation 
    operation = 'substraction'
    first_num = int(first_num_str)
    entry.delete(0, END)


def button_multiplication():
    first_num_str = entry.get()
    global first_num
    global operation 
    operation = 'multiplication'
    first_num = int(first_num_str)
    entry.delete(0, END)

def button_division():
    first_num_str = entry.get()
    global first_num
    global operation 
    operation = 'division'
    first_num = int(first_num_str)
    entry.delete(0, END)

# to take an input we have to use lambda
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda:button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda:button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda:button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda:button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda:button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda:button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda:button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda:button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda:button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda:button_click(0))
button_clear = Button(root, text='clear', padx=80, pady=20, fg='orange',command=button_clear)
button_add = Button(root, text='+', padx=39, pady=20, command=button_add)
button_equal = Button(root, text='=', padx=91, pady=20, command=button_equal)
button_sub = Button(root, text='-', padx=42, pady=20, command=button_substraction)
button_mult = Button(root, text='*', padx=40, pady=20, command=button_multiplication)
button_div = Button(root, text='/', padx=43, pady=20, command=button_division)

# adding an exit button

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
# columnspan helps to fit into 2 coulumns space.
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_sub.grid(row=6, column=0)
button_mult.grid(row=6, column=1)
button_div.grid(row=6, column=2)

button_exit = Button(root, text='Exit', padx = 140, pady=10, command=root.quit)
button_exit.grid(row=7, column =0, columnspan=3)



root.mainloop()

