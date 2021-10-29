# Menyambung / concatenate
namaPertama= "Yusuf"
namaAkhir= "Syam"
namaLengkap= namaPertama+" "+namaAkhir

print(namaLengkap)

# Menghitung panjang String (Dihitung mulai dari 1)
panjangNama= len(namaLengkap)
print(panjangNama)

# Membalik String
print(namaLengkap[::-1])

# Mengecek apakah ada suatu char/string dalam string (Tetap memperhatikan kapital)
# contoh mengecek apakah ada huruf f dalam nama lengkap
cariHuruf= "d" in namaLengkap
print(cariHuruf)
print("yam" in namaLengkap)
print("sufyam" not in namaLengkap)
print()

# index dari sebuah char dalam string (Mulai dari 0)
print("Indeks ke 2 dari nama Lengkap adalah {}".format(namaLengkap[2]))

# Kalau index bernilai negatif, maka dihitung mulai dari belakang
print("Indeks ke -2 dari nama Lengkap adalah {}".format(namaLengkap[-2]))

# Kalau ada 2 index (0:3), maka yang diambil adalah index 0 sampai 2
print("Indeks ke 0 sampai 5 dari nama Lengkap adalah {}".format(namaLengkap[0:5]))

# Kalau mau print tapi meloncat, gunakan 3 argumen, contoh: string[index awal, index akhir, increment]
print("Index yang genap : {}".format(namaLengkap[0:len(namaLengkap):2]))

# Mengulang string
print("Wk"*10)

# Mencari huruf paling besar dari sebuah string (berdasarkan ascii table)
print(max(namaLengkap))
print(min(namaLengkap)) #Kalau ada char spasi dalam string, maka yang keluar adalah char spasi, karna ia terkecil

# Mencari jumlah sebuah char dalam sebuah string
# Contoh: Mencari jumlah char 'u' dalam nama lengkap
print(namaLengkap.count("u"))

# Merubah string menjadi kapital / kecil
print(namaLengkap.upper())
print(namaLengkap.lower())
# Ingin mengecek sebuah string kapital/kecil semua? pakai isUpper atau isLower

# Mengecek string mengandung string, angka, dll
# Mengecek string semuanya huruf
print(namaLengkap.isalpha())
# Mengecek string mengandung huruf DAN angka
print(namaLengkap.isalnum())
# Mengecek string angka saja
print(namaLengkap.isdecimal())
# Mengecek string berisi cuma spasi / tab / \n atau newline
print(namaLengkap.isspace())
# Mengecek semua kata string dimulai dari huruf besar
print(namaLengkap.istitle())

# Mengecek apabila sebuah string diawali / diakhiri string tertentu (tidak terbatas pada kata)
print(namaLengkap.startswith("Yus"))
print(namaLengkap.endswith("usuf Syam"))