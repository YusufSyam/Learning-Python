class Pegawai:
    def __init__(self, nama):
        self.__nama= nama
        self._gaji= Pegawai.setGaji(self)

    def setGaji(self): return 2500000

    def getGaji(self): return self._gaji

    def getNama(self): return self.__nama

class Dosen(Pegawai):
    def __init__(self, nama, sks):
        self.__nama= nama
        self.__sks= sks
        self.__gaji= super().setGaji()

    def getGaji(self): return self.__gaji+(self.__sks*120000)

    def getNama(self): return self.__nama

class Staff(Pegawai):
    def __init__(self, nama, kehadiran):
        self.__nama = nama
        self.__kehadiran = kehadiran
        self.__gaji = super().setGaji()

    def getGaji(self): return self.__gaji+(self.__kehadiran*50000)

    def getNama(self): return self.__nama


pegawai= []

pegawai.append(Staff(input("Nama Staf ::> "),int(input("Jumlah Kehadiran ::> "))))
pegawai.append(Dosen(input("Nama Dosen ::> "),int(input("Jumlah SKS ::> "))))
pegawai.append(Pegawai(input("Nama Pegawai ::> ")))

for i in range(len(pegawai)): print("{} mendapatkan gaji Rp. {}".format(pegawai[i].getNama(),pegawai[i].getGaji()))
