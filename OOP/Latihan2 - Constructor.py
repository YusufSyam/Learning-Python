class A:

    # Membuat konstruktor
    # Konstruktor harus setidaknya memiliki 1 parameter, di mana parameter pertama
    # Bisa dijadikan sebagai (this) atau perujuk kepada class
    def __init__(a, inputNama): # sebagai contoh di sini parameter pertama a, tapi sebaiknya pakai self
        a.nama= inputNama

class B:

    def __init__(self, inputNama, inputUmur):
        self.nama= inputNama
        self.umur= inputUmur

instanceA= A("ini nama")
print(instanceA.nama)

instanceB= B(input("Masukkan nama: "),input("Masukkan umur: "))
print("Nama mu {} dan umur mu adalah {:s}".format(instanceB.nama,instanceB.umur))