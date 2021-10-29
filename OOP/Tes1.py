class A:
    def __init__(self):
        print("Ini Constructor A")

class B(A):
    def __init__(self):
        print("Ini Constructor B")

class C(B):
    def __init__(self):
        print("Ini Constructor C")

tes= C()

# Jadi bisa disimpulkan, construction (atau method-method lainnya) secara automatis mengoverride method yang sama dari induk

class D:
    def __init__(self):
        print("Ini Constructor D")

class E(D):
    def __init__(self,nama):
        print("Ini Constructor E bernama",nama)

tes2= E("yusuf")

# Tetap tidak menjalankan constructor dari kelas induk walaupun method nya mempunyai parameter berjumlah beda