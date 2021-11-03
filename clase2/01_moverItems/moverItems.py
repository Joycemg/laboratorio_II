from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog, QMessageBox
from PyQt5 import uic
from PyQt5 import QtCore

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("laboratorio_II/clase2/01_moverItems/intercambio.ui", self)
        self.botonAgregar.clicked.connect(self.on_agregar)
        self.boton_MoverD.clicked.connect(self.on_moverD)
        self.boton_MoverI.clicked.connect(self.on_moverI)
        self.botonEditar.clicked.connect(self.on_editar)
        self.boton_Eliminar.clicked.connect(self.on_quitar)


    def keyPressEvent(self, qKeyEvent):
        print(qKeyEvent.key())
        if qKeyEvent.key() == QtCore.Qt.Key_Return: 
            print('Enter pressed')
            self.on_agregar()
        else:
            super().keyPressEvent(qKeyEvent)
            
    def on_agregar(self):
        if self.display.text().strip():
            self.listA.addItem(self.display.text().strip())
            self.display.setText('')

    def on_moverD(self):
        try:
            self.listB.addItem(self.listA.currentItem().text())
            self.listA.takeItem(self.listA.currentRow())
        except:
            pass

    def on_moverI(self):
        try:
            self.listA.addItem(self.listB.currentItem().text())
            self.listB.takeItem(self.listB.currentRow())
        except:
            pass        

    def on_editar(self):
        try:

            if  self.listA.currentItem():
                texto_item = self.listA.currentItem().text()
                nuevo_texto, ok = QInputDialog.getText(self, 'Editar',
                            'Ingrese nuevo item', text=texto_item)
                if ok:
                    self.listA.currentItem().setText(nuevo_texto)
            else:
                texto_item = self.listB.currentItem().text()
                nuevo_texto, ok = QInputDialog.getText(self, 'Editar',
                            'Ingrese nuevo item', text=texto_item)
                if ok:
                    self.listB.currentItem().setText(nuevo_texto)
        except:

           QMessageBox.about(self, "Error", "No hay item seleccionado")



    def on_quitar(self):
        if  self.listA.hasFocus():
            self.listA.takeItem(self.listA.currentRow())
        else:
            self.listB.takeItem(self.listB.currentRow())

    def on_Click(self):
        if  self.listA.hasFocus():
            self.listB.currentRow().setSelected(False)
        else:
            self.listB.takeItem(self.listB.currentRow())




app = QApplication([])
win = MiVentana()
win.show()
app.exec_()