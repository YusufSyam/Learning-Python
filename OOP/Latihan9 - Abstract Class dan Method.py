# Saat ingin memakai abstract class, kita mengimportnya terlebih dahulu
from abc import ABC, abstractmethod

class Tombol:
    def __init__(self, onClick, link):
        self._onClick= onClick
        self.link= link

    @abstractmethod
    def tertekan(self): # <-- Merupakan abstract method yang memaksa semua kelas anak mengimplementasikannya
        pass

    # Bagaimana memaksa agar link harus diisi di kelas anak?
    @property
    @abstractmethod
    def link(self):
        pass

class RadioButton(Tombol):
    def tertekan(self):
        print(self._onClick)

    def redirect(self):
        print("Redirect ke:",self.link)

    @Tombol.link.setter
    def link(self, input):
        self.__link= input

    @link.getter
    def link(self):
        return self.__link

    # Jujur, ini 2 method di atas sama method terakhir kelas induk masih belumpi terlalu kumengerti

objekTombol= RadioButton("Radio Button Terpencet!","googel")
objekTombol.tertekan()
objekTombol.redirect()

