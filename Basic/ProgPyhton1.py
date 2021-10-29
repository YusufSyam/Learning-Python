

iniSalah= False

print("\n---- pengondisian ----\n")
if iniSalah : #sintaks if else
    print ("Erere\nini if")
else :
    print ("Bakuvi")
    print ("Ini else")

print("\n---- perulangan ----\n")
for i in range (3): #perulangan
    print ("ini i", str(i)) #cast int ke string, kalau pake '+' tidak spasi, kalau pake ',' auto spasi
    for j in range (3):
        print ("ini j "+ format(j)) #printf
        if j==i :
            print ("J = I")
    if (i==2): print ("\nini akhir dari for\n") #bisa juga dikasi begini

a= 0

print("\n---- perulangan (while) ----\n")
while(True):
    a+=1
    print ("Ini while ke-",a) #Ternyata kalau pake '+' harus string
    if a==2 : print ("Ini while ke- "+str(a)+" lagi") #Tapi kalo begini bisa
    if a==5 : break

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

