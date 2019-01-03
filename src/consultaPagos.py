import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QHeaderView
from BD.Transaccion import Transaccion
from BD.Socio import Socio
from BD.Joven import Joven
from BD.Apadrinamiento import Apadrinamiento

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
        self.eSocioNombre.setText(self.socioApadrinador.getNombreDePila())

        #busco los apadrinamientos del socio
        self.listaDeApadrinamientos = Apadrinamiento.listaApadrinamientos(self.socioApadrinador.getUsuarioId())

        #busco los pagos hechos a los apadrinamientos del socio
        self.listaDePagos = []
        for ap in self.listaDeApadrinamientos:
            #print(ap)
            self.listaDePagos += Transaccion.listaTransacciones(ap.getIdApadrinamiento(), 0)
        
        print('Lista de pagos del socio ', (self.socioApadrinador.getUsuarioId()))
        for p in self.listaDePagos:
            print(p)


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
            print('Apadrinamiento : ', apadrinamiento)
            self.tPagos.setItem(i, 4, QTableWidgetItem(str(apadrinamiento)))

    #salir de la interfaz y regresar a la anterior
    def salir(self):
        self.close()
        self.parent.show()
