import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QHeaderView
from BD.Transaccion import Transaccion
from BD.Socio import Socio
from BD.Joven import Joven
from BD.Apadrinamiento import Apadrinamiento
from warningNoUserSelected import WarningNoUserSelected
from detallePagos import DetallePagos

form_1, base_1 = uic.loadUiType('UI/consultaPagos.ui')

class ConsultaPagos(base_1, form_1):
    def __init__(self, parent = None, idSocio = None):
        super(base_1, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.child = None

        #boton Atras
        self.bAtras.clicked.connect(self.salir)

        #muestro los datos del socio apadrinador
        self.socioApadrinador = Socio.getSocio(idSocio)
        self.eSocioId.setText(str(self.socioApadrinador.getUsuarioId()))
        self.eSocioId.setEnabled(False)
        self.eSocioNombre.setText(self.socioApadrinador.getNombreDePila())
        self.eSocioNombre.setEnabled(False)

        #busco los apadrinamientos del socio
        self.listaDeApadrinamientos = Apadrinamiento.listaApadrinamientos(self.socioApadrinador.getUsuarioId())

        #busco los pagos hechos a los apadrinamientos del socio
        self.listaDePagos = []
        for ap in self.listaDeApadrinamientos:
            #print(ap)
            self.listaDePagos += Transaccion.listaTransacciones(ap.getIdApadrinamiento(), 0)


        #print('Lista de pagos del socio ', (self.socioApadrinador.getUsuarioId()))
        #for p in self.listaDePagos:
            #print(p)

        #Acomodamiento de la tabla
        self.tPagos.verticalHeader().hide()
        self.tPagos.setRowCount(len(self.listaDePagos))
        self.tPagos.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

        #Mostramos los datos de todas los pagos
        for i, pago in enumerate(self.listaDePagos):
            #Columna Nº Movimiento
            self.tPagos.setItem(i, 0, QTableWidgetItem(str(pago.getIdTransaccion())))
            #Columna Descripcion
            self.tPagos.setItem(i, 1, QTableWidgetItem(pago.getMotivo()))
            #Columna Fecha
            self.tPagos.setItem(i, 2, QTableWidgetItem(pago.getFechaEmision()))
            #Columna Importe
            cadena = str(pago.getCuantia()) + ' ' + pago.getMoneda()
            self.tPagos.setItem(i, 3, QTableWidgetItem(cadena))
            #Columna Apadrinamiento
            apadrinamiento = pago.getApadrinamiento().getIdApadrinamiento()
            self.tPagos.setItem(i, 4, QTableWidgetItem(str(apadrinamiento)))

        #Consulta
        self.bConsulta.clicked.connect(self.consultaDePagos)

    
    def consultaDePagos(self):
        index = self.tPagos.selectedIndexes()
        indexPago = index[0].row()
        print(index)
        if not index:
            self.child = WarningNoUserSelected(self, 'Pago')
            self.child.show()
            print('No elemento seleccionado')
        else:
            self.child = DetallePagos(self, self.listaDePagos[indexPago], self.socioApadrinador)
            self.hide()
            self.child.show()
            print('Pago seleccionado: ')
            print(self.listaDePagos[indexPago])


    #salir de la interfaz y regresar a la anterior
    def salir(self):
        self.close()
        self.parent.show()
