from tkinter import *
from PIL import ImageTk,Image

# Bedanya window dengan frame adalah run sendiri

root = Tk()

# Membuat fungsi yang akan membuat window baru saat sebuah button ditekan
def open():
    # Mendefinisikan variabel my_img sebagai variabel global
    global my_img

    # Membuat window baru lalu menyetel titlenya
    top = Toplevel()
    top.title('My Second Window')

    # Membuat gambar
    my_img = ImageTk.PhotoImage(Image.open("image/dahyun.png"))
    my_label = Label(top, image=my_img).pack()

    # Membuat button untuk keluar dari window
    btn2 = Button(top, text="close window", command=top.destroy).pack()


btn = Button(root, text="Open Second Window", command=open).pack()

mainloop()