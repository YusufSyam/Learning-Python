from tkinter import *

root = Tk()

# Selanjutnya kita ingin membuat input yang akan menjalankan sesuatu jika tombol ditekan
# Parameter: width adalah lebar, kita juga bisa mengubah bg, fg, border, dll
entry= Entry(root, width=50)
entry.grid(row=0, column=0)

# Jika ingin mendefinisikan state/keadaan awal input form jika belum diisi
# entry.insert(0, 'State awal')


def my_click(row_pos, col_pos):
    # Untuk mendapatkan hasil entry, kita bisa menggunakan entry.get()
    new_label= Label(root, text=f'Hello {entry.get()}!')
    new_label.grid(row=row_pos, column=col_pos)

col_pos= 1
row_pos= 1

# Mendefinisikan button, di sini kita memberikan parameter pada command dengan lambda
button= Button(root, text='Enter', command=lambda : my_click(row_pos, col_pos))
button.grid(row=0, column=1)

root.mainloop()

