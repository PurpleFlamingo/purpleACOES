import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QHeaderView
from BD.BDOperaciones import BDOperaciones
from perfilUsuario import PerfilUsuario
from warningNoUserSelected import WarningNoUserSelected
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
        #Lista de nombres de las columnas
        #Deben referirse a los datos de las dos listas de arriba concatenadas y ordenadas
        self.cabeceras = ['Nombre', 'Apellidos', 'Provincia', 'Estado', 'Rol', 'Permiso']

        self.usuarios = []
        self.getUsuarios()

        self.bAtras.clicked.connect(self.atras)
        self.bAnadirUsuario.clicked.connect(self.newUsuario)
        self.bEditarUsuario.clicked.connect(self.editarUsuario)

    def recargar(self):
        self.getUsuarios()

    def atras(self):
        self.parent.show()
        self.hide()

    def newUsuario(self):
        self.child = PerfilUsuario(self)
        self.child.show()

    def editarUsuario(self):
        index = self.tUsuarios.selectedIndexes()
        if not index:
            self.child = WarningNoUserSelected(self)
            #self.child.setModal(True)
            self.child.show()
            print('No elemento seleccionado')
        else:
            user = index[0].row()
            idSeleccionado = self.usuarios[user]['id_usuario']
            self.child = PerfilUsuario(self,idSeleccionado)
            self.child.show()

    def getUsuarios(self):
        db = BDOperaciones()
        usuarios = db.getUsuarios()
        self.tUsuarios.verticalHeader().hide()
        self.tUsuarios.setColumnCount(len(self.cabeceras))
        self.tUsuarios.setRowCount(len(usuarios))
        self.tUsuarios.setHorizontalHeaderLabels(self.cabeceras)
        self.tUsuarios.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        for i, user in enumerate(usuarios):
            for j, key in enumerate(self.datosComunes):
                self.tUsuarios.setItem(i, j, QTableWidgetItem(user[key]))
            for j, key in enumerate(self.datosUsuarios):
                self.tUsuarios.setItem(i, len(self.datosComunes) + j, QTableWidgetItem(user[key]))
        self.usuarios = usuarios

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gestorUsuarioW = GestorUsuario()
    gestorUsuarioW.show()
    sys.exit(app.exec_())
