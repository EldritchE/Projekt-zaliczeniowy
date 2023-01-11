import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

# Utwórz aplikację
app = QApplication(sys.argv)

# Utwórz okno
window = QWidget()
window.setWindowTitle("Możliwości GUI")

# Utwórz etykietę
label = QLabel("Witaj w oknie GUI!", window)
label.move(50, 50)


# Utwórz przycisk
def klik():
    print("Kliknięto przycisk!")
    label = QLabel("KLIKNIETO!!!", window)


button = QPushButton("Kliknij mnie", window)
button.move(50, 100)
button.clicked.connect(klik)

# Pokaż okno
window.show()

# Uruchom pętlę aplikacji
sys.exit(app.exec_())
