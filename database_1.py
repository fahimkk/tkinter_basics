from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('file dialog box')
root.geometry('400x400')

# to create an sqlite database or 
# to connect an existing database
conn = sqlite3.connect('address_book.db')

# create a cursor to move around inside the database
c = conn.cursor()

# Everything is stored inside a table.
# the data types are null, integer, real, text, blob
# to create a table
# commentout once you create a database other wise it will create eveytime you run
'''c.execute(""" CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer)
        """)
'''
# create text boxes for entry
Entry(root, width=30).grid(row=0, column=1, padx=20)
# by putting a padx=20 will make a distance from x axis
# we dont have to put that in every entry, that has the same effect
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

# box labels
Label(root, text='First Name').grid(row=0, column=0)
Label(root, text='Last Name').grid(row=1, column=0)
Label(root, text='Address').grid(row=2, column=0)
Label(root, text='City').grid(row=3, column=0)
Label(root, text='State').grid(row=4, column=0)
Label(root, text='Zipcode').grid(row=5, column=0)

# create a submit button for database
def submit():
    # clear the input text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

submit_button = Button(root, text= 'Clear Text Box',command = submit)
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)
# ipadx will stretch in x axis.

# to commit changes into database
conn.commit()

# to close the connection with the database
conn.close()

root.mainloop()