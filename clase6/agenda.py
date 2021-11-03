from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("laboratorio_II/clase6/agenda.ui", self)
        self.botonB.clicked.connect(self.on_Buscar)
        # Crear columnas
        self.tabla.setColumnCount(3)
        # Nombrar las Columnas
        self.tabla.setHorizontalHeaderLabels(['Nombre', 'Apellido', 'E-mail'])
        # Tamaño de la columna
        self.tabla.resizeColumnsToContents()
        self.tabla.horizontalHeader().setStretchLastSection(True)

        # Agregar fila en blanco
        self.tabla.insertRow(0)

        # Agregar Items de la fila
        self.tabla.setItem(0, 0,QTableWidgetItem('Pepe'))
        self.tabla.setItem(0, 1,QTableWidgetItem('Sanchez'))
        self.tabla.setItem(0, 2,QTableWidgetItem('Ps@mail.com'))

    def on_Buscar(self):
        self.tabla.findItems(self.buscador.text())
app = QApplication([])

win = MiVentana()
win.show()

app.exec_()