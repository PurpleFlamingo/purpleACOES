import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QHeaderView
from BD.Joven import Joven
from BD.Usuario import Usuario
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
            self.child = PerfilBecado(idSeleccionado)
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
        # self.datosComunes = ['nombre', 'apellidos', 'estado', 'fechaNacimiento', 'grado', 'coloniaNacimiento', 'coloniaResidencia', 'colegio']
        for i, kid in enumerate(jovenes):
            for j, key in enumerate(self.datosComunes):
                if key == 'nombre':
                    if kid.getNombre() != None:
                        self.tBecados.setItem(i, j, QTableWidgetItem(str(kid.getNombre())))
                elif key == 'apellidos':
                    if kid.getApellido() != None:
                        self.tBecados.setItem(i, j, QTableWidgetItem(str(kid.getApellido())))
                elif key == 'estado':
                    if kid.getEstado() != None:
                        if kid.getEstado() not in estados:
                            estados.append(kid.getEstado())
                        self.tBecados.setItem(i, j, QTableWidgetItem(str(kid.getEstado())))
                elif key == 'fechaNacimiento':
                    if kid.getFechaNacimiento() != None:
                        self.tBecados.setItem(i, j, QTableWidgetItem(str(kid.getFechaNacimiento())))
                elif key == 'grado':
                    if kid.getGrado() != None:
                        self.tBecados.setItem(i, j, QTableWidgetItem(str(kid.getGrado())))
                    else:
                        self.tBecados.setItem(i, j, QTableWidgetItem(''))
                elif key == 'coloniaNacimiento':
                    if kid.getColoniaNacimiento() != None:
                        if str(kid.getColoniaNacimiento().getIdColonia()) not in cnacimiento:
                            cnacimiento.append(str(kid.getColoniaNacimiento().getIdColonia()))
                        self.tBecados.setItem(i, j, QTableWidgetItem(str(kid.getColoniaNacimiento().getIdColonia())))
                elif key == 'coloniaResidencia':
                    if kid.getColoniaResidencia() != None:
                        if str(kid.getColoniaResidencia().getIdColonia()) not in cresidencia:
                            cresidencia.append(str(kid.getColoniaResidencia().getIdColonia()))
                        self.tBecados.setItem(i, j, QTableWidgetItem(str(kid.getColoniaResidencia().getIdColonia())))
                elif key == 'colegio':
                    if kid.getColegio() != None:
                        if str(kid.getColegio().getIdColegio()) not in colegio:
                            colegio.append(str(kid.getColegio().getIdColegio()))
                        self.tBecados.setItem(i, j, QTableWidgetItem(str(kid.getColegio().getIdColegio())))
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
        result = [kid for kid in result if nombre == '' or nombre.lower() in str(kid.getNombre().lower())]
        result = [kid for kid in result if apellidos == '' or apellidos.lower() in str(kid.getApellido().lower())]
        result = [kid for kid in result if estado == '' or estado in str(kid.getEstado())]
        result = [kid for kid in result if cnacimiento == '' or cnacimiento in str(kid.getColoniaNacimiento().getIdColonia())]
        result = [kid for kid in result if cresidencia == '' or cresidencia in str(kid.getColoniaResidencia().getIdColonia())]
        result = [kid for kid in result if colegio == '' or colegio in str(kid.getColegio().getIdColegio())]
        self.filtrada = result
        # actualizamos la vista por los contenidos filtrados
        self.tBecados.setRowCount(len(result))
        for i, kid in enumerate(result):
            for j, key in enumerate(self.datosComunes):
                if key == 'nombre':
                    if kid.getNombre() != None:
                        self.tBecados.setItem(i, j, QTableWidgetItem(str(kid.getNombre())))
                elif key == 'apellidos':
                    if kid.getApellido() != None:
                        self.tBecados.setItem(i, j, QTableWidgetItem(str(kid.getApellido())))
                elif key == 'estado':
                    if kid.getEstado() != None:
                        self.tBecados.setItem(i, j, QTableWidgetItem(str(kid.getEstado())))
                elif key == 'fechaNacimiento':
                    if kid.getFechaNacimiento() != None:
                        self.tBecados.setItem(i, j, QTableWidgetItem(str(kid.getFechaNacimiento())))
                elif key == 'grado':
                    if kid.getGrado() != None:
                        self.tBecados.setItem(i, j, QTableWidgetItem(str(kid.getGrado())))
                    else:
                        self.tBecados.setItem(i, j, QTableWidgetItem(''))
                elif key == 'coloniaNacimiento':
                    if kid.getColoniaNacimiento() != None:
                        self.tBecados.setItem(i, j, QTableWidgetItem(str(kid.getColoniaNacimiento().getIdColonia())))
                elif key == 'coloniaResidencia':
                    if kid.getColoniaResidencia() != None:
                        self.tBecados.setItem(i, j, QTableWidgetItem(str(kid.getColoniaResidencia().getIdColonia())))
                elif key == 'colegio':
                    if kid.getColegio() != None:
                        self.tBecados.setItem(i, j, QTableWidgetItem(str(kid.getColegio().getIdColegio())))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gestorApadrinamientoW = GestorApadrinamiento('2')
    gestorApadrinamientoW.show()
    sys.exit(app.exec_())
