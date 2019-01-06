import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QHeaderView
from BD.Joven import Joven
from BD.Usuario import Usuario
from perfilBecado import PerfilBecado
from warningNoUserSelected import WarningNoUserSelected

form_1, base_1 = uic.loadUiType('UI/gestorApadrinamiento.ui')

class GestorApadrinamiento(base_1, form_1):
    def __init__(self, iduser: int, parent = None):
        super(base_1,self).__init__()
        self.setupUi(self)
        self.idUsuario = iduser
        # instancia del usuario de la sesion para obtener su rol
        usuario = Usuario.getUsuario(self.idUsuario)
        self.rolUsuario = usuario.getRolId()
        self.parent = parent
        self.child = None
        # datos comunes a socios y voluntarios
        self.datosComunes = ['nombre', 'apellidos', 'estado', 'coloniaNacimiento', 'coloniaResidencia', 'colegio']
        # lista de nombres de las columnas
        # deben referirse a los datos de las dos listas de arriba concatenadas y ordenadas
        self.cabeceras = ['Nombre', 'Apellidos', 'Estado', 'Fecha Nacimiento', 'Grado', 'Colonia de Nacimiento', 'Colonia de Residencia', 'Colegio']
        # lista con toda la informacion de los usuarios actuales en la base de datos
        self.jovenes = []
        self.filtrada = []

        self.refresh()

        self.bAtras.clicked.connect(self.atras)
        self.bAnadirBecado.clicked.connect(self.newBecado)
        self.bEditarBecado.clicked.connect(self.editBecado)
        self.bActualizar.clicked.connect(self.refresh)

        self.cEstado.currentIndexChanged.connect(self.busqueda)
        self.cCNacimiento.currentIndexChanged.connect(self.busqueda)
        self.cCResidencia.currentIndexChanged.connect(self.busqueda)
        self.cColegio.currentIndexChanged.connect(self.busqueda)
        self.eNombre.textChanged.connect(self.busqueda)
        self.eApellidos.textChanged.connect(self.busqueda)

    def atras(self):
        self.parent.show()
        self.close()

    def newBecado(self):
        self.child = PerfilBecado(self) # hacer perfil de un becado
        self.child.show()

    def editBecado(self):
        index = self.tBecados.selectedIndexes()
        if not index:
            self.child = WarningNoUserSelected(self)
            self.child.show()
            print('No se ha seleccionado ningun becado.')
        else:
            kid = index[0].row()
            if self.filtrada:
                idSeleccionado = self.filtrada[kid]['id_joven']
            else:
                idSeleccionado = self.usuarios[kid]['id_joven']

            self.child = PerfilBecado(self, id = idSeleccionado, rolUsuarioSesion = self.rolUsuario)
            self.child.show()

    def refresh(self):
        db = Joven()
        jovenes = db.listaJovenes()
        # cargamos metadatos de la tabla
        self.tBecados.verticalHeader().hide()
        self.tBecados.setColumnCount(len(self.cabeceras))
        self.tBecados.setRowCount(len(jovenes))
        self.tBecados.setHorizontalHeaderLabels(self.cabeceras)
        self.tBecados.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        estados = ['']
        cnacimiento = ['']
        cresidencia = ['']
        colegio = ['']
        # iteramos por todos los usuarios y datos de cada usuario, y guardamos los elementos
        for i, kid in enumerate(jovenes):
            for j, key in enumerate(self.datosComunes):
                if key == 'estado':
                    if kid[key] not in estados:
                        estados.append(kid[key])
                elif key == 'coloniaNacimiento':
                    if kid[key] not in cnacimiento:
                        cnacimiento.append(kid[key])
                elif key == 'coloniaResidencia':
                    if kid[key] not in cresidencia:
                        cresidencia.append(kid[key])
                elif key == 'colegio':
                    if kid[key] not in colegio:
                        colegio.append(kid[key])
                print(jovenes[0])
                self.tBecados.setItem(i, j, QTableWidgetItem(kid[key]))

        # cargar lista de opciones en cada comboBox
        self.cEstado.clear()
        self.cEstado.addItems(estados)
        self.cCNacimiento.clear()
        self.cCNacimiento.addItems(cnacimiento)
        self.cCResidencia.clear()
        self.cCResidencia.addItems(cresidencia)
        self.cColegio.clear()
        self.cColegio.addItems(colegio)

        self.jovenes = jovenes

    def busqueda(self):
        # lectura de los campos de filtrado
        nombre = self.eNombre.text()
        apellidos = self.eApellidos.text()
        estado = self.cEstado.currentText()
        cnacimiento = self.cCNacimiento.currentText()
        cresidencia = self.cCResidencia.currentText()
        colegio = self.cColegio.currentText()

        # filtramos todos los resultados por todos los campos
        result = self.jovenes

        result = [kid for kid in result if nombre == '' or nombre.lower() in kid['nombre'].lower()]
        result = [kid for kid in result if apellidos == '' or apellidos.lower() in kid['apellidos'].lower()]
        result = [kid for kid in result if estado == '' or estado.lower() in kid['estado'].lower()]
        result = [kid for kid in result if cnacimiento == '' or cnacimiento.lower() in kid['coloniaNacimiento'].lower()]
        result = [kid for kid in result if cresidencia == '' or cresidencia.lower() in kid['coloniaResidencia'].lower()]
        result = [kid for kid in result if colegio == '' or colegio.lower() in kid['colegio'].lower()]

        self.filtrada = result
        # actualizamos la vista por los contenidos filtrados
        self.tBecados.setRowCount(len(result))
        for i, kid in enumerate(result):
            for j, key in enumerate(self.datosComunes):
                self.tBecados.setItem(i, j, QTableWidgetItem(kid[key]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gestorApadrinamientoW = GestorApadrinamiento('2')
    gestorApadrinamientoW.show()
    sys.exit(app.exec_())
