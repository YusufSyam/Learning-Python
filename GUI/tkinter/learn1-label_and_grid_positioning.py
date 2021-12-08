# Mengimport semua module yang ada di tkinter
from tkinter import *

# Mendefinisikan variabel window (yang mencakup seluruh gui) dengan Tk()
root= Tk()

# Membuat label
my_label= Label(root, text='Hello World!')
my_label2= Label(root, text='Yusuf Syam')

# Menentukan posisi dengan grid (packing)
my_label.grid(row=0, column=0)
my_label2.grid(row=1, column=1)

# Walaupun kita tulis begini
# my_label2.grid(row=1, column=10000000)
# Posisinya tetap akan sama dengan row 1 column 1
# Ini karena setiap grid posisinya relatif satu sama lain

# Membuat label ketiga
my_label3= Label(root, text='INI LABEL KE TIGA!').grid(row=2, column=2)

# Btw grid tidak bisa dipakai bersamaan denga pack

# Karena gui tkinter berjalan dengan sebuah loop
# Untuk menjalankan gui maka kita harus memanggil fungsi looping ini
root.mainloop()

