class Hewan:

    def __init__(self, nama, warna):
        self.nama= nama
        self.warna= warna

    def showInfo(self):
        print (self.nama,self.warna)

    def showNamaClass(self):
        print("Ini class Hewan")

class Reptil(Hewan):
    # Saat ingin membuat constructor berbeda di kelas anak, yang tetap
    # Memakai method kelas induk maka kia bisa super()
    def __init__(self,nama,warna): # Di sini constructor mengoverride constructor induk
        # Kita bisa menggunakan cara ini
        # Hewan.__init__(self,nama,warna)
        # Namun lebih baik kalau menggunakan cara ini (super())
        super().__init__(nama,warna) # Dengan cara ini, tidak perlu lagi memasukkan self di parameter
        super().showInfo()

    # Di sini kita ingin mengoverride method showNamaClass (Saat ingin mengoverride,pastikan jumlah parameter atau nama methodnya sama)
    # Tambahan: saat ingin mengoverride sebuah method, sebaiknya kasih komen: override

    # Override
    def showNamaClass(self):
        print("Ini class Reptil")

Ayam= Reptil("Yusuf","biru")
Ayam.showNamaClass()
print(Ayam.__dict__)