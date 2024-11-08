import sys
from PyQt6.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QPushButton

class Hovedvindu(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("oppmeldingsskjema")

        layout = QFormLayout()
        self.setLayout(layout)

        layout.addRow("navn:", QLineEdit(self))
        layout.addRow("Epost", QLineEdit(self))
        layout.addRow("passord", QLineEdit(self, echoMode = QLineEdit.EchoMode.Password))
        layout.addRow("gjenta Passord", QLineEdit(self, echoMode = QLineEdit.EchoMode.Password) )
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    vindu = Hovedvindu()

    sys.exit(app.exec())
