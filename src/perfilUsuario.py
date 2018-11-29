import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from BD.BDOperaciones import BDOperaciones
import recursosQT_rc

form_1, base_1 = uic.loadUiType('UI/perfilUsuario.ui')

class PerfilUsuario(base_1, form_1):
    def __init__(self, parent = None, id = None, rol = None):
        super(base_1,self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.idUser = id
        self.rolUser = rol
        self.bSalirSinGuardar.clicked.connect(self.salir)

        if self.rolUser=="Socio":
        	self.lFechaNacimiento.hide()
        	self.eFechaNacimiento.hide()
        else:
            self.lPoblacion.hide()
            self.ePoblacion.hide()
            self.lSector.hide()
            self.eSector.hide()
            self.lTelefono2.hide()
            self.eTelefono2.hide()
            self.lRelacion.hide()
            self.eRelacion.hide()
            self.lFechaSalida.hide()
            self.eFechaSalida.hide()
            self.lCertificado.hide()
            self.eCertificado.hide()
            self.eComentarios.hide()

        if self.idUser != None:
            self.cargarDatos()
            self.rolUser = self.eRol.text()
            #print(self.eRol.text())
            self.bGuardarYSalir.clicked.connect(self.actualizar)
        else:
            self.bGuardarYSalir.clicked.connect(self.insertar)


    def salir(self):
        self.parent.show()
        self.close()

    def cargarDatos(self):
        db= BDOperaciones()
        usuario=db.getUsuario(self.idUser)
        self.eUsuario.setText(usuario[1])
        self.eClave.setText(usuario[2])
        self.eRol.setText(usuario[3])
        self.ePermiso.setText(usuario[4])
        if usuario[3]=="Socio":
            socio=db.getSocio(self.idUser)
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
            self.eFechaAlta.setText(socio[15].strftime('%Y-%m-%d') if (socio[15]!=None) else '')
            self.eFechaSalida.setText(socio[16].strftime('%Y-%m-%d') if (socio[16]!=None) else '')
            self.eComentarios.setText(socio[17])
        else:
            v=db.getVoluntario(self.idUser)
            #print(v)
            self.eNombre.setText(v[1])
            self.eApellidos.setText(v[2])
            self.eNif.setText(v[3])
            self.eFechaNacimiento.setText(v[4].strftime('%Y-%m-%d') if (v[4]!=None) else '')
            self.eFechaAlta.setText(v[5].strftime('%Y-%m-%d') if (v[5]!=None) else '')
            self.eCorreoElectronico.setText(v[6])
            self.eTelefono1.setText(v[7])
            self.eDireccion.setText(v[8])
            self.eCodigoPostal.setText(v[9])
            self.eProvincia.setText(v[10])
            self.eEstado.setText(v[11])

    def actualizar(self):
        datosUsuario, datosOtros = self.leerDatos()

        db = BDOperaciones()
        db.actualizarUsuario(datosUsuario, datosOtros, self.idUser, self.rolUser)
        self.salir()

    def insertar(self):
        datosUsuario, datosOtros = self.leerDatos()

        db = BDOperaciones()
        db.insertarUsuario(datosUsuario, datosOtros)
        self.salir()

    def leerDatos(self):
        datosUsuario = [self.eUsuario.text(),self.eClave.text(),self.eRol.text(),self.ePermiso.text()]
        for data in datosUsuario:
            data = data if (data != None) else ''

        datosOtros = []
        if self.rolUser == 'Socio':
            ds1=[self.eNombre.text(),self.eApellidos.text(),self.eNif.text(),self.eDireccion.text()]
            ds2=[self.ePoblacion.text(),self.eCodigoPostal.text(),self.eProvincia.text(),self.eEstado.text()]
            ds3=[self.eTelefono1.text(), self.eTelefono2.text(),self.eCorreoElectronico.text(),self.eRelacion.text()]
            ds4=[self.eCertificado.text(), self.eSector.text(),self.eFechaAlta.text(),self.eFechaSalida.text(),self.eComentarios.toPlainText()]
            datosOtros=ds1+ds2+ds3+ds4
            for data in datosOtros:
                data = data if (data != None) else ''
        else:
            dv1=[self.eNombre.text(),self.eApellidos.text(),self.eNif.text(),self.eFechaNacimiento.text()]
            dv2=[self.eFechaAlta.text(),self.eCorreoElectronico.text(),self.eTelefono1.text(),self.eDireccion.text()]
            dv3=[self.eCodigoPostal.text(),self.eProvincia.text(),self.eEstado.text()]
            datosOtros=dv1+dv2+dv3
            for data in datosOtros:
                data = data if (data != None) else ''
        return datosUsuario, datosOtros


if __name__ == '__main__':
    app = QApplication(sys.argv)
    perfilUsuarioW = PerfilUsuario()
    perfilUsuarioW.show()
    sys.exit(app.exec_())
