import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from BD import BD
import recursosQT_rc

form_1, base_1 = uic.loadUiType('UI/perfilUsuario.ui')

class PerfilUsuario(base_1, form_1):
    def __init__(self, parent = None):
        super(base_1,self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.child = []
       

    def salir(self):
        self.parent.show()
        self.hide()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    perfilUsuarioW = PerfilUsuario()
    perfilUsuarioW.show()
    sys.exit(app.exec_())