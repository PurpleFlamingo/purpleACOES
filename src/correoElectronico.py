import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from passwordDisplay import PasswordDisplay
from BD.BD import BD

form_1, base_1 = uic.loadUiType('UI/correoElectronico.ui')

class CorreoElectronico(base_1, form_1):
    def __init__(self, parent = None):
        self.claveRecuperada =  parent.claveRecuperada
        print(self.claveRecuperada)
        super(base_1,self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.child = None
        self.eEmail.setFocus(True)
        self.bOk.clicked.connect(self.aceptar)
        self.bExit.clicked.connect(self.salir)


    def salir(self):
        self.hide()


    def aceptar(self):
        email = self.eEmail.text().replace(' ','')
        if(email != None):
            if(email != ""):
                setter = "correo_electronico = " + email 
                if self.parent.claveBD[2].lower == "socio":
                    wherer = "id_socio = " + str(self.parent.id)
                    BD.update("socio", setter, wherer)
                else:
                    wherer = "id_voluntario = " + str(self.parent.id)
                    BD.update("voluntario", setter, wherer)
                print("La contraseña es :", self.claveRecuperada)
                if self.child is None or self.child != PasswordDisplay(self):
                    self.child = PasswordDisplay(self)
                    self.child.setModal(True)
                    self.child.show()

    
       