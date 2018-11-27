import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from BD.BDOperaciones import BDOperaciones

form_1, base_1 = uic.loadUiType('UI/cambiarContraseña.ui')


class CambiarContrasenia(base_1, form_1):
    def __init__(self, iduser: int):
        self.idUsuario = iduser
        super(base_1, self).__init__()
        self.setupUi(self)
        self.bAtras.clicked.connect(self.atras)
        self.bEnviar.clicked.connect(self.enviardatos)
        bd = BDOperaciones()
        print("durum")
        print(bd.getUsuario(self.idUsuario)[2])
        self.lMensaje.setText(bd.getUsuario(self.idUsuario)[2])

    # Metodo que devuelve a perfil de usuario pulsando el boton atras
    def atras(self):
        self.parent.show()
        self.close()

    # Metodo que actualiza la contraseña de usuario o notifica un error en la bd
    def enviardatos(self):
        bd = BDOperaciones()
        contrasenia = bd.getUsuario(idUsuario)[2]
        self.lMensaje.setText(contrasenia)
        if str(contrasenia) != str(self.eCAntigua.text()):
            self.lMensaje.setText("Contraseña actual incorrecta.")
            self.eCAntigua.setText("")
            self.eCNueva.setText("")
            self.eCConfirmacion.setText("")
        if str(self.eCNueva.text()) != str(self.eCConfirmacion.text()):
            self.lMensaje.setText("Confirmación de contraseña es distinta a la nueva contraseña.")
            self.eCAntigua.setText("")
            self.eCNueva.setText("")
            self.eCConfirmacion.setText("")
        else:
            bd.setPassUsuario(eCNueva.text(), iduser)
            self.lMensaje.setText("Se ha cambiado la contraseña con exito.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cambiarContraseniaW = CambiarContrasenia(1)
    cambiarContraseniaW.show()
    sys.exit(app.exec_())
