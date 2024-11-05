import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

#vertikalt

class Hovedvindu(QWidget):
    def __init__(self):
        super().__init__()
                        #fra venstre, fra toppen, bredde, høyde
        self.setGeometry(900, 200, 300, 100)

        self.setWindowTitle("QWBoxLayout-test")
        layout = QVBoxLayout()
        self.setLayout(layout)

        #det finnes 2 måter å sette navn på knapper        
        button1 = QPushButton("knapp 1")
        button2 = QPushButton()
        button2.setText("knapp 2")
        button3 = QPushButton("knapp 3")

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addStretch()
        layout.addWidget(button3)

        layout.setSpacing(12)
        layout.setContentsMargins(70,70,70,70)


        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    vindu = Hovedvindu()

    sys.exit(app.exec())

