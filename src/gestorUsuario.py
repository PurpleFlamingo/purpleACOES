import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QHeaderView
from BD.BDOperaciones import BDOperaciones
from perfilUsuario import PerfilUsuario
import datetime

form_1, base_1 = uic.loadUiType('UI/gestorUsuario.ui',resource_suffix='')

class GestorUsuario(base_1, form_1):
    def __init__(self, parent = None):
        super(base_1,self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.child = None
        #Estos deben de ser datos comunes a socios y voluntarios
        self.datosComunes = ['nombre_pila', 'apellidos', 'provincia', 'estado']
        self.datosUsuarios = ['rol', 'permiso']
        self.getUsuarios()

        self.bAtras.clicked.connect(self.atras)
        self.bAnadirUsuario.clicked.connect(self.newUsuario)
        self.bEditarUsuario.clicked.connect(self.editarUsuario)

    def atras(self):
        self.parent.show()
        self.hide()

    def newUsuario(self):
        self.child = PerfilUsuario(self)
        self.child.show()

    def editarUsuario(self):
        self.child = PerfilUsuario(self,1)#el segundo valor es de prueba
        self.child.show()

    def getUsuarios(self):
        db = BDOperaciones()
        usuarios = db.getUsuarios()
        self.tUsuarios.verticalHeader().hide()
        self.tUsuarios.setColumnCount(len(self.datosComunes) + len(self.datosUsuarios))
        self.tUsuarios.setRowCount(len(usuarios))
        self.tUsuarios.setHorizontalHeaderLabels(self.datosComunes+self.datosUsuarios)
        self.tUsuarios.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        for i, user in enumerate(usuarios):
            for j, key in enumerate(self.datosComunes):
                self.tUsuarios.setItem(i, j, QTableWidgetItem(user[key]))
            for j, key in enumerate(self.datosUsuarios):
                self.tUsuarios.setItem(i, len(self.datosComunes) + j, QTableWidgetItem(user[key]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gestorUsuarioW = GestorUsuario()
    gestorUsuarioW.show()
    sys.exit(app.exec_())
