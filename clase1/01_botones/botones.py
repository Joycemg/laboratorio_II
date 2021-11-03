from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
# Intercambiar habilitacion de botones 

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("laboratorio_II/clase1/01_botones/botones.ui", self)
        self.boton1.clicked.connect(self.on_Click)
        self.boton2.clicked.connect(self.on_Click)

    def on_Click(self):
        if self.boton1.isEnabled() == True:
            self.boton1.setEnabled(False)
            self.boton2.setEnabled(True)
        else:
            self.boton2.setEnabled(False)
            self.boton1.setEnabled(True)


app = QApplication([])
win = MiVentana()
win.show()
app.exec_()