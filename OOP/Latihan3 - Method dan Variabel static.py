class Orang:

    # Variabel static, merupakan variabel yang tidak terikat pada object
    # Melainkan pada class,  namun saat ingin dipakai, harus diikuti dengan namaClass.variabel static
    jumlahTindakan= 0
    def __init__(self, inputNama, inputUmur):
        self.nama= inputNama
        self.umur= inputUmur
        self.health= 100

    def jalan(self):
        self.health-=10
        print(self.nama+" berjalan...")
        Orang.jumlahTindakan+=1

    def memukul(self, objekOrang):
        print(self.nama+" memukul "+objekOrang.nama+"...")
        objekOrang.health-=20
        Orang.jumlahTindakan+=1

yusuf= Orang("Yusuf",19)
print(yusuf.health)

yusuf.jalan()
print("Darah yusuf:",yusuf.health)
print("Jumlah tindakan yang dilakukan orang orang:",Orang.jumlahTindakan)

print()

alif= Orang("alif",20)
yusuf.memukul(alif)

print("Darah alif:",alif.health)
print("Jumlah tindakan yang dilakukan orang orang:",Orang.jumlahTindakan)