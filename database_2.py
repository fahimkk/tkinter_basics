from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('file dialog box')
root.geometry('500x500')

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
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10,0))
# by putting a padx=20 will make a distance from x axis
# we dont have to put that in every entry, that has the same effect
# we can also pass padding as tuple, for y asix (above, below)

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

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

# box labels
Label(root, text='First Name').grid(row=0, column=0, pady=(10,0))
Label(root, text='Last Name').grid(row=1, column=0)
Label(root, text='Address').grid(row=2, column=0)
Label(root, text='City').grid(row=3, column=0)
Label(root, text='State').grid(row=4, column=0)
Label(root, text='Zipcode').grid(row=5, column=0)
Label(root, text='ID Number').grid(row=9, column=0, pady=5)

# create a submit button for database
def submit():

    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute('INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)',
    # this parameter doesnt want to be same as the parametes outside the function. 
    # its only to use inside this function, we can use any name
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zipcode':zipcode.get()
        })
    conn.commit()
    conn.close()
    # clear the input text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# all items are stored inside a list as a tuple.

def query():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute('SELECT *, oid FROM addresses')
    # this oid is helpful when deleting, ie in database we may have similiar data with same parameter.
    # each record in database only have specific uniq oid.
    records = c.fetchall()
    # records is list with tuples
    print_records = ''
    for record in records:
        # each record is a tuple
        print_records += str(record) + '\n'
    query_label = Label(root, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)
    conn.commit()
    conn.close()
    
def delete():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute('DELETE from addresses WHERE oid='+delete_box.get())
    # oid number is order of the entry like 1,2,3 etc.

    conn.commit()
    conn.close()
    
# Create Submit Button
submit_button = Button(root, text= 'Add Record to Database',command = submit)
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# Create a Query Button
query_button = Button(root, text= 'Get Data from Database',command = query)
query_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=100)


# Create a Delete Button
delete_button = Button(root, text= 'Delete Data from Database',command = delete)
delete_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=90)



root.mainloop()