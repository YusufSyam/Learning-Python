print("\n---- Array/List ----\n")
arrayHewan= ["Kucing", "Mobil", "Kucang"]

for i in range(len(arrayHewan)): #fungsi len() untuk mengembalikkn panjang array
    print (i+1) ; print (arrayHewan[i]) #kalo mau 2 statement, bisa pakek ';'

print()

#Bisa juga begini
for i in arrayHewan:
    print (i)

#Array/list bisa berbeda tipe datanya
arrayBedaTipeData= ["String", 1, True, 0.43]

for i in range(len(arrayBedaTipeData)):
    print (arrayBedaTipeData[i])

print("menambah data..")

#Dalam array, kita bisa menambah data dengan 3 method

arrayBedaTipeData.append(3)
#append(), menambah data dari belakang

arrayBedaTipeData.insert(2, "Ini jadi ke-2")
#insert(i, data), memasukkan data sesuai indeks

arrayBedaTipeData.remove(3)
del arrayHewan[2]
#remove(), atau del[], untuk menghapus data
#Sekarang array jadinya seperti ini
for i in range(len(arrayBedaTipeData)):
    print (arrayBedaTipeData[i])

#List bisa ditambah, dikali, dan dipotong

listAngka1= [1, 2, 3, 4, 5, 6]
listAngka2= [7, 8, 9, 10]

#Menjumlahkan list
listAngkaAll= listAngka1+listAngka2
print ("Hasil penjumlahan list :", listAngkaAll)

#Meng-kali list
listAngka2 *= 3
print ("List 2 dikali 3 : ", listAngka2)

#Memotong list
print ("List Angka setelah dipotong bersisa 5 angka, = ", listAngka1[0:5]) #berarti menyisakan hanya indeks 0,1,2,3,4
#Nda tau kenapa enda bisa, jadi kukomen ki

# list= []
# list.append(2)
# print (list[0])

# arr= []
#
# for i in range(3):
#     col= []
#     for j in range(3):
#         col.append(int(input()))
#     arr.append(col)