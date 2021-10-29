#Muh. Yusuf Syam
#H071191044
#Tema = Library

from random import randint
import time
import datetime

daftarBuku= []
daftarPengunjung= []
daftarTanggal= []
log= ""


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

class Guest(User):
    daftarLog= {}

    def __init__(self, a, b):
        print(a)
        _nama= a
        _uang= 50000+(5000*randint(5, 20))
        print(a)

    def lihatRiwayatAktivitas(self, log):
        print("(Riwayat aktivitas di perpustakaan)")

        print(log)

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
        print(" Judul buku      : ",self.__judul)
        print(" Jenis buku      : ",self.__jenis)
        print(" Penulis         : ",self.__penulis)
        print(" Penerbit        : ",self.__penerbit)
        print(" Jumlah halaman  : ",self.__jumlahHalaman)

    def bacaBuku(self):
        print(" _____ ")
        print("|_|_|_| BUKU",self.__judul,"|_|_|_|")
        print(">",self.__isi)

###########################################################

pengunjung= User()

def main():
    setBuku()
    luarPerpustakaan()

def luarPerpustakaan():
    print(" _________________________________________________")
    print("|_|_|_|_|_|_|_|     PERPUSTAKAAN    |_|_|_|_|_|_|_|")
    print("||/            ---------------------            \||")
    print("|| 1. Masuk perpustakaan                         ||")
    print("|| 2. Keluar                                     ||")

    input1= input("> ")

    if(input1== "1"):
        tamuMasuk()
    elif (input1 == "2"):
        return
    else: print("> Input salah")

def tamuMasuk():
    tambahTanggal()
    input1= input("> Silahkan masukkan nama : ")
    print("> (INFO) riwayat aktivitas pengunjung dicatat perhari dan tidak disimpan")

    print(input1)
    print(setTanggal2())

    global pengunjung
    pengunjung= Guest(input1, setTanggal2())
    daftarPengunjung.append(input1)

    global log
    log= log+"-"+setWaktu2()+" -> Pertama kalinya memasuki perpustakaan\n"
    pengunjung.daftarLog[setTanggal2()]= log

    opsiUntukTamu()

def opsiUntukTamu():
    while (True):
        print("\n(Dalam perpustakaan) -> (Sebagai pengunjung)")
        print(" 1. Lihat daftar buku")
        print(" 2. Periksa detail buku")
        print(" 3. Baca buku")
        print(" 4. Lihat riwayat aktivitas")
        print(" 5. Lihat daftar pengunjung yang masuk perpustakaan hari ini")
        print(" 6. Keluar")

        input1= input("> ")
        print("\n")

        global log

        if (input1=="1"): lihatDaftarBuku()
        elif(input1=="2"): tamuPeriksaBuku(input1)
        elif(input1=="3"): tamuPeriksaBuku(input1)
        elif(input1=="4"):
            global pengunjung
            pengunjung.lihatRiwayatAktivitas(log)
        elif(input1=="5"): lihatDaftarPengunjung()
        elif(input1=="6"):
            print("> Keluar dari perpustakaan..")
            pengunjung = None
            daftarTanggal = []
            log = ""
            luarPerpustakaan()
            return

        else: print("> Input salah")

def opsiUntukAnggota():
    while (True) :
        print("\n(Dalam perpustakaan) -> (Sebagai member perpustakaan)")
        print(" 1. Lihat daftar buku")
        print(" 2. Periksa detail buku")
        print(" 3. Baca buku")
        print(" 4. Meminjam buku")
        print(" 5. Mengembalikan buku")
        print(" 6. Lihat riwayat aktivitas")
        print(" 7. Lihat daftar pengunjung yang masuk perpustakaan hari ini")
        print(" 8. Keluar")

        input1= input("> ")
        System.out.println()

        if (input1==("1")): lihatDaftarBuku()
        elif (input1==("2")): anggotaPeriksaBuku(input1)
        elif (input1==("3")): anggotaPeriksaBuku(input1)
        elif (input1==("4")): anggotaPinjamBuku()
        elif (input1==("5")): anggotaKembalikanBuku()
        elif (input1==("6")):
            if (tambahTanggal()==False):
                log= "";
                pengunjung.daftarLog[setTanggal2()]= ""

            pengunjung.lihatRiwayatAktivitas();

        elif (input1==("7")): lihatDaftarPengunjung()
        elif (input1==("8")) :
            tulisMember()
            print("> Keluar dari perpustakaan..")
            pengunjung= None
            daftarTanggal= []
            log= ""
            luarPerpustakaan()
            break
        else: print("> Input salah")

def lihatDaftarBuku():
    print(" _________                 _________")
    print("|_|_|_|_|_|  DAFTAR BUKU  |_|_|_|_|_|")

    if (len(daftarBuku) == 0):
        print("  -Kosong-")
    else:
        for i in range(len(daftarBuku)) :
            print("{:d}. {:s}".format((i+1), daftarBuku[i].getJudul()))

def tamuPeriksaBuku(input1):
    lihatDaftarBuku()

    input2= input("> Pilih buku : ")
    print("\n")

    a= int(input2)-1

    if(a<= len(daftarBuku) and input1=="2"):
        daftarBuku[a].detail()
    elif(a<= len(daftarBuku) and input1=="3"):
        daftarBuku[a].bacaBuku()
        global log
        log = log + "-" + setWaktu2() + " -> Membaca " + daftarBuku[a].getJudul() + "\n"
        pengunjung.daftarLog[setTanggal2()]= log
    else : print("> Input salah")

def lihatDaftarPengunjung():
    print("(Daftar pengunjung hari ini -",setTanggal2(),"- )")

    global daftarPengunjung
    if (tambahTanggal()==False) :
        daftarPengunjung= []
        daftarPengunjung.append(pengunjung.getNama())

    for i in range(len(daftarPengunjung)):
        print("{:d}. {:s}".format((i+1),(daftarPengunjung[i])))

def mendaftarJadiAnggota():
    if (checkName()==True):
        print("> : Anda merupakan seorang anggota, silahkan masuk sebagai anggota..\n")
        luarPerpustakaan()
        return


    print("> : Saat menjadi anggota, anda bisa meminjam buku di perpustakaan(biaya pendaftaran Rp. 30000)")
    print("> : Apakah anda ingin menjadi anggota perpustakaan? (y/n) : ")

    if(input()=="y"):
        if(pengunjung.membayar(30000)):
            pengunjung = pengunjung.menjadiMember()
            log = log,"-",setWaktu(),"-> Mendaftar menjadi anggota perpustakaan\n"
            pengunjung.daftarLog[setTanggal2()]= log

        print("> Selamat anda berhasil menjadi anggota!")
        print("> (INFO) riwayat aktivitas anggota dicatat perhari dan disimpan")
        print("> (INGAT) username- mu = ",pengunjung.getNama())
        print("> (INGAT) kata sandi perpustakaan = library124")
        opsiUntukAnggota();

    else:
        print("> Anda menolak menjadi anggota..")
        opsiUntukTamu()

def tambahTanggal():
    waktuSama= True

    if(len(daftarTanggal)==0):
        waktuSama= False
    else:
        for i in range(len(daftarTanggal)):
            if(setTanggal2()!=daftarTanggal[i]):
                waktuSama= False
            else:
                waktuSama= True
                break

    if(waktuSama==False):
        daftarTanggal.append(setTanggal2())

def setBuku():
    buku1 = Book("Harry Potter", "Novel ringan", "penulis 1", "Airlangga", 340)
    buku2 = Book("Percy Jackson", "Novel ringan", "penulis 2", "Airlangga", 280)
    buku3 = Book("Narnia", "Novel ringan", "penulis 3", "Penerbit novel", 275)
    buku4 = Book("Cara menghasilkan 1000$ tanpa keluar rumah", "Buku pelajaran", "penulis 4", "Airlangga", 1000)

    buku1.setIsi("Harry Potter..")
    buku2.setIsi("Percy Jackson..")
    buku3.setIsi("Narnia..")
    buku4.setIsi("Binomo..")

    daftarBuku.append(buku1)
    daftarBuku.append(buku2)
    daftarBuku.append(buku3)
    daftarBuku.append(buku4)

def setTanggal2():
    return datetime.date.today()

def setWaktu2():
    a = time.localtime()
    hr = a.tm_hour
    mn = a.tm_min
    return "{:d}:{:d}".format(hr, mn)



main()