import sys
from PyQt6.QtWidgets import QApplication, QWidget,QGridLayout, QLabel, QFormLayout, QComboBox, QDoubleSpinBox, QLineEdit, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIcon


planeter = ["Merkur", "Venus", "Jorden", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun"]
tyngdegraft = [3.7,8.87,9.807,3.721,24.79,10.44,8.87,11.15]
planetBilder = ["Merkur.png", "Venus.png", "Jorden.png", "Mars.png", "Jupiter.png", "Saturn.png", "Uranus.png", "Neptun.png"]


class Hovedvindu(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Planet vekt")
        self.setGeometry(500,100,500,400)


        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.topplabel = QLabel()
        self.topplabel.setText("Hva er din vekt på andre planeter")
        self.layout.addWidget(self.topplabel,0,0,1,2, alignment = Qt.AlignmentFlag.AlignCenter)

        self.skjema = QFormLayout()
        self.menyCombobox = QComboBox()
        self.menyCombobox.setPlaceholderText("Velg en planet")
        self.menyCombobox.addItem("Tifeldig planet")
        for planet in planeter:
            self.menyCombobox.addItem(planet)

        self.menyCombobox.activated.connect(self.oppdaterBilde())
        self.skjema.addRow(self.menyCombobox)

        

        self.vektInput = QDoubleSpinBox()
        self.vektInput.setPrefix("Din vekt i KG:                           ")
        self.vektInput.setDecimals(1)
        self.skjema.addRow(self.vektInput)

        self.regnutknapp = QPushButton("Regn ut")
        self.skjema.addRow(self.regnutknapp)


        self.layout.addLayout(self.skjema,1,0)

        self.bildelabel = QLabel()
        self.pixmap = QPixmap("sun.png")
        self.pixmap = self.pixmap.scaled(256,256)
        self.bildelabel.setPixmap(self.pixmap)

        self.layout.addWidget(self.bildelabel, 1,1)

        self.bunnLabel= QLabel("Velg en planet og skriv inn vekten din!")
        self.layout.addWidget(self.bunnLabel,2,0,1,2, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.show()
    
    def oppdaterBilde(self):
        self.pixmap = QPixmap


if __name__ == "__main__":
    app = QApplication(sys.argv)
    vindu = Hovedvindu()
    sys.exit(app.exec())
