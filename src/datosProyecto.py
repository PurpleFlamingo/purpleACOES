import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from BD.BDOperaciones import BDOperaciones
import recursosQT_rc

form_1, base_1 = uic.loadUiType('UI/datosProyecto.ui')

class DatosProyecto(base_1, form_1):
    def __init__(self, parent = None, id = None, rol = None):
        super(base_1,self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.child = None

        self.bSalirSinGuardar.clicked.connect(self.salir)

    def salir(self):
        self.parent.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    datosProyectoW = DatosProyecto()
    datosProyectoW.show()
    sys.exit(app.exec_())
