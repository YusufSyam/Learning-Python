from tkinter import *

root = Tk()

# Membuat frame baru dengan menentukan padding
frame = LabelFrame(root, padx=50, pady=50)
frame.pack(padx=10, pady=10)

# Membuat button yang 'parent'-nya bukan root melainkan frame
b = Button(frame, text="Don't Click Here!")
b2 = Button(frame, text="...or here!")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()