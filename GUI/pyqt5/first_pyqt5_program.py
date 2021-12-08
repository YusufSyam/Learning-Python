# Import modul
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def window():
   #  Membuat aplikasi dengan membuat objek QApplication yang parameternya sys.argv
   app = QApplication(sys.argv)

   # Membuat Widget yang sekarang menjadi top level window
   w = QWidget()

   # Menambahkan label pada widget w lalu menyetel text nya
   b = QLabel(w)
   b.setText("Hello World!")

   # Menyetel posisi dan ukuran window dengan set geometry
   w.setGeometry(100,100,200,50)

   # Memindahkan posisi label
   b.move(50,20)

   # Menyetel title gui
   w.setWindowTitle("PyQt5")
   w.show()

   # Menjalankan aplikasi (memasuki main loop) dengan sintaks di bawah
   sys.exit(app.exec_())

if __name__ == '__main__':
   window()