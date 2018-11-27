import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from BD.BDOperaciones import BDOperaciones
from BD.BD import BD
import recursosQT_rc

form_1, base_1 = uic.loadUiType('UI/perfilUsuario.ui')

class PerfilUsuario(base_1, form_1):
    def __init__(self, parent = None, id = None):
        super(base_1,self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.id = id
        self.bSalirSinGuardar.clicked.connect(self.salir)
        self.bGuardarYSalir.clicked.connect(self.actualizar)
        if self.id != None:
            db= BDOperaciones()
            usuario=db.getUsuario(self.id)
            self.eUsuario.setText(usuario[1])
            self.eClave.setText(usuario[2])
            self.eRol.setText(usuario[3])
            self.ePermiso.setText(usuario[4])
            if usuario[3]=="Socio":
            	socio=db.getSocio(self.id)
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
            else:
            	v=db.getVoluntario(self.id)
            	self.eNombre.setText(v[1])
            	self.eApellidos.setText(v[2])
            	self.eNif.setText(v[3])
            	self.eDireccion.setText(v[8])
            	self.eCodigoPostal.setText(v[9])
            	self.eProvincia.setText(v[10])
            	self.eEstado.setText(v[12])
            	self.eTelefono1.setText(v[7])
            	self.eCorreoElectronico.setText(v[6])
            	self.eFechaAlta.setText(v[5].strftime('%Y-%m-%d'))
            	self.eFechaNacimiento.setText(v[4].strftime('%Y-%m-%d'))



    def salir(self):
        self.parent.show()
        self.hide()

    def actualizar(self):
    	db=BD()
    	datosUsuario= [self.eUsuario.text(),self.eClave.text(),self.eRol.text(),self.ePermiso.text()]
    	ds1=[self.eNombre.text(),self.eApellidos.text(),self.eNif.text(),self.eDireccion.text()]
    	ds2=[self.ePoblacion.text(),self.eCodigoPostal.text(),self.eProvincia.text(),self.eEstado.text()]
    	ds3=[self.eTelefono1.text(), self.eTelefono2.text(),self.eCorreoElectronico.text(),self.eRelacion.text()]
    	ds4=[self.eCertificado.text(), self.eSector.text(),self.eFechaAlta.text(),self.eFechaSalida.text(),self.eComentarios.text()]
    	datosSocio=ds1+ds2+ds3+ds4
    	dv1=[self.eNombre.text(),self.eApellidos.text(),self.eNif.text(),self.eFechaNacimiento.text()]
    	dv2=[self.eFechaAlta.text(),self.eCorreoElectronico.text(),self.eTelefono1.text(),self.eDireccion.text()]
    	dv3=[self.eCodigoPostal.text(),self.eProvincia.text(),None,self.eEstado.text()]
    	datosVoluntario=dv1+dv2+dv3


    	if self.id != None:
    		db.delete('usuario', 'id_usuario='+str(self.id))
    		db.delete('socio', 'id_socio='+str(self.id))
    		db.delete('voluntario','id_voluntario='+str(self.id))


    	db.insert(datosUsuario,"usuario")
    	if self.eRol.text()=="socio":
    		db.insert(datosSocio,"socio")
    	else:
    		db.insert(datosVoluntario,"voluntario")


    	self.parent.show()
    	self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    perfilUsuarioW = PerfilUsuario()
    perfilUsuarioW.show()
    sys.exit(app.exec_())
