import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from BD.BDOperaciones import BDOperaciones
from BD.Joven import Joven
from BD.Colonia import Colonia
from BD.Colegio import Colegio
from warningDatosSinRellenar import WarningDatosSinRellenar
from warningSalirSinGuardar import WarningSalirSinGuardar

form_1, base_1 = uic.loadUiType('UI/perfilBecado.ui')


class PerfilBecado(base_1, form_1):
    def __init__(self, id=None):
        super(base_1, self).__init__()
        self.setupUi(self)
        self.col = Colonia()
        self.coleg = Colegio()
        self.idjoven = id
        self.joven = Joven.getJoven(self.idjoven)
        self.datos = []
        self.bSalirSinGuardar.clicked.connect(self.salirSinGuardar)
        self.bGuardarYSalir.clicked.connect(self.guardarYSalir)
        if self.idjoven != None:
            self.cargarDatos()

    def salirSinGuardar(self):
        self.child = WarningSalirSinGuardar(self)
        self.child.show()

    def salir(self):
        self.close()

    def cargarDatos(self):
        self.joven = Joven.getJoven(self.idjoven)
        self.eNombre.setText(self.joven.getNombre())
        self.eApellidos.setText(self.joven.getApellido())
        self.eNombrePadre.setText(self.joven.getNombrePadre() if (self.joven.getNombrePadre() != None) else '')
        self.eNombreMadre.setText(self.joven.getNombreMadre() if (self.joven.getNombreMadre() != None) else '')
        self.eUrlFoto.setText(str(self.joven.getFoto()) if (self.joven.getFoto() != None) else '')
        self.eFechaNacimiento.setText(
            str(self.joven.getFechaNacimiento()) if (self.joven.getFechaNacimiento() != None) else '')
        self.eFechaAltaAcoes.setText(str(self.joven.getFechaAltaACOES()))
        self.eFechaAlta.setText(str(self.joven.getFechaAlta()) if (self.joven.getFechaAlta() != None) else '')
        self.eFechaSalidaAcoes.setText(
            str(self.joven.getFechaSalidaACOES()) if (self.joven.getFechaSalidaACOES() != None) else '')
        self.eGrado.setText(str(self.joven.getGrado()) if (self.joven.getGrado() != None) else '')
        self.eColoniaNacimiento.setText(
            self.col.getColonia(self.joven.getColoniaNacimiento().getIdColonia()).getNombre())
        self.eColoniaResidencia.setText(
            self.col.getColonia(self.joven.getColoniaResidencia().getIdColonia()).getNombre())
        self.eColegio.setText(self.coleg.getColegio(self.joven.getColegio().getIdColegio()).getNombreDeColegio())
        self.eHistorial.setText(self.joven.getHistorial() if (self.joven.getHistorial() != None) else '')
        self.eObservaciones.setText(self.joven.getObservaciones() if (self.joven.getObservaciones() != None) else '')
        self.datos.append(self.eNombre.text())
        self.datos.append(self.eApellidos.text())
        self.datos.append(self.eNombrePadre.text())
        self.datos.append(self.eNombreMadre.text())
        self.datos.append(self.eUrlFoto.text())
        self.datos.append(self.eFechaNacimiento.text())
        self.datos.append(self.eFechaAltaAcoes.text())
        self.datos.append(self.eFechaAlta.text())
        self.datos.append(self.eFechaSalidaAcoes.text())
        self.datos.append(self.eGrado.text())
        self.datos.append(self.eColoniaNacimiento.text())
        self.datos.append(self.eColoniaResidencia.text())
        self.datos.append(self.eColegio.text())
        self.datos.append(self.eHistorial.toPlainText())
        self.datos.append(self.eObservaciones.toPlainText())

    def guardarYSalir(self):
        if self.eNombre.text() == '' or self.eApellidos.text() == '' or self.eFechaAltaAcoes.text() == '' or self.eColoniaNacimiento.text() == '' or self.eColoniaResidencia.text() == '' or self.eColegio.text() == '':
            print('Error: faltan datos obligatorios.')
            self.child = WarningDatosSinRellenar(self)
            self.child.show()
            return False
        else:
            if self.datos[0] != self.eNombre.text():
                self.joven.setNombre(self.eNombre.text())
            if self.datos[1] != self.eApellidos.text():
                self.joven.setApellido(self.eApellidos.text())
            if self.datos[2] != self.eNombrePadre.text():
                self.joven.setNombrePadre(self.eNombrePadre.text())
            if self.datos[3] != self.eNombreMadre.text():
                self.joven.setNombreMadre(self.eNombreMadre.text())
            if self.datos[4] != self.eUrlFoto.text():
                self.joven.setFoto(self.eUrlFoto.text())
            if self.datos[5] != self.eFechaNacimiento.text():
                self.joven.setFechaNacimiento(self.eFechaNacimiento.text())
            if self.datos[6] != self.eFechaAltaAcoes.text():
                self.joven.setFechaAltaACOES(self.eFechaAltaAcoes.text())
            if self.datos[7] != self.eFechaAlta.text():
                self.joven.setFechaAlta(self.eFechaAlta.text())
            if self.datos[8] != self.eFechaSalidaAcoes.text():
                self.joven.setFechaSalidaACOES(self.eFechaSalidaAcoes.text())
            if self.datos[9] != self.eGrado.text():
                self.joven.setGrado(self.eGrado.text())
            if self.datos[10] != self.eColoniaNacimiento.text():
                bd = BDOperaciones()
                idantigua = self.col.getColonia(self.joven.getColoniaNacimiento().getIdColonia())
                coloniaantigua = self.col.getColonia(idantigua)
                habitantesantiguo = coloniaantigua.getNumeroDeHabitantes()
                coloniaantigua.setNumeroDeHabitantes(habitantesantiguo - 1)
                id = bd.maxId('id_colonia', 'colonia')
                id += 1
                self.col.newColonia(id, self.eColoniaNacimiento.text(), 1)
                nuevacolonia = self.col.getColonia(id)
                self.joven.setColoniaNacimiento(nuevacolonia)
            '''
            self.joven.setColoniaResidencia(self.eColoniaResidencia.text())
            self.joven.setColegio(self.eColegio.text())
            self.joven.setHistorial(self.eHistorial.text())
            self.joven.setObservaciones(self.eObservaciones.text())
            '''
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    perfilBecadoW = PerfilBecado(1)
    perfilBecadoW.show()
    sys.exit(app.exec_())

