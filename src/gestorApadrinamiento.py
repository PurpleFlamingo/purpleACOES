import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QHeaderView
from BD.Joven import Joven
from BD.Usuario import Usuario
from BD.Colonia import Colonia
from BD.Colegio import Colegio
from perfilBecado import PerfilBecado
from warningNoUserSelected import WarningNoUserSelected
from gestorProyecto import GestorProyecto

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
        self.user = Usuario()
        if self.user.getUsuario(self.idUsuario).getRolId() == 'Agente Local':
            self.bAnadirBecado.hide()
            self.bEditarBecado.hide()
        # datos comunes a socios y voluntarios
        self.datosComunes = ['nombre', 'apellidos', 'estado', 'fechaNacimiento', 'grado', 'coloniaNacimiento', 'coloniaResidencia', 'colegio']
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
        self.bProyectos.clicked.connect(self.proyectos)

        self.cEstado.currentIndexChanged.connect(self.busqueda)
        self.cCNacimiento.currentIndexChanged.connect(self.busqueda)
        self.cCResidencia.currentIndexChanged.connect(self.busqueda)
        self.cColegio.currentIndexChanged.connect(self.busqueda)
        self.eNombre.textChanged.connect(self.busqueda)
        self.eApellidos.textChanged.connect(self.busqueda)

    def proyectos(self):
        self.child = GestorProyecto(self)
        self.child.show()
        self.hide()

    def atras(self):
        self.parent.show()
        self.close()

    def newBecado(self):
        self.child = PerfilBecado()
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
                idSeleccionado = self.filtrada[kid].getIdJoven()
            else:
                idSeleccionado = self.jovenes[kid].getIdJoven()
            self.child = PerfilBecado(idSeleccionado, 'modificar')
            self.child.show()

    def refresh(self):
        self.cEstado.clear()
        self.cCNacimiento.clear()
        self.cCResidencia.clear()
        self.cColegio.clear()
        self.tBecados.clear()
        jovenes = Joven.listaJovenes()
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
        # self.datosComunes = ['nombre', 'apellidos', 'estado', 'fechaNacimiento', 'grado', 'coloniaNacimiento', 'coloniaResidencia', 'colegio']
        for i, kid in enumerate(jovenes):
                nombre = kid.getNombre()
                if nombre != None:
                    self.tBecados.setItem(i, 0, QTableWidgetItem(nombre))
                else:
                    self.tBecados.setItem(i, 0, QTableWidgetItem(''))
                apellidos = kid.getApellido()
                if apellidos != None:
                    self.tBecados.setItem(i, 1, QTableWidgetItem(apellidos))
                else:
                    self.tBecados.setItem(i, 1, QTableWidgetItem(''))
                estado = kid.getEstado()
                if estado != None:
                    if estado not in estados:
                        estados.append(estado)
                    self.tBecados.setItem(i, 2, QTableWidgetItem(estado))
                else:
                    self.tBecados.setItem(i, 2, QTableWidgetItem(''))
                fechanacimiento = str(kid.getFechaNacimiento())
                if fechanacimiento != None:
                    self.tBecados.setItem(i, 3, QTableWidgetItem(fechanacimiento))
                else:
                    self.tBecados.setItem(i, 3, QTableWidgetItem(''))
                grado = kid.getGrado()
                if grado != None:
                    self.tBecados.setItem(i, 4, QTableWidgetItem(grado))
                else:
                    self.tBecados.setItem(i, 4, QTableWidgetItem(''))
                if kid.getColoniaNacimiento() != None:
                    colon = kid.getColoniaNacimiento().getNombre()
                    if colon not in cnacimiento:
                        cnacimiento.append(colon)
                    self.tBecados.setItem(i, 5, QTableWidgetItem(colon))
                else:
                    self.tBecados.setItem(i, 5, QTableWidgetItem(''))
                if kid.getColoniaResidencia() != None:
                    colon2 = kid.getColoniaResidencia().getNombre()
                    if colon2 not in cresidencia:
                        cresidencia.append(colon2)
                    self.tBecados.setItem(i, 6, QTableWidgetItem(colon2))
                else:
                    self.tBecados.setItem(i, 6, QTableWidgetItem(''))
                if kid.getColegio() != None:
                    colegio1 = kid.getColegio().getNombreDeColegio()
                    if colegio1 not in colegio:
                        colegio.append(colegio1)
                    self.tBecados.setItem(i, 7, QTableWidgetItem(colegio1))
                else:
                    self.tBecados.setItem(i, 7, QTableWidgetItem(''))
        # cargar lista de opciones en cada comboBox
        self.cEstado.addItems(estados)
        self.cCNacimiento.addItems(cnacimiento)
        self.cCResidencia.addItems(cresidencia)
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
        result = [kid for kid in result if nombre == '' or nombre.lower() in str(kid.getNombre().lower())]
        result = [kid for kid in result if apellidos == '' or apellidos.lower() in str(kid.getApellido().lower())]
        result = [kid for kid in result if estado == '' or estado in str(kid.getEstado())]
        result = [kid for kid in result if cnacimiento == '' or cnacimiento in kid.getColoniaNacimiento().getNombre()]
        result = [kid for kid in result if cresidencia == '' or cresidencia in kid.getColoniaResidencia().getNombre()]
        result = [kid for kid in result if colegio == '' or colegio in kid.getColegio().getNombreDeColegio()]
        self.filtrada = result
        # actualizamos la vista por los contenidos filtrados
        self.tBecados.setRowCount(len(result))
        for i, kid in enumerate(result):
            nombre = kid.getNombre()
            if nombre != None:
                self.tBecados.setItem(i, 0, QTableWidgetItem(nombre))
            else:
                self.tBecados.setItem(i, 0, QTableWidgetItem(''))
            apellidos = kid.getApellido()
            if apellidos != None:
                self.tBecados.setItem(i, 1, QTableWidgetItem(apellidos))
            else:
                self.tBecados.setItem(i, 1, QTableWidgetItem(''))
            estado = kid.getEstado()
            if estado != None:
                self.tBecados.setItem(i, 2, QTableWidgetItem(estado))
            else:
                self.tBecados.setItem(i, 2, QTableWidgetItem(''))
            fechanacimiento = str(kid.getFechaNacimiento())
            if fechanacimiento != None:
                self.tBecados.setItem(i, 3, QTableWidgetItem(fechanacimiento))
            else:
                self.tBecados.setItem(i, 3, QTableWidgetItem(''))
            grado = kid.getGrado()
            if grado != None:
                self.tBecados.setItem(i, 4, QTableWidgetItem(grado))
            else:
                self.tBecados.setItem(i, 4, QTableWidgetItem(''))
            if kid.getColoniaNacimiento() != None:
                colon = kid.getColoniaNacimiento().getNombre()
                self.tBecados.setItem(i, 5, QTableWidgetItem(colon))
            else:
                self.tBecados.setItem(i, 5, QTableWidgetItem(''))
            if kid.getColoniaResidencia() != None:
                colon2 = kid.getColoniaResidencia().getNombre()
                self.tBecados.setItem(i, 6, QTableWidgetItem(colon2))
            else:
                self.tBecados.setItem(i, 6, QTableWidgetItem(''))
            if kid.getColegio() != None:
                colegio1 = kid.getColegio().getNombreDeColegio()
                self.tBecados.setItem(i, 7, QTableWidgetItem(colegio1))
            else:
                self.tBecados.setItem(i, 7, QTableWidgetItem(''))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gestorApadrinamientoW = GestorApadrinamiento('2')
    gestorApadrinamientoW.show()
    sys.exit(app.exec_())
