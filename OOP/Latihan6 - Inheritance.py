# --------- Inheritance biasa --------- #
class Hewan:

    def __init__(self, nama, warna):
        self.nama= nama
        self.warna= warna

# Untuk membuat class anak dari class A, saat membuat kelas,
# Masukkan nama class parents di dalam kurung\

class Reptil(Hewan): # <-- Ini berarti Reptil menurunkan sifat2 (method dan atribut) dari class Hewan
    pass

class Unggas(Hewan):
    pass


Ayam= Unggas("Yusuf","biru")
Buaya= Reptil("Fakboy","hijau")
# print(help(Ayam))
print(Ayam.nama)

# --------- Multiple Inheritance ---------- #
# Yaitu class yang mempunyai dua atau lebih induk

class Team:
    def setTeam(self, team):
        self.team= team

class Tipe:
    def setTipe(self, tipe):
        self.tipe= tipe

# Di sini, kelas Hero mewariskan dua kelas sekaligus
class Hero(Team,Tipe):
    def __init__(self, name, health):
        self.name= name
        self.health= health

Yusuf= Hero("Yusuf",100)
Yusuf.setTeam("Merah") # Menggunakan method dari class Team
Yusuf.setTipe("The Gamer") # Menggunakan method dari class Tipe

print(Yusuf.team)