from tkinter import *
# tkinter is a python library used to create gui applications

root = Tk()
root.title('Calculator') # title on the top title bar.
root.geometry('400x300') # Size of the window. (widthrx height) format.

# Entry widget is used to take user input data.
# here we create four text feild boxes for user to type input.
input_1 = Entry(root, width = 20, borderwidth=5)
input_2 = Entry(root, width = 20, borderwidth=5)
input_3 = Entry(root, width = 20, borderwidth=5)
input_4 = Entry(root, width = 20, borderwidth=5)

# placing the four input boxes.
# grid widget is used to align the entry boxes inside the window
input_1.grid(row=0, column=0, padx=(20,5), pady=(20,10))
input_2.grid(row=0, column=1, padx=(5,20), pady=(20,10))
input_3.grid(row=1, column=0, padx=(20,5), pady=5)
input_4.grid(row=1, column=1, padx=(5,20), pady=5)

# fuction to run when calculate button pressed
def calculate():
    # get method is used to get the user input value 
    # int mehtod is used to convert string into integer
    num1 = int(input_1.get())
    num2 = int(input_2.get())
    num3 = int(input_3.get())
    num4 = int(input_4.get())

    # clearing the input boxes when we press calculate button 
    input_1.delete(0,END)
    input_2.delete(0,END)
    input_3.delete(0,END)
    input_4.delete(0,END)

    # operations
    total = num1+num2+num3+num4
    product = num1*num2*num3*num4
    smallest = min(num1,num2,num3,num4)
    largest = max(num1,num2,num3,num4)

    # labeling text fields, 
    label_sum = Label(root, text='Sum of the four values: '+str(total))
    label_product = Label(root, text='product of the four values: '+str(product))
    label_smallest = Label(root, text='The smallest value: '+str(smallest))
    label_largest = Label(root, text='The largest of the value: '+str(largest))

    label_sum.grid(row=3,column=0,columnspan=2, pady=(10,2))
    label_product.grid(row=4,column=0, columnspan=2, pady=2)
    label_smallest.grid(row=5,column=0, columnspan=2, pady=2)
    label_largest.grid(row=6,column=0, columnspan=2, pady=2)


# calculate button
# Button widget is used to create button, we can pass command in button widget
button_calculate = Button(root, text='Calculate', command=calculate,width=17, height=1, fg='blue')
button_calculate.grid(row=2, column=0, padx=(20,5), pady=15)

# exit button
button_exit = Button(root, text='Exit', command=root.quit,width=17, height=1, fg='red')
button_exit.grid(row=2, column=1, padx=(5,20), pady=15)


root.mainloop()