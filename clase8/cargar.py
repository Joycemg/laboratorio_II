from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QDialog
from PyQt5 import uic
import sqlite3



class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("laboratorio_II/clase8/Icargar.ui", self)
        # Conexiones de botones.
        self.botonCargar.clicked.connect(self.on_cargar) # Cargar BD a Qt5lista
        self.lista.itemClicked.connect(self.on_click) # Interaccion con la Qt5lista
        self.botonEliminar.clicked.connect(self.on_eliminar) # Eliminar usuario
        self.botonEditar.clicked.connect(self.on_editar) # Editar usuario
        self.botonAgregar.clicked.connect(self.on_agregar)
        self.email.textEdited.connect(self.validador)
        # Bandera para agregar usuario.
        self.flag = 0

        # Conexion de BD
        self.conexion = sqlite3.connect("laboratorio_II/clase8/bdIcargar")
        self.cursor = self.conexion.cursor()
        self.on_cargar() # Cargamos la BD

        # Inicializacion de QmessageBox
        self.msg = QMessageBox()
        self.msg.setWindowTitle('TPLaboratorio')
        self.msg.setIcon(QMessageBox.Information)

    # Validacion de los campos para agregar usuario.
    def validador(self):
        if self.nombre.text() and self.apellido.text() and "@" in self.email.text():
            self.botonAgregar.setEnabled(True)
            self.flag = 1

 
    def on_click(self):
        # Activacion de botones
        self.botonEditar.setEnabled(True)
        self.botonEliminar.setEnabled(True)
        self.botonAgregar.setEnabled(True)

        # Lista con los datos seleccionados..
        click = self.lista.currentItem().text().split()

        # Dupla de label para automatizacion.
        labels = self.nombre,self.apellido,self.email

        # Automatizacion; Establecimiento de texto en los respectivo label y su desactivacion.
        for num, label in enumerate(labels):
            label.setText(click[num+1])
            label.setEnabled(False)

    def on_cargar(self):
        # Desactivacion de botones
        self.botonEditar.setEnabled(False)
        self.botonEliminar.setEnabled(False)
        self.botonAgregar.setEnabled(False)
        self.on_agregar()

        if not self.lista:

            # Seleccionamos todos los usuarios de la BD
            self.cursor.execute('select * from personas')
            usuarios = self.cursor.fetchall()

            # Carga de usuarios de la BD a la Qt5Lista.
            for usuario in usuarios:
                formato = f'''
    {usuario[0]}. {usuario[1]:4} {usuario[2]} 
        {usuario[3]:}         '''
                self.lista.addItem(formato)
        else:
             self.msg.setText('Ya hay datos cargados.\n¿Quieres cargarlos otra vez?')
             self.msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
             returnValue = self.msg.exec()
             if returnValue == QMessageBox.Yes:
                 self.lista.clear()
                 self.on_cargar()
    
    def on_editar(self):
        # Llamamos a la clase Qdialog
        mydialog = dialog()
        mydialog.setModal(True)

        # Almacenamos en una lista los datos del usuario seleccionado
        labels = self.lista.currentItem().text().split()
        
        # Establecemos el usuario seleccionado en los label de la clase dialog
        mydialog.nombre.setText(labels[1])
        mydialog.apellido.setText(labels[2])
        mydialog.email.setText(labels[3])
        mydialog.exec()

        # Confirmamos los cambios, siempre y cuando los lineedit no esten vacios..
        if mydialog.nombre.text() and mydialog.apellido.text() and mydialog.email.text():
            formato = f'''
    {labels[0]} {mydialog.nombre.text().capitalize():4} {mydialog.apellido.text().capitalize()} 
        {mydialog.email.text().capitalize():}         '''
            self.lista.currentItem().setText(formato)
            self.on_click()
        else:
            pass


    def on_eliminar(self):
        # Separamos nombre, apellido y mail, para su posterior uso
        usuario = self.lista.currentItem().text().split()
        self.msg.setText(f'¿Intentas eliminar el usuario {usuario[0]} {usuario[1]} {usuario[2]}?')
        self.msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        returnValue = self.msg.exec()
        if returnValue == QMessageBox.Yes:
            self.lista.takeItem(self.lista.currentRow())

    def on_agregar(self):
        labels = self.nombre,self.apellido,self.email

        # Bandera desactivada
        if not self.flag:
            if self.lista.currentItem():
                self.lista.currentItem().setSelected(False)
            for label in labels:
                label.setText("")
                label.setEnabled(True)
            self.nombre.setFocus(True)

            self.botonEditar.setEnabled(False)
            self.botonEliminar.setEnabled(False)
            self.botonAgregar.setEnabled(False)
        
        #Bandera activa
        else:
            num = self.lista.count() # Contador de usuario

            formato = f'''
    {num + 1}. {labels[1].text().capitalize():4} {labels[2].text().capitalize()} 
        {labels[2].text().capitalize():}         '''
            self.lista.addItem(formato)

            # Seleccionamos el ultimo usuario agregado 
            self.lista.setCurrentRow(num)
            self.flag = 0
            self.on_click()

    # def on_agregar(self):
    #     nombre = self.nombre.text()
    #     apellido = self.apellido.text()
    #     email = self.email.text()

    #     self.cursor.execute(f'insert into personas (nombre,apellido,mail) values ({nombre}, {apellido}, {email})')
class dialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("laboratorio_II/clase8/inputDiag.ui", self)

app = QApplication([])

win = MiVentana()
win.show()

app.exec_()