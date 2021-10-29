print("\n---- Scanner/input ----\n")
input() #iniScanner
iniNama= input("Masukkan nama : ") #Bisa juga begini

if (input("Masukkan 'uwau': ") == "uwau") :
    print ("Kamu memasukkan uwau! Chukkaee")
elif (iniNama == "Yusuf") :
    print ("Namamu "+iniNama+" !")
else : print ("Kamu tidak memasukkan uwauu :(((")

#Input integer

inputInteger= int(input())
print("Hasil : ",(inputInteger+2))

#Input hanya string - Lengkapi pakek while
s = input("Enter your name: ")
if not s.isalpha():
    print("Please enter only alphabetical characters for your name.")

#Input di baris bersamaan
x, y = input("Enter a two value: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
print()

#Input Map
a,b,c = map(float, input().split())