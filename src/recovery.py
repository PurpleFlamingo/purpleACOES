import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget

form_1, base_1 = uic.loadUiType('UI/recovery.ui')

class Recovery(base_1, form_1):
    def __init__(self, parent = None):
        super(base_1,self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.child = None

        self.eUserName.setText(self.parent.eUser.text())
        self.bOk.clicked.connect(self.aceptar)
        self.bExit.clicked.connect(self.salir)

    def aceptar(self):
        self.hide()
        self.parent.show()

    def salir(self):
        self.hide()
        self.parent.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    recoveryW = Recovery()
    recoveryW.show()
    sys.exit(app.exec_())
