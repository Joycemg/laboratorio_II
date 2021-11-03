from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("laboratorio_II/clase3/pizzas.ui", self)
        self.checkBox.clicked.connect(self.okey)
        self.checkBox_2.clicked.connect(self.okey)
        self.checkBox_3.clicked.connect(self.okey)
        self.pushButton.clicked.connect(self.calcu)
        self.total = 0

    def okey(self):
        total = 0
        if self.checkBox.isChecked():
            total += 20
        if self.checkBox_2.isChecked():
            total += 50
        if self.checkBox_3.isChecked():
            total += 10
        self.total = total
    def calcu(self):
        if self.total:
            self.totalText.setText(f'Precio extras: ${self.total}')

        else:
            self.totalText.setText('No ha elegido ningun extra')
app = QApplication([])

win = MiVentana()
win.show()

app.exec_()