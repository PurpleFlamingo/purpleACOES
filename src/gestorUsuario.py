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
        self.bActualizar.clicked.connect(self.recargar)
        self.bBuscar.clicked.connect(self.busqueda)

    def recargar(self):
        self.getUsuarios()

    def atras(self):
        self.parent.show()
        self.hide()

    def newUsuario(self):
        rol = self.cRolNew.currentText()
        self.child = PerfilUsuario(self, rol = rol)
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
            self.child = PerfilUsuario(self,id = idSeleccionado)
            self.child.show()

    def resetBusqueda(self):
        self.eNombre.setText('')
        self.eApellidos.setText('')
        self.cProvincia.setCurrentIndex(0)
        self.cEstado.setCurrentIndex(0)
        self.cRol.setCurrentIndex(0)
        self.cPermiso.setCurrentIndex(0)

    def getUsuarios(self):
        db = BDOperaciones()
        usuarios = db.getUsuarios()
        self.tUsuarios.verticalHeader().hide()
        self.tUsuarios.setColumnCount(len(self.cabeceras))
        self.tUsuarios.setRowCount(len(usuarios))
        self.tUsuarios.setHorizontalHeaderLabels(self.cabeceras)
        self.tUsuarios.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        roles = []
        permisos = []
        provincias = []
        estados = []
        for i, user in enumerate(usuarios):
            for j, key in enumerate(self.datosComunes):
                if key == 'provincia':
                    if user[key] not in provincias:
                        provincias.append(user[key])
                elif key == 'estado':
                    if user[key] not in estados:
                        estados.append(user[key])
                self.tUsuarios.setItem(i, j, QTableWidgetItem(user[key]))
            for j, key in enumerate(self.datosUsuarios):
                if key == 'rol':
                    if user[key] not in roles:
                        roles.append(user[key])
                elif key == 'permiso':
                    if user[key] not in permisos:
                        permisos.append(user[key])
                self.tUsuarios.setItem(i, len(self.datosComunes) + j, QTableWidgetItem(user[key]))

        self.cProvincia.clear()
        self.cProvincia.addItems([''])
        self.cProvincia.addItems(provincias)
        self.cEstado.clear()
        self.cEstado.addItems([''])
        self.cEstado.addItems(estados)
        self.cRolNew.clear()
        self.cRolNew.addItems(roles)
        self.cRol.clear()
        self.cRol.addItems([''])
        self.cRol.addItems(roles)
        self.cPermiso.clear()
        self.cPermiso.addItems([''])
        self.cPermiso.addItems(permisos)

        #self.resetBusqueda()

        self.usuarios = usuarios

    def busqueda(self):
        nombre = self.eNombre.text()
        apellido = self.eApellidos.text()
        provincia = self.cProvincia.currentText()
        estado = self.cEstado.currentText()
        rol = self.cRol.currentText()
        permiso = self.cPermiso.currentText()

        result = self.usuarios

        result = [user for user in result if nombre == '' or nombre.lower() in user['nombre_pila'].lower()]
        result = [user for user in result if apellido == '' or apellido.lower() in user['apellidos'].lower()]
        result = [user for user in result if provincia == '' or provincia.lower() in user['provincia'].lower()]
        result = [user for user in result if estado == '' or estado.lower() in user['estado'].lower()]
        result = [user for user in result if rol == '' or rol.lower() in user['rol'].lower()]
        result = [user for user in result if permiso == '' or permiso.lower() in user['permiso'].lower()]

        self.tUsuarios.setRowCount(len(result))
        for i, user in enumerate(result):
            for j, key in enumerate(self.datosComunes):
                self.tUsuarios.setItem(i, j, QTableWidgetItem(user[key]))
            for j, key in enumerate(self.datosUsuarios):
                self.tUsuarios.setItem(i, len(self.datosComunes) + j, QTableWidgetItem(user[key]))

        #self.resetBusqueda()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gestorUsuarioW = GestorUsuario()
    gestorUsuarioW.show()
    sys.exit(app.exec_())
