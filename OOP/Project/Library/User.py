from random import randint
#import Main as Main
import time
import datetime

class User:
    _nama= ""
    _uang= 0
    _indeks= -1

    daftarLog= {}
    bukuDipinjam= []

    def setIndeks(self, a):
        self._indeks= a

    def getNama(self): return self._nama
    def getUang(self): return self._uang
    def getIndeks(self): return self._indeks
    def getBukuDipinjam(self):
        semuaJudul= ""
        for i in range(len(self.bukuDipinjam)):
            semuaJudul+= (self.bukuDipinjam[i].getJudul()+"#-#")
            semuaJudul+= (self.bukuDipinjam[i].getWaktuPengembalian()+"#-#")
        return semuaJudul

    def membayar(self, bayar):
        if(self._uang-bayar>=0):
            self._uang-= bayar
            return True
        else: return False

    def menjadiMember(self):
        return Member(self._nama, self._uang, self.daftarLog)

    def setTanggal(self):
        return datetime.date.today()+""

    def setWaktu(self):
        a = time.localtime()
        hr = a.tm_hour
        mn = a.tm_min
        return "{:d}:{:d}".format(hr,mn)

class Member(User):

    def __init__(self, nama2, uang2):
        self.__nama= nama2
        self.__uang= uang2

    def __init__(self, nama2, uang2, daftarLog2):
        self._nama= nama2
        self._uang= uang2
        self.__daftarLog= daftarLog2

    def lihatRiwayatAktivitas(self):
        print("(Riwayat aktivitas di perpustakaan)")

        for i in range(len(Main.daftarTanggal)):
            print("{:d}. {:s}".format((i+1),Main.daftarTanggal[i]))

        inputString= input("> Pilih tanggal : ")
        indeksTanggal= int(inputString)-1

        if(daftarLog[Main.daftarTanggal[indeksTanggal]]==null or len(daftarLog[Main.daftarTanggal[indeksTanggal]])==0):
            daftarLog[Main.setTanggal()]= "-Tidak Melakukan Apapun-"

        print(daftarLog[Main.daftarTanggal[indeksTanggal]])

class Guest(User):

    def __init__(self, a, b):
        print(a)
        _nama= a
        _uang= 50000+(5000*randint(5, 20))
        print(a)

    def lihatRiwayatAktivitas(self):
        print("(Riwayat aktivitas di perpustakaan)")

        if(len(daftarLog)==0):
            print(" -Anda belum melakukan apapun-")
            daftarLog[setTanggal()]= "-Tidak melakukan apapun-"
            return

        if(daftarLog[setTanggal()]== null):
            daftarLog[setTanggal()] = "-Tidak melakukan apapun-"

        print(daftarLog[setTanggal()])

class Book:
    def __init__(self, a, b, c, d, e):
        self.__judul= a
        self.__jenis= b
        self.__penulis= c
        self.__penerbit= d
        self.__jumlahHalaman= e

    def setIsi(self, a):
        self.__isi= a

    def setWaktuPengembalian(self, a):
        self.__waktuPengembalian= a

    def getWaktuPengembalian(self):
        return self.__waktuPengembalian

    def getJudul(self):
        return self.__judul

    def detail(self):
        print(" _________                 _________")
        print("|_|_|_|_|_|  DETAIL BUKU  |_|_|_|_|_|")
        print(" Judul buku      : " + __judul)
        print(" Jenis buku      : " + __jenis)
        print(" Penulis         : " + __penulis)
        print(" Penerbit        : " + __penerbit)
        print(" Jumlah halaman  : " + __jumlahHalaman)

    def bacaBuku(self):
        print(" _____ ")
        print("|_|_|_| BUKU",__judul,"|_|_|_|")
        print(">",__isi)




