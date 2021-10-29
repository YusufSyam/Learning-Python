# Misal kita ingin merubah suatu fungsi method
# Kita menggunakan decoration


class Player:

    __jumlah= 0 # <-- Variabel static

    def __init__(self, inputNama, inputHealth):
        self.__nama= inputNama
        self.__health= inputHealth
        self.__attack= None
        Player.__jumlah+=1
        # self.info= "Nama= {} Health= {}".format(self.__nama,self.__health)

    # Method yang hanya berlaku untuk class tapi tidak berlaku untuk objek
    # Adalah dengan cara kita tidak memberikan argumen self di parameter
    def getJumlah1():
        return Player.__jumlah

    # Method yang berlaku untuk keduanya, class dan objek
    # Menggunakan decoration @staticmethod
    @staticmethod
    def getJumlah2():
        return Player.__jumlah

    # Bisa juga menggunakan decoration @classmethod
    @classmethod
    def getJumlah3(iniBisaBernamaApapun): # parameter di sini menerapkan metode polimorfisme
        return iniBisaBernamaApapun.__jumlah


    # (Tidak perlu dibaca serius kalau bingung) Kalau kita mengubah suatu variabel misalnya nama, maka
    # Informasi yang berada di atribut info tidak akan berubah, maka dibutuhkan method dengan property
    # Misal kita ingin method menjadi sebuah variabel, kita menggunakan decoration @property
    @property
    def showInfo(self):
        return "Nama= {} Health= {}".format(self.__nama, self.__health)

    # Membuat method setter / getter menjadi seperti variabel
    # Misal kita ingin membuat setter getter dari variabel private __attack
    # Maka untuk setter kita menambahkan decoratio @namaVariabel.setter = @attack.setter

    # Untuk melakukan hal tersebut kita mendefinisikan sebuah method dengan nama yang
    # sama (sebenarnya bebas) dengan atribut yang ingin dibuatkan setter getter nya dengan decoration @property
    @property
    def attack(self):
        pass

    @attack.setter
    def setAttack(self, attack):
        self.__attack= attack

    @attack.getter
    def getAttack(self):
        return self.__attack

player1= Player("Yusuf","100")

# Saat ingin mengambil info, kita tidak memakai (), karena itu merupakan variabel bukan method
print(player1.showInfo)

# Akan error
# print(player1.getJumlah1())

# Tidak error
print(Player.getJumlah1())
print(Player.getJumlah2())
print(player1.getJumlah2())
print(Player.getJumlah3())
print(player1.getJumlah3())

print()

# Setter dan getter dengan decoration property

# Terlihat setter dan getter dari player seperti tanpa enkapsulasi, namun sebenarnya
# Itu berkat dari decoration setter dan getter
player1.setAttack= 10
print(player1.getAttack)