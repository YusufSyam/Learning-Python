print("\n---- print ----\n")
print("Uwau")

print("\n---- Print format ----\n")
iniString= "okalak"
intString2= "Itu python toh, tidak {}ji! wkwkw".format(iniString) #format string

arrayHewan= ["Kucing", "Mobil"]

print (intString2)
print ("{:>40}".format("Ini rata kanan (40 kolom)")) #rataan String
print ("{:^40}".format("Ini rata tengah (40 kolom)"))
print ("{:10}".format("Ini rata kiri"))

print ("{:s} : {:20d}".format("Rata kanan angka (20)",96))  #rata int
print ("{:s} : {:20.2f}".format("Rata kanan float (20)",96.12871))  #rata float
print ("{:.2f}".format(2.118713823)) #format angka

print("{iniString3} kekeke {ini}".format(iniString3= "Erere", ini= "Itu nda jelas skalii"))
print ("{k[1]}".format(k=arrayHewan)) #format array

print("---- Casting ----")

b= "1"
f= int(b)
k= bool(f)
b= str(f)

print ("{} {} {}".format(f, k, b))