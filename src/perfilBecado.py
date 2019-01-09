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
    def __init__(self, id=None, modo = 'aniadir'):
        super(base_1, self).__init__()
        self.setupUi(self)
        self.idjoven = id
        self.joven = Joven.getJoven(self.idjoven)
        self.datos = []
        self.modo = modo
        self.bSalirSinGuardar.clicked.connect(self.salirSinGuardar)
        self.bGuardarYSalir.clicked.connect(self.guardarYSalir)
        if self.idjoven != None:
            self.cargarDatos()

        self.joven = Joven.getJoven(self.idjoven)

    def salirSinGuardar(self):
        self.child = WarningSalirSinGuardar(self)
        self.child.show()

    def salir(self):
        self.close()

    def cargarDatos(self):
        self.joven = Joven.getJoven(self.idjoven)
        self.eNombre.setText(self.joven.getNombre() if (self.joven.getNombre() != None) else '')
        self.eApellidos.setText(self.joven.getApellido() if (self.joven.getApellido() != None) else '')
        self.eNombrePadre.setText(self.joven.getNombrePadre() if (self.joven.getNombrePadre() != None) else '')
        self.eNombreMadre.setText(self.joven.getNombreMadre() if (self.joven.getNombreMadre() != None) else '')
        self.eUrlFoto.setText(str(self.joven.getFoto()) if (self.joven.getFoto() != None) else '')
        self.eFechaNacimiento.setText(str(self.joven.getFechaNacimiento()) if (self.joven.getFechaNacimiento() != None) else '')
        self.eFechaAltaAcoes.setText(str(self.joven.getFechaAltaACOES()) if (self.joven.getFechaAltaACOES() != None) else '')
        self.eFechaAlta.setText(str(self.joven.getFechaAlta()) if (self.joven.getFechaAlta() != None) else '')
        self.eFechaSalidaAcoes.setText(str(self.joven.getFechaSalidaACOES()) if (self.joven.getFechaSalidaACOES() != None) else '')
        self.eGrado.setText(str(self.joven.getGrado()) if (self.joven.getGrado() != None) else '')
        c1 = self.joven.getColoniaNacimiento().getNombre()
        self.eColoniaNacimiento.setText(c1 if (c1 != None) else '')
        c2 = self.joven.getColoniaResidencia().getNombre()
        self.eColoniaResidencia.setText(c2 if (c2 != None) else '')
        c3 = self.joven.getColegio().getNombreDeColegio()
        self.eColegio.setText(c3 if (c3 != None) else '')
        self.eHistorial.setText(self.joven.getHistorial() if (self.joven.getHistorial() != None) else '')
        self.eObservaciones.setText(self.joven.getObservaciones() if (self.joven.getObservaciones() != None) else '')
        if self.modo != 'aniadir':
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
        if self.modo != 'aniadir':
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
                    habitantesantiguo = self.joven.getColoniaNacimiento().getNumeroDeHabitantes()
                    self.joven.getColoniaNacimiento().setNumeroDeHabitantes(habitantesantiguo - 1)
                    id = bd.maxId('id_colonia', 'colonia')
                    id += 1
                    self.joven.setColoniaNacimiento(Colonia.newColonia(id, self.eColoniaNacimiento.text(), 0))
                if self.datos[11] != self.eColoniaResidencia.text():
                    habitantesantiguo = self.joven.getColoniaNacimiento().getNumeroDeHabitantes()
                    self.joven.getColoniaResidencia().setNumeroDeHabitantes(habitantesantiguo - 1)
                    id = bd.maxId('id_colonia', 'colonia')
                    id += 1
                    self.joven.setColoniaResidencia(Colonia.newColonia(id, self.eColoniaNacimiento.text(), 1))
                if self.datos[12] != self.eColegio.text():
                    id = bd.maxId('id_colegio', 'colegio')
                    id += 1
                    self.joven.setColegio(Colegio.newColegio(id, False, self.eColegio.text(), 1))
                if self.datos[13] != self.eHistorial.toPlainText():
                    self.joven.setHistorial(self.eHistorial.toPlainText())
                if self.datos[14] != self.eObservaciones.toPlainText():
                    self.joven.setObservaciones(self.eObservaciones.text())

        else:
            if self.eNombre.text() == '' or self.eApellidos.text() == '' or self.eFechaAltaAcoes.text() == '' or self.eColoniaNacimiento.text() == '' or self.eColoniaResidencia.text() == '' or self.eColegio.text() == '':
                print('Error: faltan datos obligatorios.')
                self.child = WarningDatosSinRellenar(self)
                self.child.show()
                return False
            else:
                n1 = self.eNombre.text()
                a1 = self.eApellidos.text()
                n2 = self.eNombrePadre.text()
                n3 = self.eNombreMadre.text()
                e1 = self.eEstado.text()
                u1 = self.eUrlFoto.text()
                f1 = self.eFechaNacimiento.text()
                f2 = self.eFechaAltaAcoes.text()
                f3 = self.eFechaAlta.text()
                f4 = self.eFechaSalidaAcoes.text()
                g1 = self.eGrado.text()

                bd = BDOperaciones()
                id = bd.maxId('id_colonia', 'colonia')
                id += 1
                nc1 = Colonia.newColonia(id, self.eColoniaNacimiento.text(), 1)

                if self.eColoniaNacimiento.text() != self.eColoniaResidencia.text():
                    id = bd.maxId('id_colonia', 'colonia')
                    id += 1
                    nc2 = Colonia.newColonia(id, self.eColoniaResidencia.text(), 1)
                else:
                    nc2 = nc1

                id = bd.maxId('id_colegio', 'colegio')
                id += 1
                nc3 = self.Colegio.newColegio(id, False, self.eColegio.text(), 1)
                h1 = self.eHistorial.toPlainText()
                o1 = self.eObservaciones.toPlainText()

                id = bd.maxId('id_usuario', 'usuario')
                id += 1
                self.joven = Joven.newJoven(idJoven = id, nombre = n1, apellidos = a1, nombrePadre = n2, nombreMadre = n3, estado = e1, urlFoto = u1, fechaNacimiento=f1, fechaAlta=f2, fechaAltaACOES=f3, fechaSalidaACOES=f4, grado=g1, historial=h1, observaciones=o1, coloniaNacimiento=nc1, coloniaResidencia=nc2, colegio=nc3)
                '''
                Falta comprobar si el colegio y colonia que se estan creando ya estan en la base de datos.
                Falta comprobar si funciona la creacion de joven.
                Falta añadir un individuo mas a la colonia si se inserta en una ya existente.
                Falta pedir a que colonia pertenece el colegio.
                '''

        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    perfilBecadoW = PerfilBecado()
    perfilBecadoW.show()
    sys.exit(app.exec_())

