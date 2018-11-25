import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from gestorUsuario import GestorUsuario
from recovery import Recovery


form_1, base_1 = uic.loadUiType('UI/login.ui')

class LogIn(base_1, form_1):
    def __init__(self):
        super(base_1,self).__init__()
        self.setupUi(self)
        self.child = None

        self.bRecordatorio.clicked.connect(self.recordatorio)
        self.bLogin.clicked.connect(self.usuario)
        self.bExit.clicked.connect(self.salir)

    #TODO: Esta funcion debe ser modificada para que redireccione a la ventana de seleccion de subsistema
    def usuario(self):
        self.child = GestorUsuario(self)
        self.child.show()
        self.hide()

    def salir(self):
        exit()

    def recordatorio(self):
        self.child = Recovery(self)
        self.child.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    loginW = LogIn()
    loginW.show()
    sys.exit(app.exec_())
