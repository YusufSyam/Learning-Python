# Magic method pada class

class Hewan:

    # 1. Magic Method __init__ (Constructor)
    def __init__(self, nama):
        self.__nama= nama

    # 2. Magic Method __repr__
    # Merupakan method yang dijalankan saat nama objek saja yang diprint/dipanggil
    # Isi default dari __repr__ adalah tempat alokasi objek di memori
    def __repr__(self):
        return "INI ADALAH METHOD __REPR__ DARI HEWAN "+self.__nama

    # 3. Magic Method __str__, __str__ sama dengan __repr__
    # Tapi orang2 mengatakan kalau saat debug sebaiknya gunakan __repr__, saat program sudah jadi gunakan __str__
    def __str__(self):
        return "INI ADALAH METHOD __STR__ DARI HEWAN " + self.__nama

    # 4. Magic Method __dict__ yang biasa kita gunakan untuk mau melihat ke dalam objek

Yusuf= Hewan("Yusuf")
print(Yusuf)
# Saat didefinisikan keduanya method __str__ dan __repr__
# Yang dijalankan adalah __str__
# Kalau hanya ingin __repr__ atau __str__ yang dijalankan, maka tuliskan begini:
print(repr(Yusuf))
print(str(Yusuf))