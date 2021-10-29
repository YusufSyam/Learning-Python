# Menggabungkan semua komponen dari suatu list
# Syaratnya list harus berisi hanya string
listKata= ["Aku","sayang","Jihyo","3000"]
# Sebelum .join kita mengisi string apa yang menjadi pemisah antara elemen map
gabunganListKata= ' '.join(listKata)
print(gabunganListKata)

# Memisahkan / split String berdasarkan string lain
x= "AKU###$$$kuarSayang###$$$kuarKamu###$$$kuar:)"
print(x.split("###$$$kuar"))

# Memperbaiki hasil print string x
print(' '.join(x.split("###$$$kuar")))
print()

stringX= "Muh%^!$@^%^&99Yusuf%^!$@^%^&99Syam"
print(stringX)
listDariStringX= stringX.split("%^!$@^%^&99")
print(listDariStringX)
print(' '.join(listDariStringX))

# Mereplace suatu string dengan string di dalam string
print("Memperbaiki stringX dengan replace")
print(stringX.replace("%^!$@^%^&99"," "))

# Rata / Justify String
kanan= "kanan".rjust(20) # Berarti ke kanan dengan 20 spasi
print("Rata kanan: '{}'".format(kanan))

kiri= "kiri".ljust(20,"-") # Berarti rata kiri dan spasi diubah menjadi parameter kedua yaitu '-'
print(kiri)

tengah= "tengah".center(21, ".") # karena jumlah spasi ganjil, maka seblah kiri 11 kanan 10
print(tengah)

print()

# Menghilangkan suatu string / char dalam string tapi hanya pada di awal / akhir
print("Memprint tengah tadi tanpa titik: "+tengah.strip("."))

stringAneh= "AKU Aneh denganlalala"
print(stringAneh.strip("denganlalala"))