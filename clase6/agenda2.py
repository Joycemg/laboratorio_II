from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox, QFileDialog
from PyQt5 import uic
import csv

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("laboratorio_II/clase6/agenda.ui", self)
        self.botonAgregar.clicked.connect(self.on_Agregar)
        self.botonEliminar.clicked.connect(self.on_Eliminar)
        self.botonGuardar.clicked.connect(self.on_Guardar)
        self.botonCargar.clicked.connect(self.on_Cargar)
        # Pop mensaje
        self.msg = QMessageBox()
        self.msg.setWindowTitle('Error')
        self.msg.setIcon(QMessageBox.Warning)

        # Contador de filas
        self.countRow = 0

        # Crear columnas
        self.tabla.setColumnCount(3)

        # Nombrar las Columnas
        self.tabla.setHorizontalHeaderLabels(['Nombre', 'Apellido', 'E-mail'])

        # Tamaño de la columna
        self.tabla.resizeColumnsToContents()
        self.tabla.horizontalHeader().setStretchLastSection(True)

    def borrado(self):
        self.nombre.clear()
        self.apellido.clear()
        self.email.clear()

    def on_Agregar(self):
        nombre = self.nombre.text()
        apellido = self.apellido.text()
        email = self.email.text()
        if nombre and apellido and email:
            self.tabla.insertRow(self.countRow)
            self.tabla.setItem(self.countRow, 0,QTableWidgetItem(self.nombre.text()))
            self.tabla.setItem(self.countRow, 1,QTableWidgetItem(self.apellido.text()))
            self.tabla.setItem(self.countRow, 2,QTableWidgetItem(self.email.text()))
            self.borrado()
            self.countRow += 1
            print(self.countRow)
        else:
            self.msg.setText('Los campos no estan completos.')
            self.msg.exec()

    def on_Eliminar(self):
        selec = self.tabla.currentRow()
        if self.tabla.rowCount() > 0 and self.tabla.selectedItems():
            self.tabla.removeRow(selec)
            self.countRow = self.tabla.rowCount()
        else:
            self.msg.setText('No hay nada seleccionado')
            self.msg.exec()

    def on_Guardar(self):    
        save = QFileDialog.getSaveFileName(self,  
                                    "Guardar archivo",  
                                    "/home/joyce/Documentos/programacion/laboratorio_II/clase6", # Ruta de inicio 
                                    "CSV Files (*.csv)",  options=QFileDialog.DontUseNativeDialog)
        if save[0] == '':
            return 0
        if save[1] == 'CSV Files (*.csv)' and not '.csv' in save[0]:
            save = save[0] + '.csv'
        else:
            save = save[0]
        file = open(save, 'w')
        escritor_csv = csv.writer(file, delimiter=',', quotechar='"')
        for row in range(self.tabla.rowCount()):
            items = self.tabla.item(row, 0).text(),self.tabla.item(row, 1).text(),self.tabla.item(row, 2).text()
            escritor_csv.writerow(items)
        file.close()

    def on_Cargar(self):

        load = QFileDialog.getOpenFileNames(self,  
                                    "Cargar archivo",  
                                    "/home/joyce/Documentos/programacion/laboratorio_II/clase6", # Ruta de inicio 
                                    "CSV Files (*.csv)",  options=QFileDialog.DontUseNativeDialog)
        if len(load[1]) == 0:
            return 0
        else:
            self.tabla.clearContents()
            self.countRow = 0
            self.tabla.setRowCount(self.countRow)
            archivo = open(''.join(load[0]))
            lector_csv = csv.reader(archivo)

            for y in lector_csv:
                self.tabla.insertRow(self.countRow)
                for i in range(3):
                    self.tabla.setItem(self.countRow, i,QTableWidgetItem(y[i]))
                self.countRow += 1



app = QApplication([])

win = MiVentana()
win.show()

app.exec_()