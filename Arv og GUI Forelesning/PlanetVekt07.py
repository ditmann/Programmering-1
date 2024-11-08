import sys
from PyQt6.QtWidgets import QApplication, QWidget,QGridLayout, QLabel, QFormLayout, QComboBox, QDoubleSpinBox, QLineEdit, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIcon


planter = ["Merkur", "Venus", "Jorden", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun"]
tyngdegraft = [3.7,8.87,9.807,3.721,24.79,10.44,8.87,11.15]

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

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    vindu = Hovedvindu()
    sys.exit(app.exec())
