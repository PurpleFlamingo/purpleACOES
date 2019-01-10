import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QHeaderView
from BD.Apadrinamiento import Apadrinamiento
from BD.Usuario import Usuario
from BD.Socio import Socio
from BD.Voluntario import Voluntario
from perfilApadrinamientos import PerfilApadrinamientos
from warningNoUserSelected import WarningNoUserSelected

form_1, base_1 = uic.loadUiType('UI/consultaApadrinamiento.ui')

class ConsultaApadrinamiento(base_1, form_1):
    def __init__(self, iduser: int, parent = None):
        super(base_1, self).__init__()
        self.setupUi(self)
        self.idUsuario = iduser
        self.usuario = Usuario.getUsuario(self.idUsuario)
        self.rolUsuario = self.usuario.getRolId()
        self.socio = Socio.getSocio(self.idUsuario)
        self.esSocio = True
        if self.socio == None:
            self.socio = Voluntario.getVoluntario(self.idUsuario)
            self.esSocio = False
        self.parent = parent
        self.child = None
        if (self.rolUsuario != 'Agente Local') and (self.rolUsuario != 'Coordinador General'):
            self.bNuevoApadrinamiento.hide()
            self.bEditarApadrinamiento.hide()

        self.cabeceras = ['Joven', 'Asociado a', 'Fecha de Inicio', 'Fecha de Fin']
        self.apadrinamientos = []
        self.refresh()

        self.bAtras.clicked.connect(self.atras)
        self.bNuevoApadrinamiento.clicked.connect(self.crear)
        self.bEditarApadrinamiento.clicked.connect(self.editar)
        self.bActualizar.clicked.connect(self.refresh)

    def atras(self):
        self.parent.show()
        self.close()

    def crear(self):
        self.child = PerfilApadrinamientos()
        self.child.show()

    def editar(self):
        index = self.tApadrinamientos.selectedIndexes()
        if not index:
            self.child = WarningNoUserSelected(self)
            self.child.show()
            print('No se ha seleccionado ningun apadrinado.')
        else:
            ap = index[0].row()
            idSeleccionado = self.apadrinamientos[ap].getIdApadrinamiento()
            self.child = PerfilApadrinamientos(idSeleccionado, self.idUsuario, 'modificar')
            self.child.show()

    def refresh(self):
        self.tApadrinamientos.clear()
        if self.esSocio:
            self.eSocio.setText((self.socio.getNombreDePila() + ' ' + self.socio.getApellidos()) if (self.socio.getNombreDePila() != None) else '')
        else:
            self.eSocio.setText((self.socio.getNombre() + ' ' + self.socio.getApellidos()) if (self.socio.getNombre() != None) else '')
        apadrinamientos = Apadrinamiento.listaApadrinamientos()
        # cargamos metadatos de la tabla
        self.tApadrinamientos.verticalHeader().hide()
        self.tApadrinamientos.setColumnCount(len(self.cabeceras))
        self.tApadrinamientos.setRowCount(len(apadrinamientos))
        self.tApadrinamientos.setHorizontalHeaderLabels(self.cabeceras)
        self.tApadrinamientos.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

        fila = 0
        for i, ap in enumerate(apadrinamientos):
            if self.esSocio:
                if str(ap.getSocio().getUsuarioId()) == str(self.socio.getUsuarioId()) or (ap.getAgente().getUsuario() == self.socio.getUsuario()):
                    self.tApadrinamientos.setItem(fila, 0, QTableWidgetItem(ap.getJoven().getNombre() + ' ' + ap.getJoven().getApellido()))
                    self.tApadrinamientos.setItem(fila, 1, QTableWidgetItem(ap.getSocio().getNombreDePila() + ' ' + ap.getSocio().getApellidos()))
                    self.tApadrinamientos.setItem(fila, 2, QTableWidgetItem(str(ap.getFechaDeInicio())))
                    if ap.getFechaDeBaja() != None:
                        self.tApadrinamientos.setItem(fila, 3, QTableWidgetItem(str(ap.getFechaDeBaja())))
                    else:
                        self.tApadrinamientos.setItem(fila, 3, QTableWidgetItem(''))
                    fila += 1
            else:
                self.tApadrinamientos.setItem(i, 0, QTableWidgetItem(
                    ap.getJoven().getNombre() + ' ' + ap.getJoven().getApellido()))
                self.tApadrinamientos.setItem(i, 1, QTableWidgetItem(
                    ap.getSocio().getNombreDePila() + ' ' + ap.getSocio().getApellidos()))
                self.tApadrinamientos.setItem(i, 2, QTableWidgetItem(str(ap.getFechaDeInicio())))
                if ap.getFechaDeBaja() != None:
                    self.tApadrinamientos.setItem(i, 3, QTableWidgetItem(str(ap.getFechaDeBaja())))
                else:
                    self.tApadrinamientos.setItem(i, 3, QTableWidgetItem(''))

        self.apadrinamientos = apadrinamientos


if __name__ == '__main__':
    app = QApplication(sys.argv)
    consultaApadrinamientoW = ConsultaApadrinamiento('1')
    consultaApadrinamientoW.show()
    sys.exit(app.exec_())
