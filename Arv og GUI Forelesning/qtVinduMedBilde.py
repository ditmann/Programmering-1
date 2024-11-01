import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap


#klasse som arver fra QWidget:
class Vindu(QWidget):
    def __init__(self,):
        super().__init__()
        self.setWindowTitle("enkelt vindu")
        self.resize(300,300)

        label1 = QLabel()
        label1.setText("Hello World")
        
        labelImg = QLabel()
        pixmap = QPixmap("gmaer.jpg")
        labelImg.setPixmap(pixmap)

app = QApplication(sys.argv)

vindu = Vindu()
vindu.show()

sys.exit(app.exec())
