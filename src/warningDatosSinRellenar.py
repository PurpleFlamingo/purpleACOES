import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget

form_1, base_1 = uic.loadUiType('UI/warningDatosSinRellenar.ui')

class WarningDatosSinRellenar(base_1, form_1):
    def __init__(self, parent = None, mensaje = None):
        super(base_1, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.mensaje = mensaje
        print(self.mensaje)
        if self.mensaje == 'Usuario':
            print("El usuario ingresado ya existe")
            self.lWarning.setText("Usuario ya existente")

        if self.mensaje == 'Clave':
            print("Las claves son distintas")
            self.lWarning.setText("Las claves introducidas son distintas")


        self.bAtras.clicked.connect(self.salir)

    def salir(self):
        self.close()
        #self.parent.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    warning = WarningDatosSinRellenar()
    warning.show()
    sys.exit(app.exec_())
