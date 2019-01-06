import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from BD.Joven import Joven
from warningDatosSinRellenar import WarningDatosSinRellenar
from warningSalirSinGuardar import WarningSalirSinGuardar

form_1, base_1 = uic.loadUiType('UI/perfilBecado.ui')

class PerfilBecado(base_1, form_1):
    def __init__(self, id_joven = None,  parent = None, rol = None):
        super(base_1, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.rolUser = rol
        self.idjoven = id_joven
        self.bSalirSinGuardar.clicked.connect(self.salirSinGuardar)

        if self.idjoven != None:
            self.cargarDatos()
            self.bGuardarYSalir.clicked.connect(self.guardarYSalir)

        self.joven = None

    def salirSinGuardar(self):
        self.child = WarningSalirSinGuardar(self)
        self.child.show()

    def salir(self):
        self.parent.show()
        self.close()

    def cargarDatos(self):
        self.joven = Joven.getJoven(self.idjoven)
        self.eNombre.setText(self.joven.getNombre())
        self.eApellidos.setText(self.joven.getApellido())
        self.eNombrePadre.setText(self.joven.getNombrePadre() if (self.joven.getNombrePadre() != None) else '')
        self.eNombreMadre.setText(self.joven.getNombreMadre() if (self.joven.getNombreMadre() != None) else '')
        self.eUrlFoto.setText(self.joven.getFoto() if (self.joven.getFoto() != None) else '')
        self.eFechaNacimiento(self.joven.getFechaNacimiento() if (self.joven.getFechaNacimiento() != None) else '')
        self.eFechaAltaAcoes(self.joven.getFechaAltaACOES())
        self.eFechaAlta(self.joven.getFechaAlta() if (self.joven.getFechaAlta() != None) else '')
        self.eFechaSalidaAcoes(self.joven.getFechaSalidaACOES() if (self.joven.getFechaSalidaACOES() != None) else '')
        self.eGrado(self.joven.getGrado() if (self.joven.getGrado() != None) else '')
        self.eColoniaNacimiento(self.joven.getColoniaNacimiento())
        self.eColoniaResidencia(self.joven.getColoniaResidencia())
        self.eColegio(self.joven.getColegio())
        self.eHistorial(self.joven.getHistorial() if (self.joven.getHistorial() != None) else '')
        self.eObservaciones(self.joven.getObservaciones() if (self.joven.getObservaciones() != None) else '')

    def guardarYSalir(self):
        if self.eNombre.text() == '' or self.eApellidos.text() == '' or self.eFechaAltaAcoes.text() == '' or self.eColoniaNacimiento.text() == '' or self.eColoniaResidencia.text() == '' or self.e.Colegio.text() == '':
            print('Error: faltan datos obligatorios.')
            self.child = WarningDatosSinRellenar(self)
            self.child.show()
            return False
        else:
            self.joven.setNombre(self.eNombre.text())
            self.joven.setApellido(self.eApellidos.text())
            self.joven.setNombrePadre(self.eNombrePadre.text())
            self.joven.setNombreMadre(self.eNombreMadre.text())
            self.joven.setFoto(self.eUrlFoto.text())
            self.joven.setFechaNacimiento(self.eFechaNacimiento.text())
            self.joven.setFechaAltaACOES(self.eFechaAltaAcoes.text())
            self.joven.setFechaAlta(self.eFechaAlta.text())
            self.joven.setFechaSalidaACOES(self.eFechaSalidaAcoes.text())
            self.joven.setGrado(self.eGrado.text())
            self.joven.setColoniaNacimiento(self.eColoniaNacimiento.text())
            self.joven.setColoniaResidencia(self.eColoniaResidencia.text())
            self.joven.setColegio(self.eColegio.text())
            self.joven.setHistorial(self.eHistorial.text())
            self.joven.setObservaciones(self.eObservaciones.text())


if __name__== '__main__':
    app = QApplication(sys.argv)
    perfilBecadoW = PerfilBecado()
    perfilBecadoW.show()
    sys.exit(app.exec_())
