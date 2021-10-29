class PalingTua:
    def show(self):
        print("Ini Paling tua")

class A(PalingTua):
    def show(self):
        print("Ini A")

class B(PalingTua):
    def show(self):
        print("Ini B")

class C(A,B):
    def show(self):
        print("Ini C")
# ^
# |
# Bentuk nya seperti Diamond

C().show()
# Cara pengecekannya:
# 1. Jika ada show() di c, maka yang dieksekusi show() di C
# 2. Jika tidak ada show() di C, dilihat urutan saat C diinisialisasi: class C(A,B)
# Bisa dilihat A dituliskan duluan baru B, maka yang dieksekusi show() di A
# Kalau tidak ada show() di A, maka yang dieksekusi show() di B
# Jika masih tidak ada show() di B, maka yang dieksekusi show() di class Paling Tua