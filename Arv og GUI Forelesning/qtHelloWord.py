import sys # man kan bruke kommandoer fra systemet
from PyQt6.QtWidgets import QApplication, QWidget #importerer noen spesifike ting fra QTWidgets siden det er så stort bibliotek

app = QApplication(sys.argv) #lager "applikasjonen"

vindu = QWidget()   # lager vinduer i applikasejonen 

vindu.setWindowTitle("hello world!!") 
vindu.resize(300,100)
vindu.move(700,300)


vindu.show()


sys.exit(app.exec())  #har med for å kunne stenge vinduet/at det kommer opp i det heletatt