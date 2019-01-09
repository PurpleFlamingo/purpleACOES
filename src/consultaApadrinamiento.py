import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QHeaderView
from BD.Joven import Joven
from BD.Usuario import Usuario
from perfilApadrinamiento import PerfilApadrinamiento
from warningNoUserSelected import WarningNoUserSelected

form_1, base_1 = uic.loadUiType('UI/consultaApadrinamiento.ui')

class ConsultaApadrinamiento(base_1, form_1):
    def __init__(self, iduser: int, parent = None):
        super(base_1, self).__init__()
        self.setup.Ui(self)
        self.idUsuario = iduser
        usuario = Usuario.getUsuario(self.idUsuario)
        self.rolUsuario = usuario.getRolId()
        self.parent = parent
        self.child = None
        if Usuario.getUsuario(self.idUsuario).getRolId() != 'Agente Local' or Usuario.getUsuario(self.idUsuario) != 'Coordinador General':
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
        self.child = PerfilApadrinamiento()
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
            self.child = PerfilApadrinamiento(idSeleccionado, 'modificar')
            self.child.show()

    #def refresh(self):

if __name__ == '__main__':
    app = QApplication(sys.argv)
    consultaApadrinamientoW = ConsultaApadrinamiento('2')
    consultaApadrinamientoW.show()
    sys.exit(app.exec_())
