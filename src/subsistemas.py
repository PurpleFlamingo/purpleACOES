import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit
from BD.BDOperaciones  import BDOperaciones
from gestorUsuario import GestorUsuario
from gestorFinanciero import GestorFinanciero
#from gestorApadrinamiento import GestorApadrinamiento


form_1, base_1 = uic.loadUiType('UI/subsistemas.ui')


class Subsistemas(base_1, form_1):
    def __init__(self, iduser: int, parent = None):
        super(base_1, self).__init__()
        self.setupUi(self)
        self.idUsuario = iduser
        self.parent = parent
        self.child = None
        self.bAtras.clicked.connect(self.atras)
        self.bUsuarios.clicked.connect(self.usuarios)
        self.bFinanciero.clicked.connect(self.financiero)
        self.bApadrinamiento.clicked.connect(self.apadrinamiento)

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
        #print('Hola, el boton funciona :D')

    def apadrinamiento(self):
        #if self.child is None or self.child != GestorApadrinamiento(self, self.idUsuario):
        #    self.child = GestorApadrinamiento(self, self.idUsuario)
        #    self.child.show()
        #    self.hide()
        #else:
        #    self.hide()
        #    self.child.show()
        print('Hola, el boton funciona :D')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    subsistemaW = Subsistemas('1')
    subsistemaW.show()
    sys.exit(app.exec_())
