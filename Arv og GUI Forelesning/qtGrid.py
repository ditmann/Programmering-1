import sys
from PyQt6.QtWidgets import*

class hovedvindu(QWidget):
    def __init__(self):
        super().__init__()


        self.setGeometry(800,200,600,600)

        layout = QGridLayout()
        self.setLayout(layout)

        minLabel = QLabel()
        minLabel.setText("Gamer")
        layout.addWidget(minLabel,0,0)

        minKnapp = QPushButton("knapp")
        layout.addWidget(minKnapp,0,1)

        minInputLinje = QLineEdit()
        minInputLinje.setPlaceholderText("gi meg tekst!!")
        layout.addWidget(minInputLinje,0,2)

        minRadioknapp = QRadioButton("radioknapp")
        layout.addWidget(minRadioknapp,1,0)

        minSjekkboks = QCheckBox("Avkrysse boks")
        layout.addWidget(minSjekkboks,1,1)

        minCombobox = QComboBox()
        minCombobox.setPlaceholderText("velg kun ett av alternativene")
        minCombobox.addItem("gaming")
        minCombobox.addItem("gamers")
        layout.addWidget(minCombobox,1,2)


        minTekst = QTextEdit()
        minTekst.setPlaceholderText("brukerinput, flere linjer")
        layout.addWidget(minTekst,2,0)

        minBeskjed = QMessageBox()
        minBeskjed.setText("dette er en beskjed til deg")
        layout.addWidget(minBeskjed,2,1)

        minSlider = QSlider()
        minSlider.setRange(10,80)
        layout.addWidget(minSlider,2,3)


        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)

    vindu = hovedvindu()

    sys.exit(app.exec())

