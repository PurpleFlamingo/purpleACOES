import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from BD.BD import BD
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
        if user != None:
            if user != "":
                self.db = BD()
                self.nombre = "LOWER(`nombre`) = \"" + user.lower() + "\""
                self.claveBD = self.db.selectEscalar("id_usuario, clave, rol","usuario",self.nombre)
                if self.claveBD != None:
                    self.claveRecuperada = self.claveBD[1]
                    self.cond = "LOWER(`usuario`) = " + (str(self.claveBD[0])).lower()
                    
                    if self.claveBD[2].lower == "socio":
                        self.tabla = "socio"
                        self.identificacion = self.db.selectEscalar("id_socio",self.tabla,self.cond)
                    else:
                        self.tabla = "voluntario"
                        self.identificacion = self.db.selectEscalar("id_voluntario",self.tabla,self.cond)
                    self.id = self.identificacion[0]
                    print("Identificacion: ",self.id)
                    self.emailDB = self.db.selectEscalar("correo_electronico",self.tabla,self.cond)
                    print("Email: ",self.emailDB)
                    if(self.emailDB[0] == None):
                        if self.child is None or self.child != CorreoElectronico(self):
                            self.child = CorreoElectronico(self)
                            self.child.setModal(True)
                            self.child.show()
                    else:
                        print("La contraseña es :", self.claveRecuperada)
                        if self.child is None or self.child != PasswordDisplay(self):
                            self.child = PasswordDisplay(self)
                            self.child.setModal(True)
                            self.child.show()

                


if __name__ == '__main__':
    app = QApplication(sys.argv)
    recoveryW = Recovery()
    recoveryW.show()
    sys.exit(app.exec_())
