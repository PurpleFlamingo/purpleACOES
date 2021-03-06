import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from BD.BDOperaciones import BDOperaciones
from BD.Usuario import Usuario
from BD.Socio import Socio
from BD.BD import BD
from BD.Voluntario import Voluntario
from warningDatosSinRellenar import WarningDatosSinRellenar
from warningSalirSinGuardar import WarningSalirSinGuardar
from cambiarContraseña import CambiarContrasenia
import recursosQT_rc
import time

form_1, base_1 = uic.loadUiType('UI/perfilUsuario.ui')

class PerfilUsuario(base_1, form_1):
    def __init__(self, parent = None, id = None, rol = None, rolUsuarioSesion = None):
        super(base_1,self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.idUser = id
        self.rolUser = rol
        self.bSalirSinGuardar.clicked.connect(self.salirSinGuardar)

        #rol del usuario que ha iniciado la sesión
        self.rolUsuarioSesion = rolUsuarioSesion

        self.eCertificado.setText('No')
        

        self.eRol.setText(self.rolUser)
        if(self.rolUser == 'Socio'):
            self.ePermiso.setText('Socio')
            self.eEstado.setText('España')
        self.eRol.setEnabled(False)

        if(self.rolUser == 'Coordinador General'):
            self.ePermiso.setText('General')
        
        if self.rolUsuarioSesion == 'Socio':
            self.eFechaAlta.setEnabled(False)
            self.eFechaSalida.setEnabled(False)
            self.lPermiso.hide()
            self.ePermiso.hide()
            self.lRol.hide()
            self.eRol.hide()

        if self.rolUser == 'Socio' :
            self.lFechaNacimiento.hide()
       	    self.eFechaNacimiento.hide()
        else:
            self.lComentario.hide()
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
            #cambiar contraseña
            self.eClave.hide()
            self.eClave2.hide()
            self.lClave_2.hide()            
            self.bCambiarClave.clicked.connect(self.cambioDeClave)
        else:
            self.eFechaAlta.setText(str(time.strftime('%Y-%m-%d')))
            self.bGuardarYSalir.clicked.connect(self.insertar)
            self.bCambiarClave.hide()

        


    def cambioDeClave(self):
        self.child = CambiarContrasenia(self.idUser)
        self.child.show()

    def salirSinGuardar(self):
        self.child = WarningSalirSinGuardar(self)
        self.child.show()

    def salir(self):
        self.parent.show()
        self.close()

    def cargarDatos(self):
        db= BDOperaciones()
        self.usuario = Usuario.getUsuario(self.idUser)
        #usuario=db.getUsuario(self.idUser)
        self.eUsuario.setText(self.usuario.getNombre())
        self.eRol.setText(self.usuario.getRolId())
        self.ePermiso.setText(self.usuario.getPermisoId())
        if self.rolUser == "Socio":
            self.socio = Socio.getSocio(self.idUser)
            self.eNombre.setText(self.socio.getNombreDePila())
            self.eApellidos.setText(self.socio.getApellidos())
            self.eNif.setText(self.socio.getNif())
            self.eDireccion.setText(self.socio.getDireccion())
            self.ePoblacion.setText(self.socio.getPoblacion())
            self.eCodigoPostal.setText(self.socio.getCodigoPostal())
            self.eProvincia.setText(self.socio.getProvincia())
            self.eEstado.setText(self.socio.getEstado())
            self.eTelefono1.setText(self.socio.getTelefono1())
            self.eTelefono2.setText(self.socio.getTelefono2())
            self.eCorreoElectronico.setText(self.socio.getCorreoElectronico())
            self.eRelacion.setText(str('Si' if self.socio.getRelacion() else 'No'))
            self.eCertificado.setText(str('Si' if self.socio.getCertificado() else 'No'))
            self.eSector.setText(self.socio.getSector())
            self.eFechaAlta.setText(self.socio.getFechaDeAlta() if (self.socio.getFechaDeAlta() != None) else '')
            self.eFechaSalida.setText(self.socio.getFechaDeBaja() if (self.socio.getFechaDeBaja() != None) else '')
            self.eComentarios.setText(self.socio.getObservaciones())
        else:
            v=db.getVoluntario(self.idUser)
            #print(v)
            self.eNombre.setText(v[1])
            self.eApellidos.setText(v[2])
            self.eNif.setText(v[3])
            self.eFechaNacimiento.setText(v[4].strftime('%Y-%m-%d') if (v[4]!=None) else '')
            self.eFechaAlta.setText(v[5].strftime('%Y-%m-%d') if (v[5] != None) else '')
            self.eCorreoElectronico.setText(v[6])
            self.eTelefono1.setText(v[7])
            self.eDireccion.setText(v[8])
            self.eCodigoPostal.setText(v[9])
            self.eProvincia.setText(v[10])
            self.eEstado.setText(v[11])
        
        



    def actualizar(self):
        datosUsuario, datosOtros = self.leerDatos()
         
        if self.rolUser == "Socio":
            #print(datosUsuario)
            #Compruebo si los datos obligatorios estan vacios y si lo estan muestro un mensaje error que no permite guardar los cambios
            #que se hayan hecho hasta que todos los campos obligatorios tengan información en ellos
            
            if not datosUsuario[0] or not datosUsuario[1] or not datosUsuario[2] or not datosOtros[0] or not datosOtros[1] or not datosOtros[2] or not datosOtros[3] or not datosOtros[4] or not datosOtros[5] or not datosOtros[6] or not datosOtros[7] or not datosOtros[10] or not datosOtros[14]:
                print('Error: faltan datos obligatorios')
                self.child = WarningDatosSinRellenar(self)
                self.child.show()
                return False
            
            #Compruebo que el nombre de usuario nuevo no se encuentre en la tabla usuarios
            condicion = 'nombre = \'' + datosUsuario[0] + '\''
            #print('Condicion de control: '+condicion)
            resultado = Usuario.estaEnLaTabla('usuario', condicion)
            #print('Resultado :',resultado)
            #si el nombre de usuario ya se encuentra en uso se muestra un mensaje comunicando este hecho y no permitiendo guardar hasta
            #que se ingrese un nombre de usuario que no este en uso
            if datosUsuario[0] != self.usuario.getNombre() and resultado:
                print('Error: Nombre de usuario ya utilizado')
                self.child = WarningDatosSinRellenar(self, "Usuario")
                self.child.show()
                return False

            #se comprueba que se hayan realizado cambios y se procede a actualizar los datos que se hayan modificado
            if self.usuario.getNombre() != datosUsuario[0]:
                self.usuario.setNombre(datosUsuario[0])
            if self.usuario.getRolId() != datosUsuario[1]:
                self.usuario.setNombre(datosUsuario[1])
            if self.usuario.getPermisoId() != datosUsuario[2]:
                self.usuario.setNombre(datosUsuario[2])

            if self.socio.getNombreDePila() != datosOtros[0]:
                self.socio.setNombrePila(datosOtros[0])
            if self.socio.getApellidos() != datosOtros[1]:
                self.socio.setApellidos(datosOtros[1])
            if self.socio.getNif() != datosOtros[2]:
                self.socio.setNif(datosOtros[2])
            if self.socio.getDireccion() != datosOtros[3]:
                self.socio.setDireccion(datosOtros[3])
            if self.socio.getPoblacion() != datosOtros[4]:
                self.socio.setPoblacion(datosOtros[4])
            if self.socio.getCodigoPostal() != datosOtros[5]:
                self.socio.setCodigoPostal(datosOtros[5])
            if self.socio.getProvincia() != datosOtros[6]:
                self.socio.setProvincia(datosOtros[6])
            if self.socio.getEstado() != datosOtros[7]:
                self.socio.setEstado(datosOtros[7])
            if self.socio.getTelefono1() != datosOtros[8]:
                self.socio.setTelefono1(datosOtros[8])
            if self.socio.getTelefono2() != datosOtros[9]:
                self.socio.setTelefono2(datosOtros[9])
            if self.socio.getCorreoElectronico() != datosOtros[10]:
                self.socio.setCorreoElectronico(datosOtros[10])
            if self.socio.getRelacion() != datosOtros[11]:
                if datosOtros[12].lower() == 'si':
                    datosOtros[12] = 1
                elif datosOtros[12].lower() == 'no':
                    datosOtros[12] = 0
                self.socio.setRelacion(datosOtros[11])
            if self.socio.getCertificado() != datosOtros[12]:
                if datosOtros[12].lower() == 'si':
                    datosOtros[12] = 1
                elif datosOtros[12].lower() == 'no':
                    datosOtros[12] = 0
                self.socio.setCertificado(datosOtros[12])
            if self.socio.getSector() != datosOtros[13]:
                self.socio.setSector(datosOtros[13])
            if self.socio.getFechaDeAlta != datosOtros[14]:
                self.socio.setFechaDeAlta(datosOtros[14])
            if self.rolUsuarioSesion != 'Socio' and self.socio.getFechaDeBaja != datosOtros[15]:
                self.socio.setFechaDeBaja(datosOtros[15])
            if self.socio.getObservaciones() != datosOtros[16]:
                self.socio.setObservaciones(datosOtros[16])

            self.salir()


        else:
            #db = BDOperaciones()
            #db.actualizarUsuario(datosUsuario, datosOtros, self.idUser, self.rolUser)
            pass
        self.salir()

    def insertar(self):
        if self.eClave.text() != self.eClave2.text():
            print('Error: Las claves no son iguales')
            self.child = WarningDatosSinRellenar(self, 'Clave')
            self.child.show()
            return False

        datosUsuario, datosOtros = self.leerDatos()
        #bd = BD()
        #resultado = ' MAX(id_usuario) '
        #user = bd.selectEscalar(resultado,'usuario',None)[0] + 1
        #datosOtros = [user] + datosOtros
        #for i in datosOtros:
            #print('datosOtros',i)
        #print("newUser = ",newUser)
        newUser = Usuario.newUsuario(datosUsuario[0],datosUsuario[1],datosUsuario[2],datosUsuario[3])
        #print("La id de newUser es ",newUser.getIdUsuario())
        if(newUser):
            if(self.rolUser == 'Socio'):
                if not datosUsuario[0] or not datosUsuario[1] or not datosUsuario[2] or not datosOtros[0] or not datosOtros[1] or not datosOtros[2] or not datosOtros[3] or not datosOtros[4] or not datosOtros[5] or not datosOtros[6] or not datosOtros[7] or not datosOtros[10] or not datosOtros[14]:
                    print('Error: faltan datos obligatorios')
                    self.child = WarningDatosSinRellenar(self)
                    self.child.show()
                    return False

                Socio.newSocio(newUser.getIdUsuario(), datosOtros[0], datosOtros[1], datosOtros[2], datosOtros[3],
                           datosOtros[4], datosOtros[5], datosOtros[6], datosOtros[7], datosOtros[8], datosOtros[9], datosOtros[10], datosOtros[11], 1 if datosOtros[12] == 'Si' else 0, datosOtros[13], datosOtros[14], datosOtros[15], datosOtros[16], datosOtros[17])
            else:
                Voluntario.newVoluntario(newUser.getIdUsuario(),datosOtros[0],datosOtros[1],datosOtros[2],datosOtros[3],datosOtros[4],datosOtros[5],datosOtros[6],datosOtros[7],datosOtros[8],datosOtros[9],datosOtros[10])
        else:
            print('Error: El usuario ya existe')
            self.child = WarningDatosSinRellenar(self, 'Usuario')
            self.child.show()
            return False

        #db = BDOperaciones()
        #db.insertarUsuario(datosUsuario, datosOtros)
        self.salir()

    def leerDatos(self):
        if self.idUser != None:
            datosUsuario = [self.eUsuario.text(),self.eRol.text(),self.ePermiso.text()]
        else:
            datosUsuario = [self.eUsuario.text(),self.eClave.text(),self.eRol.text(),self.ePermiso.text()]
        #for data in datosUsuario:
        #    data = data if (data != None) else ''

        datosOtros = []
        if self.rolUser == 'Socio':
            #print('La fecha de alta leida es :',self.eFechaAlta.text())
            cuota = 0
            ds1=[self.eNombre.text(),self.eApellidos.text(),self.eNif.text(),self.eDireccion.text()]
            ds2=[self.ePoblacion.text(),self.eCodigoPostal.text(),self.eProvincia.text(),self.eEstado.text()]
            ds3=[self.eTelefono1.text(), self.eTelefono2.text(),self.eCorreoElectronico.text(),self.eRelacion.text()]
            ds4=[self.eCertificado.text(), self.eSector.text(), self.eFechaAlta.text(),self.eFechaSalida.text() if self.eFechaSalida.text() != '' else None,self.eComentarios.toPlainText(), cuota]
            datosOtros=ds1+ds2+ds3+ds4
            #print('La fecha de alta en el array es: ',datosOtros[14])
         #   for data in datosOtros:
         #       data = data if (data != None) else ''
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
