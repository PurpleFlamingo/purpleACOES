import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from gestorUsuario import GestorUsuario
from recovery import Recovery
from warning import Advertencia
#from BD.BD import BD
from BD.BDOperaciones import BDOperaciones


form_1, base_1 = uic.loadUiType('UI/login.ui')

class LogIn(base_1, form_1):
    def __init__(self):
        super(base_1,self).__init__()
        self.setupUi(self)
        self.child = None

        #variable para llevar la cuenta de los intentos erroneos consecutivos que se producen al iniciar sesión
        self.numeroIntentosErroneos = 0
        self.eUser.setFocus(True)
        self.bRecordatorio.clicked.connect(self.recordatorio)
        self.bLogin.clicked.connect(self.usuario)
        self.bExit.clicked.connect(self.salir)


    def usuario(self):
        #si el usuario no introduce el nombre de usuario o la contraseña el botón no hace nada
        if (self.eUser.text() != '') and (self.ePassword.text()) != '':
            if(self.inicio_sesion(self.eUser.text(), self.ePassword.text())):
                #Al iniciarse correctamente la sesión el número de intentos erroneos se resetea y se borra el mensaje de error
                self.numeroIntentosErroneos = 0
                self.lWarning.setText("")
                self.eUser.setText("")
                self.ePassword.setText("")
                if self.child is None or self.child != GestorUsuario(self):
                    self.child = GestorUsuario(self)
                    self.child.show()
                    self.hide()
                else:
                    self.hide()
                    self.child.show()
            else:
                #si el usuario introduce el nombre de usuario o contraseña incorrectos la
                #aplicación muestra un mensaje en la pantalla de inicio de sesión, si lo
                #hace por quinta vez consecutiva se muestra una ventana de dialogo comunicando
                #este hecho que solo tiene un botón que cierra la aplicación.
                self.numeroIntentosErroneos += 1
                if(self.numeroIntentosErroneos < 5):
                    self.lWarning.setText("Usuario o contraeña incorrectos")
                else:
                    self.child = Advertencia(self)
                    self.child.setModal(True)
                    self.child.show()



    def salir(self):
        exit()

    def recordatorio(self):
        if self.child is None or self.child != Recovery(self):
            self.child = Recovery(self)
            self.child.show()
            self.hide()
        else:
            self.hide()
            self.child.show()

    #método que evalua si el nombre de usuario y la contraseña estan en la base de datos y son correctos.
    def inicio_sesion(self,user: str, password: str):
        db = BDOperaciones()
        return db.login(user.lower(), password)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    loginW = LogIn()
    loginW.show()
    sys.exit(app.exec_())
