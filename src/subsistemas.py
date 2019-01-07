import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from gestorUsuario import GestorUsuario
from gestorFinanciero import GestorFinanciero
from BD.Usuario import Usuario
from perfilUsuario import PerfilUsuario
from consultaPagos import ConsultaPagos
from gestorApadrinamiento import GestorApadrinamiento


form_1, base_1 = uic.loadUiType('UI/subsistemas.ui')


class Subsistemas(base_1, form_1):
    def __init__(self, iduser: int, parent = None):
        super(base_1, self).__init__()
        self.setupUi(self)
        self.idUsuario = iduser
        self.parent = parent
        self.child = None
        usuario = Usuario.getUsuario(self.idUsuario)
        self.rolUsuario = usuario.getRolId()
        self.bPerfil.setIcon(QIcon('MEDIA/User_icon.png'))
        self.bPerfil.setIconSize(QSize(24, 24))

        if self.rolUsuario == 'Socio':
            self.bFinanciero.setText('Consulta de pagos')
            self.bApadrinamiento.setText('Jovenes apadrinados')
            self.bUsuarios.hide()
            self.bFinanciero.move(80, 100)
            self.bFinanciero.clicked.connect(self.consultaDePagos)
            self.bApadrinamiento.move(80, 220)
        else:
            self.bUsuarios.clicked.connect(self.usuarios)
            self.bFinanciero.clicked.connect(self.financiero)
            self.bApadrinamiento.clicked.connect(self.apadrinamiento)

        self.bAtras.clicked.connect(self.atras)
        self.bPerfil.clicked.connect(self.perfil)

    def perfil(self):
        self.child = PerfilUsuario(self, self.idUsuario, self.rolUsuario, self.rolUsuario)
        self.child.show()

    def atras(self):
        self.parent.show()
        self.close()

    def usuarios(self):
        if self.child is None or self.child != GestorUsuario(self.idUsuario, self):
            self.child = GestorUsuario(self.idUsuario, self)
            self.child.show()
            self.hide()
        else:
            self.hide()
            self.child.show()

    def financiero(self):
        if self.child is None or self.child != GestorFinanciero(self, self.idUsuario):
            self.child = GestorFinanciero(self, self.idUsuario)
            self.child.show()
            self.hide()
        else:
            self.hide()
            self.child.show()

    def consultaDePagos(self):
            self.child = ConsultaPagos(self, self.idUsuario)
            self.child.show()
            self.hide()

    def apadrinamiento(self):
        if self.child is None or self.child != GestorApadrinamiento(self.idUsuario, self):
            self.child = GestorApadrinamiento(self.idUsuario, self)
            self.child.show()
            self.hide()
        else:
            self.hide()
            self.child.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    subsistemaW = Subsistemas('1')
    subsistemaW.show()
    sys.exit(app.exec_())
