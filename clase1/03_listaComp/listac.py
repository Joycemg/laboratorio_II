from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog
from PyQt5 import uic
# Intercambiar habilitacion de botones 

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("laboratorio_II/clase1/03_listaComp/listaComp.ui", self)
        self.botonAgregar.clicked.connect(self.on_agregar)
        # self.bEditar.clicked.connect(self.on_editar)
        # self.BEliminar.clicked.connect(self.on_quitar)
        # self.bETodos.clicked.connect(self.remove_all)


    def on_agregar(self):
        if self.nombre.text().strip():
            self.listC.addItem(self.nombre.text().strip())
            self.nombre.setText('')
        

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()