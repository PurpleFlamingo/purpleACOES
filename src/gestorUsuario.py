import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from BD.BDOperaciones import BDOperaciones
from perfilUsuario import PerfilUsuario
import datetime

form_1, base_1 = uic.loadUiType('UI/gestorUsuario.ui',resource_suffix='')

class GestorUsuario(base_1, form_1):
    def __init__(self, parent = None):
        super(base_1,self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.child = []

        self.getUsuarios()

        self.bAtras.clicked.connect(self.atras)
        self.bAnadirUsuario.clicked.connect(self.newUsuario)
        self.bEditarUsuario.clicked.connect(self.editarUsuario)

    def atras(self):
        self.parent.show()
        self.hide()

    def newUsuario(self):
        self.child.append(PerfilUsuario(self))
        self.child[len(self.child)-1].show()

    def editarUsuario(self):
        self.child.append(PerfilUsuario(self))
        self.child[len(self.child)-1].show()

    #TODO: Esta funcion debe recoger de la base de datos todos los usuarios y mostrarlos en la vista
    def getUsuarios(self):
        db = BDOperaciones()
        usuarios = db.getUsuarios()
        self.tUsuarios.setColumnCount(len(usuarios[0][0]) + len(usuarios[0][1]))
        self.tUsuarios.setRowCount(len(usuarios))
        for i, user in enumerate(usuarios):
            for j, data in enumerate(user[0]):
                if type(data) is int:
                    self.tUsuarios.setItem(i, j, QTableWidgetItem(str(data)))
                else:
                    self.tUsuarios.setItem(i, j, QTableWidgetItem(data))
            for j, data in enumerate(user[1]):
                #print(type(data))
                if type(data) is datetime.date:
                    self.tUsuarios.setItem(i, len(user[0]) + j, QTableWidgetItem(data.strftime('%Y-%m-%d')))
                elif type(data) is int:
                    self.tUsuarios.setItem(i, len(user[0]) + j, QTableWidgetItem(str(data)))
                else:
                    self.tUsuarios.setItem(i, len(user[0]) + j, QTableWidgetItem(data))
        return []

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gestorUsuarioW = GestorUsuario()
    gestorUsuarioW.show()
    sys.exit(app.exec_())
