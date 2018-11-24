import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget

form_1, base_1 = uic.loadUiType('UI/gestorUsuario.ui')

class GestorUsuario(base_1, form_1):
    def __init__(self, parent = None):
        super(base_1,self).__init__()
        self.setupUi(self)
        self.bAtras.clicked.connect(self.atras)
        self.parent = parent
        self.child = []

    def atras(self):
        self.hide()
        self.parent.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    gestorUsuarioW = GestorUsuario()
    gestorUsuarioW.show()
    sys.exit(app.exec_())
