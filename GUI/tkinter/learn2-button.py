from tkinter import *

root = Tk()

# Membuat fungsi yang akan dijalankan saat button tertindis
def my_click():
    # Jadi kita akan membuat label baru setiap tombol ditekan
    new_label= Label(root, text='Aku ditekan >///<')
    new_label.pack()



# Membuat button
# Parameter command : fungsi yang akan dijalankan saat tombol ditekan, kita bisa mem-pass parameter dengan lambda, seperti pada learn3
# fg dan bg: warna teks dan background, padx= padding x, kita juga bisa mendefinisikan padding y dengan pady
button= Button(root, text='Tekan aku!', command=my_click, fg='blue', bg='#dd3', padx=10)
button.pack()

# Membuat button yang terdisable dengan memberikan parameter state=DISABLED
button2= Button(root, text='Saya disabled', state=DISABLED).pack()

root.mainloop()

