import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class Hovedvindu(QWidget):
    def __init__(self):
        super().__init__()

        #endrer på hvordan vinduet skal vises,
        self.setWindowTitle("tester knappebinning")
        self.setGeometry(100,100,300,100)

        #lager en boks som alt skal være inni
        layout = QVBoxLayout()
        self.setLayout(layout)

        #lager objekter som skal plasseres
        knapp = QPushButton("Min kanpp")

        #knytter kanppent til en funksjon
        knapp.clicked.connect(self.knappTrykket)

        # viser knapper som er laget
        layout.addWidget(knapp)
        
        self.show()
    
    
    def knappTrykket(self):
        print("knappen ble trykket")

    

if __name__ == "__Main__":
    app = QApplication(sys.argv)

    vindu = Hovedvindu()
    
    sys.exit(app.exec)