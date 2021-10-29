a= int(input("Masukkan Angka:")); prm= True
for i in range(2,int(a/2+1)):
    if(a<0 or a%i==0):
        print(a,"bukan bilangan prima")
        break
print(a,"bilanngan prima")