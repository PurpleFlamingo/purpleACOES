import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from BD.BDOperaciones import BDOperaciones

form_1, base_1 = uic.loadUiType('UI/cambiarContraseña.ui')


class CambiarContrasenia(base_1, form_1):
    def __init__(self):
        super(base_1, self).__init__()
        self.setupUi(self)
        self.bAtras.clicked.connect(self.atras)
        self.bEnviar.clicked.connect(self.enviarDatos)

    # Metodo que devuelve a perfil de usuario pulsando el boton atras
    def atras(self):
        self.parent.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cambiarContraseniaW = CambiarContrasenia()
    cambiarContraseniaW.show()
    sys.exit(app.exec_())
