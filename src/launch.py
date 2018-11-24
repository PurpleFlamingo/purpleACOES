import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from gestorUsuario import GestorUsuario

form_1, base_1 = uic.loadUiType('UI/login.ui')

class LogIn(base_1, form_1):
    def __init__(self):
        super(base_1,self).__init__()
        self.setupUi(self)
        self.child = None

        self.bLogin.clicked.connect(self.usuario)
        self.bExit.clicked.connect(self.salir)

    def usuario(self):
        self.child = GestorUsuario(self)
        self.child.show()
        self.hide()

    def salir(self):
        exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    loginW = LogIn()
    loginW.show()
    sys.exit(app.exec_())
