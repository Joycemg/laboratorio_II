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
        self.botonGuardar.clicked.connect(self.on_guardar)
        self.altura.textEdited.connect(self.validador)
        # Bandera para agregar usuario.
        self.flag = 0
        self.status = "cargado"
        self.listaBD = []

        # Conexion de BD
        self.conexion = sqlite3.connect("laboratorio_II/clase8/usuarios")
        self.cursor = self.conexion.cursor()
        self.on_cargar() # Cargamos la BD

        # Inicializacion de QmessageBox
        self.msg = QMessageBox()
        self.msg.setWindowTitle('TPLaboratorio')
        self.msg.setIcon(QMessageBox.Information)

    # Validacion de los campos para agregar usuario.
    def validador(self):
        labels = self.nombre, self.apellido, self.email, self.telefono, self.direccion, self.nacimiento, self.peso, self.altura

        if self.verificador(labels):
            self.botonAgregar.setEnabled(True)
            self.flag = 1
    def verificador(self, formulario):
        for x in formulario:
            if x.text():
                retorno = True
            else:
                retorno = False
                break
        return retorno
    def buscadorIndex(self, check):
        for i in range(len(self.listaBD)):
            if self.listaBD[i][0] == check:
                posicion = i
                break
        return posicion
    def on_click(self):
        # Activacion de botones
        self.botonEditar.setEnabled(True)
        self.botonEliminar.setEnabled(True)
        self.botonAgregar.setEnabled(True)

        # Lista con los datos seleccionados..
        click = self.lista.currentItem().text().split()
        click = int(click[0].strip(".")) 

        posicion = self.buscadorIndex(click)
        # Dupla de label para automatizacion.
        labels = self.id_, self.nombre, self.apellido, self.email, self.telefono, self.direccion, self.nacimiento, self.peso, self.altura

        # Automatizacion; Establecimiento de texto en los respectivo label y su desactivacion.
        for num, label in enumerate(labels):
            label.setText(str(self.listaBD[posicion][num]))
            if label == labels[0]:
                label.setText(f'id_{self.listaBD[posicion][0]}')
            label.setEnabled(False)

    def on_cargar(self):
        # Desactivacion de botones
        self.botonEditar.setEnabled(False)
        self.botonEliminar.setEnabled(False)
        self.botonAgregar.setEnabled(False)
        self.on_agregar()

        if not self.lista:
            self.listaBD.clear()
            # Seleccionamos todos los usuarios de la BD
            self.cursor.execute('select * from usuarios')
            usuarios = self.cursor.fetchall()

            # Carga de usuarios de la BD a la Qt5Lista.
            for usuario in usuarios:
                formatoLista = [usuario[0],usuario[1],usuario[2],usuario[3],usuario[4],usuario[5],usuario[6], usuario[7], usuario[8], self.status]
                formatoQt = f'''
    {usuario[0]}. {usuario[1]:4} {usuario[2]} 
        {usuario[3]:}         '''
                self.lista.addItem(formatoQt)
                self.listaBD.append(formatoLista)
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
        click = self.lista.currentItem().text().split()
        click = int(click[0].strip(".")) - 1
        usuario = self.listaBD[click]

        
        # Establecemos el usuario seleccionado en los label de la clase dialog
        labels = mydialog.nombre, mydialog.apellido, mydialog.email, mydialog.telefono, mydialog.direccion, mydialog.nacimiento, mydialog.peso, mydialog.altura
        for num, label in enumerate(labels):
            label.setText(usuario[num+1])
        mydialog.exec()

        # Verificar contenidos de labels

        if self.verificador(labels):
            formato = f'''
    {usuario[0]} {mydialog.nombre.text().capitalize():4} {mydialog.apellido.text().capitalize()} 
        {mydialog.email.text().capitalize():}         '''

            for num, label in enumerate(labels):
                self.listaBD[click][num+1] = label.text()

            self.lista.currentItem().setText(formato)
            self.lista.setCurrentItem(self.lista.currentItem())
            self.on_click()


    def on_eliminar(self):
        # Separamos nombre, apellido y mail, para su posterior uso
        usuario = self.lista.currentItem().text().split()
        click = int(usuario[0].strip(".")) - 1
        click2 = click + 1
        posicion = self.buscadorIndex(click2)
        print(posicion)
        self.msg.setText(f'¿Intentas eliminar el usuario {usuario[0]} {usuario[1]} {usuario[2]}?')
        self.msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        returnValue = self.msg.exec()
        if returnValue == QMessageBox.Yes:
            self.listaBD[posicion][9]  = "borrado"
            self.lista.takeItem(self.lista.currentRow())
            
    def on_agregar(self):
        labels = self.id_, self.nombre,self.apellido,self.email, self.telefono, self. direccion, self. nacimiento, self.peso, self.altura

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
            num = self.listaBD[-1][0] +1
            self.msg.setText(f'¿Quieres agregar el usuario numero {num}?\nNombre: {labels[1].text().capitalize()}\nApellido: {labels[1].text().capitalize()}\nEmail     : {labels[2].text().capitalize()}')
            self.msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            returnValue = self.msg.exec()
            if returnValue == QMessageBox.Yes:
                estatus = "agregado"
                formatoList = formatoLista = [num,labels[1].text(),labels[2].text(),labels[3].text(),labels[4].text(),labels[5].text(),labels[6].text(), labels[7].text(), labels[8].text(), estatus]
                formato = f'''
    {num}. {labels[1].text().capitalize()} {labels[2].text().capitalize()}
         {labels[3].text().capitalize():}'''
                self.listaBD.append(formatoList)
                self.lista.addItem(formato)
                seleccionar = self.lista.count() -1
                # Seleccionamos el ultimo usuario agregado 
                self.flag = 0
                self.lista.setCurrentRow(seleccionar)
                self.on_click()

    
    def on_guardar(self):
        self.cursor.execute('select * from usuarios')
        post = self.cursor.fetchall()

        for i in self.listaBD:
            if i[9] == "borrado":
                print(i, 'borrado')
                self.cursor.execute(f'DELETE FROM usuarios WHERE id = ("{i[0]}")')
                self.conexion.commit()
            elif i[9] == 'agregado':
                print(i, 'agregado')
                self.cursor.execute("insert into usuarios (nombre,apellido,mail,telefono,direccion,nacimiento,altura,peso) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(i[1],  i[2], i[3], i[4], i[5], i[6], i[7], i[8]))
                self.conexion.commit()

            
class dialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("laboratorio_II/clase8/inputDiag.ui", self)

app = QApplication([])

win = MiVentana()
win.show()

app.exec_()