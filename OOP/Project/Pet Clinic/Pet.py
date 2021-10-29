import random

class Pet:
    def __init__(self, jenis):
        self.__nama= input("Masukkan nama pada "+jenis+" baru anda: ").title()
        self.__umur= str(random.randint(1,10))+" Tahun"
        self.__jenis= jenis
        if(jenis=="Kucing" or jenis=="Anjing" or jenis=="Kambing" or jenis=="Hamster"): self.__jumlahKaki= 4
        elif(jenis=="Ayam" or jenis=="Bebek" or jenis=="Burung"): self.__jumlahKaki= 2
        randomSifat= random.randint(1,10)
        if(randomSifat<=3): self.__sifat= "Ceria"
        elif(randomSifat<=5): self.__sifat= "Pemalu"
        elif(randomSifat<=7): self.__sifat= "Pemalas"
        elif(randomSifat<=9): self.__sifat= "Bersemangat"
        elif(randomSifat==10): self.__sifat= "Pemarah"

    def showInfo(self):
        print("Hewan Peliharaan {}:\n Nama\t\t: {}\n Umur\t\t: {}\n Sifat\t\t: {}\n Jumlah Kaki\t: {}".format(self.__jenis, self.__nama, self.__umur, self.__sifat, self.__jumlahKaki))