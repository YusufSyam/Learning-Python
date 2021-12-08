from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Radio button')

# Membuat variabel baru yang nantinya akan dikaitkan dengan radio button
# Karena value nya integer, maka kita memakai IntVar() dari tkinter, kita juga bisa menggunakan StringVar(), dll
r = IntVar()

# Menyetel nilai default
r.set("2")

# Membuat fungsi yang di mana setiap button / radio button di-click maka akan membuat label baru berisi value radio button r
def clicked(value):
	myLabel = Label(root, text=value)
	myLabel.pack()

# Membuat radio button, kita mengaitkan radiobutton dengan variabel r melalui parameter variable=r
Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

# Membuat label yang menampilkan pilihan radiobutton saat ini
myLabel = Label(root, text=r.get())
myLabel.pack()

# Membuat button yang setiap diklik menjalankan fungsi clicked tadi
myButton = Button(root, text="Click Me!", command=lambda: clicked(r.get()))
myButton.pack()

mainloop()