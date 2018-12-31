import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget

form_1, base_1 = uic.loadUiType('UI/warningSalirSinGuardar.ui')


class WarningSalirSinGuardar(base_1, form_1):
    def __init__(self, parent = None):
        super(base_1, self).__init__()
        self.setupUi(self)
        self.parent = parent
        
        self.bAtras.clicked.connect(self.volver)
        self.bSalir.clicked.connect(self.salir)

    def volver(self):
        self.close()
        
    def salir(self):
        self.close()
        self.parent.salir()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    warning = WarningSalirSinGuardar()
    warning.show()
    sys.exit(app.exec_())
