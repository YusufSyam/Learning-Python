# # FILE I/O python 3
#
# # Membuka file
# # Format: namaObjek= open('namaFile.ekstensi','mode')
#
# file= open("tesFile1.txt",'w')
# # Ada beberapa mode yang bisa digunakan
# # w= write mode -> menulis dan menghapus / menimpa file lama, jika file sudah ada, maka membuat file baru
# # r= read only -> hanya bisa membaca file
# # r+= write dan read mode
# # a (recommended)= appending mode -> menambahkan data di akhir baris, juga membuat file baru jika tidak ada,
# #  tapi jika sudah ada file, dia tidak menimpa
# # a+= appending dan reading
#
# # Untuk menulis di dalam file, kita menggunakan method write('isi string')
# file.write("Ini baris pertama dibuat dengan method write")
# file.write("\nIni kedua dibuat dengan method write")
#
# # Setelah yakin tidak menggunakan objek file, makan sebaiknya ditutup karena memakan memory
# file.close()
#
# # Untuk membaca file, kita menggunakan method read() atau readline(), yang mana
# # read() untuk membaca langsung keseluruhan file,  readline() membaca per halaman
# file2= open("tesFile1.txt",'r')
# print(file2.readline(), end='')
# print(file2.readline()) # Kalau mempunyai parameter integer, maka berarti parameter tersebut merupakan batas yang akan diprint
# # Kalau ingin membaca semua, pakai while
# # Membaca file dengan read() atau readline() seperti membuka buku, sekali lembar sebelumnya dibuka
# # maka lembar sebelumnya tidak bisa dibuka lagi, yang bisa dibuka hanya lembar selanjutnya
# file2.close()
#
# file21= open("tesFile1.txt",'r')
# # Membaca semua isi file dengan benar menggunakan while
# print()
# while(True):
#     line= file21.readline()
#     if not line:
#         break
#     print(line)
#
# # file3= open("filebaru.txt",'r')
# # print(file3.read().replace("###"," "))

file4= open("tesFile2.txt","a+")

while(True):
    choice= input("Masukkan permintaan:\n1. Write file\n2. Read file\n3. Close\n=> ")
    if(choice=="1"): file4.write("\n"+input("Menulis File..\nInput string untuk dimasukkan ke file tesFile2.txt : "))
    elif(choice=="2"):
        print("Membaca File..\n")
        # Gunakan method seek() saat ingin membaca file dengan mode a+
        file4.seek(0)
        while(True):
            line= file4.readline()
            if not line:
                break
            print(line, end='')
        print("\n")
    elif(choice=="3"):
        print("Menutup File..")
        file4.close()
        break
    else: print("Input salah")