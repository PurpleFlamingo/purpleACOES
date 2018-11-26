import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from BD.BDOperaciones import BDOperaciones
import recursosQT_rc

form_1, base_1 = uic.loadUiType('UI/perfilUsuario.ui')

class PerfilUsuario(base_1, form_1):
    def __init__(self, parent = None, id_socio = None):
        super(base_1,self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.id_socio= 1
        self.bSalirSinGuardar.clicked.connect(self.salir)
        if self.id_socio!=None:
            db= BDOperaciones()
            socio=db.getSocio(self.id_socio)
            self.eNombre.setText(socio[1])
            self.eApellidos.setText(socio[2])
            self.eNif.setText(socio[3])
            self.eDireccion.setText(socio[4])
            self.ePoblacion.setText(socio[5])
            self.eCodigoPostal.setText(socio[6])
            self.eProvincia.setText(socio[7])
            self.eEstado.setText(socio[8])
            self.eTelefono1.setText(socio[9])
            self.eTelefono2.setText(socio[10])
            self.eCorreoElectronico.setText(socio[11])
            self.eRelacion.setText(socio[12])
            self.eCertificado.setText(str(socio[13]))
            self.eSector.setText(socio[14])
            self.eFechaAlta.setText(socio[15].strftime('%Y-%m-%d'))
            self.eFechaSalida.setText(socio[16])
            self.eComentarios.setText(socio[17])



        


    def salir(self):
        self.parent.show()
        self.hide()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    perfilUsuarioW = PerfilUsuario()
    perfilUsuarioW.show()
    sys.exit(app.exec_())
