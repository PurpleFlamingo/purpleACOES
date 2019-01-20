import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QHeaderView
from BD.BDOperaciones import BDOperaciones
from BD.Apadrinamiento import Apadrinamiento
from BD.Joven import Joven
from BD.Socio import Socio
from warningDatosSinRellenar import WarningDatosSinRellenar
from warningSalirSinGuardar import WarningSalirSinGuardar
from warningNoUserSelected import WarningNoUserSelected

form_1, base_1 = uic.loadUiType('UI/perfilApadrinamiento.ui')


class PerfilApadrinamientos(base_1, form_1):
    def __init__(self, id = None, iduser = None, modo = 'aniadir'):
        super(base_1, self).__init__()
        self.setupUi(self)
        self.idApadrinamiento = id
        self.idUser = iduser
        self.apadrinamiento = Apadrinamiento.getApadrinamiento(self.idApadrinamiento)
        self.datos = []
        self.child = None
        self.modo = modo
        self.cabeceras1 = ['Nombre', 'Apellidos', 'Provincia', 'Pais']
        self.cabeceras2 = ['Nombre', 'Apellidos', 'Estado', 'Fecha Nacimiento', 'Grado', 'Colonia de Nacimiento',
                          'Colonia de Residencia', 'Colegio']
        self.socios = Socio.listaSocios()
        self.jovenes = Joven.listaJovenes()
        self.bSalirSinGuardar.clicked.connect(self.salirSinGuardar)
        self.bGuardarYSalir.clicked.connect(self.guardarYSalir)
        self.bCambiar.clicked.connect(self.cambiar)
        if self.idApadrinamiento != None:
            self.cargarDatos()
            self.socio = self.apadrinamiento.getSocio()
            self.becado = Joven.getJoven(self.apadrinamiento.getJoven())
        else:
            self.cargarTabla()

    def salirSinGuardar(self):
        self.child = WarningSalirSinGuardar(self)
        self.child.show()

    def salir(self):
        self.close()

    def cargarTabla(self):
        socios = Socio.listaSocios()
        jovenes = Joven.listaJovenes()

        self.tBecados.verticalHeader().hide()
        self.tBecados.setColumnCount(len(self.cabeceras2))
        self.tBecados.setRowCount(len(jovenes))
        self.tBecados.setHorizontalHeaderLabels(self.cabeceras2)
        self.tBecados.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

        self.tSocios.verticalHeader().hide()
        self.tSocios.setColumnCount(len(self.cabeceras1))
        self.tSocios.setRowCount(len(socios))
        self.tSocios.setHorizontalHeaderLabels(self.cabeceras1)
        self.tSocios.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

        for i, kid in enumerate(jovenes):
            nombre = kid.getNombre()
            if nombre != None:
                self.tBecados.setItem(i, 0, QTableWidgetItem(nombre))
            else:
                self.tBecados.setItem(i, 0, QTableWidgetItem(''))
            apellidos = kid.getApellido()
            if apellidos != None:
                self.tBecados.setItem(i, 1, QTableWidgetItem(apellidos))
            else:
                self.tBecados.setItem(i, 1, QTableWidgetItem(''))
            estado = kid.getEstado()
            if estado != None:
                self.tBecados.setItem(i, 2, QTableWidgetItem(estado))
            else:
                self.tBecados.setItem(i, 2, QTableWidgetItem(''))
            fechanacimiento = str(kid.getFechaNacimiento())
            if fechanacimiento != None:
                self.tBecados.setItem(i, 3, QTableWidgetItem(fechanacimiento))
            else:
                self.tBecados.setItem(i, 3, QTableWidgetItem(''))
            grado = kid.getGrado()
            if grado != None:
                self.tBecados.setItem(i, 4, QTableWidgetItem(grado))
            else:
                self.tBecados.setItem(i, 4, QTableWidgetItem(''))
            if kid.getColoniaNacimiento() != None:
                colon = kid.getColoniaNacimiento().getNombre()
                self.tBecados.setItem(i, 5, QTableWidgetItem(colon))
            else:
                self.tBecados.setItem(i, 5, QTableWidgetItem(''))
            if kid.getColoniaResidencia() != None:
                colon2 = kid.getColoniaResidencia().getNombre()
                self.tBecados.setItem(i, 6, QTableWidgetItem(colon2))
            else:
                self.tBecados.setItem(i, 6, QTableWidgetItem(''))
            if kid.getColegio() != None:
                colegio1 = kid.getColegio().getNombreDeColegio()
                self.tBecados.setItem(i, 7, QTableWidgetItem(colegio1))
            else:
                self.tBecados.setItem(i, 7, QTableWidgetItem(''))

        for i, socio in enumerate(socios):
            nombre = socio.getNombreDePila()
            if nombre != None:
                self.tSocios.setItem(i, 0, QTableWidgetItem(nombre))
            else:
                self.tSocios.setItem(i, 0, QTableWidgetItem(''))
            apellidos = socio.getApellidos()
            if apellidos != None:
                self.tSocios.setItem(i, 1, QTableWidgetItem(apellidos))
            else:
                self.tSocios.setItem(i, 1, QTableWidgetItem(''))
            provincia = socio.getProvincia()
            if provincia != None:
                self.tSocios.setItem(i, 2, QTableWidgetItem(provincia))
            else:
                self.tSocios.setItem(i, 2, QTableWidgetItem(''))
            pais = socio.getEstado()
            if pais != None:
                self.tSocios.setItem(i, 3, QTableWidgetItem(pais))
            else:
                self.tSocios.setItem(i, 3, QTableWidgetItem(''))

    def cargarDatos(self):
        self.apadrinamiento = Apadrinamiento.getApadrinamiento(self.idApadrinamiento)
        self.eBecado.setText((self.apadrinamiento.getJoven().getNombre() + ' ' + self.apadrinamiento.getJoven().getApellido()) if (self.apadrinamiento.getJoven().getNombre() != None) else '')
        self.eSocio.setText((self.apadrinamiento.getSocio().getNombreDePila() + ' ' + self.apadrinamiento.getSocio().getApellidos()) if (self.apadrinamiento.getSocio().getNombreDePila() != None) else '')
        self.eFechaInicio.setText(str(self.apadrinamiento.getFechaDeInicio()) if (str(self.apadrinamiento.getFechaDeInicio()) != None) else '')
        self.eFechaBaja.setText(str(self.apadrinamiento.getFechaDeBaja()) if (self.apadrinamiento.getFechaDeBaja() != None) else '')

        self.cargarTabla()

        if self.modo != 'aniadir':
            self.datos.append(self.eBecado.text())
            self.datos.append(self.eSocio.text())
            self.datos.append(self.eFechaInicio.text())
            self.datos.append(self.eFechaBaja.text())

    def guardarYSalir(self):
        if self.modo != 'aniadir':
            if self.eBecado.text() == '' or self.eSocio.text() == '' or self.eFechaInicio.text() == '':
                print('Error: faltan datos obligatorios.')
                self.child = WarningDatosSinRellenar(self)
                self.child.show()
                return False
            else:
                if self.datos[0] != self.eBecado.text():
                    self.apadrinamiento.setJoven(self.becado)
                if self.datos[1] != self.eSocio.text():
                    self.apadrinamiento.setSocio(self.socio)
                if self.datos[2] != self.eFechaInicio.text():
                    self.apadrinamiento.setFechaDeInicio(self.eFechaInicio.text())
                if self.datos[3] != self.eFechaBaja.text():
                    self.apadrinamiento.setFechaDeBaja(self.eFechaBaja.text())
        else:
            if self.eBecado.text() == '' or self.eSocio.text() == '' or self.eFechaInicio.text() == '':
                print('Error: faltan datos obligatorios.')
                self.child = WarningDatosSinRellenar(self)
                self.child.show()
                return False
            else:
                bd = BDOperaciones()
                id = bd.maxId('id_apadrinamiento', 'apadrinamiento')
                id += 1
                print(id)
                print(self.becado.getIdJoven())
                print(self.socio.getUsuarioId())
                print(self.idUser)
                print(self.eFechaInicio.text())
                print(self.eFechaBaja.text())
                Apadrinamiento.newApadrinamiento(id, self.becado.getIdJoven(), self.socio.getUsuarioId(), self.idUser, self.eFechaInicio.text(), self.eFechaBaja.text())
        self.close()

    def cambiar(self):
        print('cambiando')
        indexB = self.tBecados.selectedIndexes()
        indexS = self.tSocios.selectedIndexes()
        if not indexB:
            self.child = WarningNoUserSelected(self)
            self.child.show()
            print('No se ha seleccionado ningun becado.')
        else:
            kid = indexB[0].row()
            idSeleccionado = self.jovenes[kid].getIdJoven()
            self.becado = Joven.getJoven(idSeleccionado)
            self.eBecado.setText(self.becado.getNombre() + ' ' + self.becado.getApellido())

        if not indexS:
            self.child = WarningNoUserSelected(self)
            self.child.show()
            print('No se ha seleccionado ningun socio.')
        else:
            socio = indexS[0].row()
            idSeleccionado = self.socios[socio].getUsuarioId()
            self.socio = Socio.getSocio(idSeleccionado)
            self.eSocio.setText(self.socio.getNombreDePila() + ' ' + self.socio.getApellidos())
        print('acabado')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    perfilApadrinamientoW = PerfilApadrinamientos('7', '2', 'modificar')
    perfilApadrinamientoW.show()
    sys.exit(app.exec_())
