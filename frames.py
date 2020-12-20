from tkinter import *

root = Tk()
root.title('frames')

frame_1 = LabelFrame(root, text='Frame - 1', padx = 10, pady=10)
frame_2 = LabelFrame(root, text='Frame - 2', padx = 10, pady=10)
frame_1.pack(padx=10, pady=30)
frame_2.pack(padx=10, pady=10)

b1 = Button(frame_1, text = 'Button 1 of frame 1')
b2 = Button(frame_1, text = 'Button 2 of frame 1')
b3 = Button(frame_2, text = 'Button 1 of frame 2')
b4 = Button(frame_2, text = 'Button 2 of frame 2')

b1.grid(row=0, column=0)
b2.grid(row=1, column=1)
b3.grid(row=0, column=0)
b4.grid(row=1, column=1)

root.mainloop()