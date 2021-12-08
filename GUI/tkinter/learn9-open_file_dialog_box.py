from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()

# Membuat fungsi yang akan membuka open file dialog box saat sebuah button ditekan
def open():
    global my_image

    # Membuka open file dialog box dengan filedialog.askopenfilename, parameter:
    # - initialdir: folder init saat file dialog box dibuka pertama kali
    # - filetypes: list dari format file yang diinginkan/ditampilkan beserta judulnya
    root.filename = filedialog.askopenfilename(initialdir="", title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))

    # Hasil dari file dialog box adalah direktori dari file yang kita pilih, maka kita akan menampilkannya seperti ini
    my_label = Label(root, text=root.filename).pack()

    # Menampilkan gambar jika file yang dipilih adalah gambar
    try:
        my_image = ImageTk.PhotoImage(Image.open(root.filename))
        my_image_label = Label(image=my_image).pack()
    except:
        my_image_label = Label(text='Ini bukan image jadi tidak ditampilkan').pack()


my_btn = Button(root, text="Open File", command=open).pack()

root.mainloop()