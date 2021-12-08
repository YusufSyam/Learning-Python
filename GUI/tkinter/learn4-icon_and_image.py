from tkinter import *
from PIL import ImageTk,Image

root = Tk()
# Mendefinisikan icon aplikasi, yang mana merupakan file dengan format ico
root.iconbitmap('image\\programmer.ico')

# Meload image dengan library pillow
my_img = ImageTk.PhotoImage(Image.open("image/dahyun.png"))

# Lalu image yang sudah diload dipasang pada label
my_label = Label(image=my_img)
my_label.pack()

# Membuat tombol quit
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()