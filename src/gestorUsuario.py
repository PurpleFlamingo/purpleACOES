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
        self.cabeceras = ['Nombre', 'Apellidos', 'Provincia', 'Pais', 'Rol', 'Permiso']

        #Lista con toda la informacion de los usuarios actuales en la base de datos
        self.usuarios = []

        self.filtrada = []


        self.recargar()

        #Relacion entre eventos y funciones
        self.bAtras.clicked.connect(self.atras)
        self.bAnadirUsuario.clicked.connect(self.newUsuario)
        self.bEditarUsuario.clicked.connect(self.editarUsuario)
        self.bActualizar.clicked.connect(self.recargar)
        self.bBuscar.clicked.connect(self.busqueda)


    #Carga la vista del padre
    def atras(self):
        self.parent.show()
        self.close()

    #Carga la vista de perfil de usuario con una vista vacia para crear un usuario nuevo
    def newUsuario(self):
        rol = self.cRolNew.currentText()
        self.child = PerfilUsuario(self, rol = rol)
        self.child.show()

    #Carga la vista de perfil de usuario con los datos del usuario seleccionado
    #Si no hay usuario seleccionado lanza un warning
    def editarUsuario(self):
        index = self.tUsuarios.selectedIndexes()
        if not index:
            self.child = WarningNoUserSelected(self)
            #self.child.setModal(True)
            self.child.show()
            print('No elemento seleccionado')
        else:
            print(index[0])
            user = index[0].row()
            idSeleccionado = self.filtrada[user]['id_usuario']
            rolSeleccionado = self.filtrada[user]['rol']
            self.child = PerfilUsuario(self,id = idSeleccionado, rol = rolSeleccionado)
            self.child.show()

    #Reinicia todos los campos usados en el filtrado
    def resetBusqueda(self):
        self.eNombre.setText('')
        self.eApellidos.setText('')
        self.cProvincia.setCurrentIndex(0)
        self.cEstado.setCurrentIndex(0)
        self.cRol.setCurrentIndex(0)
        self.cPermiso.setCurrentIndex(0)

    #Actualiza la informacion de usuarios de la base de datos y los muestra todos en la tabla
    def recargar(self):
        db = BDOperaciones()
        usuarios = db.getUsuarios()

        #Cargamos los metadatos de la tabla
        self.tUsuarios.verticalHeader().hide()
        self.tUsuarios.setColumnCount(len(self.cabeceras))
        self.tUsuarios.setRowCount(len(usuarios))
        self.tUsuarios.setHorizontalHeaderLabels(self.cabeceras)
        self.tUsuarios.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        roles = []
        permisos = []
        provincias = []
        estados = []
        #Iteramos por todos los usuarios y datos de cada usuario, y guardamos los elementos que necesitaremos para los desplegables
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

        #Cargar lista de opciones en cada comboBox
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

    #Filtra el contenido de la tabla y actualiza la vista
    def busqueda(self):
        #lectura de los campos de filtrado
        nombre = self.eNombre.text()
        apellido = self.eApellidos.text()
        provincia = self.cProvincia.currentText()
        estado = self.cEstado.currentText()
        rol = self.cRol.currentText()
        permiso = self.cPermiso.currentText()

        #Filtramos todos los resultados por todos los campos
        result = self.usuarios

        result = [user for user in result if nombre == '' or nombre.lower() in user['nombre_pila'].lower()]
        result = [user for user in result if apellido == '' or apellido.lower() in user['apellidos'].lower()]
        result = [user for user in result if provincia == '' or provincia.lower() in user['provincia'].lower()]
        result = [user for user in result if estado == '' or estado.lower() in user['estado'].lower()]
        result = [user for user in result if rol == '' or rol.lower() in user['rol'].lower()]
        result = [user for user in result if permiso == '' or permiso.lower() in user['permiso'].lower()]

        self.filtrada = result
        #Actualizamos la vista por los contenidos fitrados
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
