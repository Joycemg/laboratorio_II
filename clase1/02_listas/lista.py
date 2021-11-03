from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog
from PyQt5 import uic
# Intercambiar habilitacion de botones 

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("laboratorio_II/clase1/02_listas/lista.ui", self)
        self.listas.itemClicked.connect(self.clickedL)
        # self.boton1.clicked.connect(self.on_Click)
        # self.boton2.clicked.connect(self.on_Click)


    def clickedL(self):
        self.label.setText(self.listas.currentItem().text())
        # if anterior:
        #     print(anterior.text())
        

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()