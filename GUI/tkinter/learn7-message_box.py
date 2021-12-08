from tkinter import *
from tkinter import messagebox

root = Tk()

# Daftar messagebox yang bisa kita pakai
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    # Membuat message box askquestion
    response = messagebox.askquestion("This is my Popup!", "Hello World!")

    # Hasil dari message box akan ditampung dalam variabel response
    # Maka kita bisa menampilkan respon dengan seperti ini
    Label(root, text=response).pack()

    if response == "yes":
        Label(root, text="You Clicked Yes!").pack()
    else:
        Label(root, text="You Clicked No!!").pack()

Button(root, text="Popup", command=popup).pack()


mainloop()