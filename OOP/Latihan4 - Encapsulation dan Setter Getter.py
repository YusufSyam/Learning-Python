class Kucing:

    def __init__(self,inputNama):
        # Untuk mendefinisikan variabel private, kita memakai 2 Underscore (__) sebelum nama variabel
        # Untuk variabel protected, cuma 1
        self.__nama= inputNama
        self.__jumlahKaki= 4
        self.__warna= None
        # Kalau ingin mendefinisikan warna di sini, maka: gantikan self.__warna dengan Kucing.setWarna(self, "warna apa")


    #setter
    def setWarna(self, inputWarna):
        self.__warna= inputWarna

    # Method private
    def __setWarna(self, inputWarna):
        pass

    #getter
    def getNama(self): return self.__nama
    def getWarna(self): return self.__warna
    def getJumlahKaki(self): return self.__jumlahKaki


persia= Kucing("persia")

# # Ini akan Error
# print(persia.nama)
# print(persia.__nama)

# Cara agar tidak error yaitu memakai method setter getter
print(persia.getNama())
print(persia.getWarna())
print(persia.getJumlahKaki())

# Untuk menyetel warna, kita memakai method set
persia.setWarna("Berkaki panjang")
print("\nMenyetel Warna kucing : "+persia.getWarna())