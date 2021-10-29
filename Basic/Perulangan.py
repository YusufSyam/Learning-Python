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

# Perulangan dari belakang
for i in range(9, -1, -1): # = for(int i=9; i<=0; i++){}
    print (i)