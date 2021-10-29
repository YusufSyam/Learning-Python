import numpy as np

# Membuat variabel bernilai random
a= np.random.rand() # Jika hanya begini akan menggenerate float dari 0-1
print('a= ',a)

# Membuat variabel bernilai random berbentuk integer, parameter wajib adalah low
# Jika parameter hanya satu yaitu low, maka low berarti adalah batas nilai tertinggi (menggantikan fungsi high), karena default high adalah None
# Jika kita juga mengisi high, maka fungsi low akan kembali seperti awal, menjadi batas bawah
b= np.random.randint(low=20)
print('b= ',b)

c= np.random.randint(low=20, high=30)
print('c= ',c)

# Membuat list angka random, cukup menambahkan parameter size
d= np.random.randint(10,30, size=10)
print(d)