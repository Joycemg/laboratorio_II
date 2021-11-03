from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("laboratorio_II/clase5/22-10/mensajeBox.ui", self)
        self.button.clicked.connect(self.on_Mensaje)
    
    def on_Mensaje(self):
        msg = QMessageBox()
        msg.setWindowTitle('boenas')
        msg.setText('Te amo')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setIcon(QMessageBox.Warning)
        returnValue = msg.exec()
        if returnValue == QMessageBox.Ok:
            msg2 = QMessageBox()
            msg2.setText('TE  AMOAROBAR')
            msg2.exec()
    
app = QApplication([])

win = MiVentana()
win.show()

app.exec_()