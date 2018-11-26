import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from BD.BDOperaciones import BDOperaciones
from correoElectronico import CorreoElectronico
from passwordDisplay import PasswordDisplay

form_1, base_1 = uic.loadUiType('UI/recovery.ui')

class Recovery(base_1, form_1):
    def __init__(self, parent = None):
        super(base_1,self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.child = None
        self.claveRecuperada = None

        self.eUserName.setFocus()
        self.bExit.clicked.connect(self.salir)
        self.bOk.clicked.connect(self.olvido)

    def salir(self):
        self.hide()
        self.parent.show()

    def olvido(self):
        nombre = self.eUserName.text().replace(' ','')
        self.recuperatorio(nombre)


    def recuperatorio(self,user: str):
        if user != None and user != "":
            db = BDOperaciones()
            self.claveRecuperada, emailSet = db.recovery(user)
            if(emailSet):
                if self.child is None or self.child != CorreoElectronico(self):
                    self.child = CorreoElectronico(self)
                    self.child.setModal(True)
                    self.child.show()
            else:
                if self.claveRecuperada == None:
                    self.eUserName.setText('Usuario incorrecto')
                elif self.child is None or self.child != PasswordDisplay(self):
                    self.passwordParent = "Recovery"
                    print("La contraseña es :", self.claveRecuperada)
                    self.child = PasswordDisplay(self)
                    self.child.setModal(True)
                    self.child.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    recoveryW = Recovery()
    recoveryW.show()
    sys.exit(app.exec_())
