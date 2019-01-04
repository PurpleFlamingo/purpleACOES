import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QHeaderView
from BD.Transaccion import Transaccion
from BD.Socio import Socio
from BD.Joven import Joven
from BD.Apadrinamiento import Apadrinamiento

form_1, base_1 = uic.loadUiType('UI/detallePagos.ui')


class DetallePagos(base_1, form_1):
    def __init__(self, parent=None, pago = None, socio = None):
        super(base_1, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.child = None

        self.bAtras.clicked.connect(self.salir)

        #leo la transaccion y el socio no son nulos
        if pago != None and socio != None:
            self.pago = pago
            self.socio = socio

            #cargo los datos a mostrar en cadenas de texto
            idTransaccion = str(self.pago.getIdTransaccion())
            nombreSocio = self.socio.getNombreDePila()
            descripcion = self.pago.getMotivo()
            importe = str(self.pago.getCuantia()) + ' ' + self.pago.getMoneda()
            fechaAbono = self.pago.getFechaEmision()
            modoPago = self.pago.getFormaPago()
            joven = self.pago.getApadrinamiento().getJoven()
            nombreJoven = joven.getNombre() + ' ' + joven.getApellido()

            #inhabilito la edicion de las cajas de texto
            self.eNumeroDeMovimiento.setEnabled(False)
            self.eNombreSocio.setEnabled(False)
            self.eDescripcion.setEnabled(False)
            self.eImporte.setEnabled(False)
            self.eFechaAbono.setEnabled(False)
            self.eModoPago.setEnabled(False)
            self.eNombreJoven.setEnabled(False)

            #relleno las cajas de texto con la información obtenida
            self.eNumeroDeMovimiento.setText(idTransaccion)
            self.eNombreSocio.setText(nombreSocio)
            self.eDescripcion.setPlainText(descripcion)
            self.eImporte.setText(importe)
            self.eFechaAbono.setText(fechaAbono)
            self.eModoPago.setText(modoPago)
            self.eNombreJoven.setText(nombreJoven)
            

    def salir(self):
        self.close()
        self.parent.show()
