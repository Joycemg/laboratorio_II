from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QInputDialog
from PyQt5 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("laboratorio_II/clase5/25-10/cbox/cBox.ui", self)
        self.msg = QMessageBox()
        self.msg.setWindowTitle('Alerta')
        self.msg.setIcon(QMessageBox.Warning)
        self.comboBox.currentIndexChanged.connect(self.on_Cambio)
        self.botonAgregar.clicked.connect(self.on_agregarItems)
        self.botonEditar.clicked.connect(self.on_editarItems)
        self.botonQuitar.clicked.connect(self.on_Quitar)
        self.botonQTodos.clicked.connect(self.on_QuitarTodo)


    def on_Cambio(self):
        indice = self.comboBox.currentIndex()
        self.etiqueta.setText(str(indice) + ' - ' + self.comboBox.currentText())

    def on_agregarItems(self):
        text, ok = QInputDialog.getText(self, 'Agregar Elementos', 'ok?')
        if ok and text:
            self.comboBox.addItem(text)
            indic = self.comboBox.findText(text)
            self.comboBox.setCurrentIndex(indic)

        else:
            self.msg.setText('No puede agregar vacios')
            self.msg.exec()

    def on_editarItems(self):
        self.msg.setStandardButtons(QMessageBox.Ok)
        if self.comboBox.count():
            indice = self.comboBox.currentIndex()
            texto_item = self.comboBox.currentText()
            nuevo_texto, ok = QInputDialog.getText(self, 'Editar',
            'Agrege nuevo nombre', text=texto_item)
            if ok and nuevo_texto and nuevo_texto != texto_item:
                self.comboBox.setItemText(indice, nuevo_texto)
                self.on_Cambio()
            else:
                self.msg.setText('No hay cambios')
                self.msg.exec()
        else:
            self.msg.setText('No hay items')
            self.msg.exec()

    def on_Quitar(self):
        self.msg.setStandardButtons(QMessageBox.Ok)
        if self.comboBox.count():
            self.msg.setText('Estas seguro?')
            self.msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            validar = self.msg.exec()
            if validar == QMessageBox.Yes:
                indice = self.comboBox.currentIndex()
                self.comboBox.removeItem(indice)
        else:
            self.msg.setText('No hay items')
            self.msg.exec()
    def on_QuitarTodo(self):
        self.msg.setStandardButtons(QMessageBox.Ok)
        if self.comboBox.count():
            self.msg.setText('Estas seguro?')
            self.msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            validar = self.msg.exec()
            if validar == QMessageBox.Yes:
                self.comboBox.clear()
                self.etiqueta.setText('')
        else:
            self.msg.setText('No hay items')
            self.msg.exec()


app = QApplication([])

win = MiVentana()
win.show()

app.exec_()