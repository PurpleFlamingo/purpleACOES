import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from BD.BDOperaciones import BDOperaciones
from BD.Transaccion import Transaccion
from BD.Proyecto import Proyecto
from BD.Apadrinamiento import Apadrinamiento

form_1, base_1 = uic.loadUiType('UI/datosTransaccion.ui')

class DatosTransaccion(base_1, form_1):
    def __init__(self, parent = None):
        super(base_1,self).__init__()
        self.setupUi(self)
        self.parent = parent
      
        self.cTipo.addItems(['Ingreso', 'Gasto'])
        self.cMoneda.addItems(['Euros', 'Lempiras'])
        self.cApadrinamiento.addItems([''] + [str(ap.getIdApadrinamiento()) for ap in Apadrinamiento.listaApadrinamientos()])
        self.cProyecto.addItems([''] + [str(pro.getIdProyecto()) for pro in Proyecto.listaProyectos()])
        self.bAtras.clicked.connect(self.atras)
        self.bConfirmar.clicked.connect(self.confirmar)

    def atras(self):
        self.close()

    def confirmar(self):
        bd = BDOperaciones()
        id_transaccion = bd.getLastId(Transaccion.tabla) + 1
        gasto = True if (self.cTipo.currentText() == 'Ingreso') else False
        fechaEmision = self.calFechaEmision.selectedDate().toPyDate()
        cuantia = self.eCuantia.text() if self.eCuantia.text() != '' else None
        if cuantia != None:
            cuantia = int(cuantia)
            if cuantia <= 0:
                cuantia = None
                print('Cuantia no puede ser negativa')            
        else:
            print('Cuantia es obligatorio')

        moneda = self.cMoneda.currentText()
        destino = self.eDestino.text() if self.eDestino.text() != '' else None
        formaPago = self.eFormaPago.text() if self.eFormaPago.text() != '' else None
        motivo = self.eMotivo.text() if self.eMotivo.text() != '' else None
        proyecto = Proyecto.getProyecto(int(self.cProyecto.currentText()))
        apadrinamiento = Apadrinamiento.getApadrinamiento(int(self.cApadrinamiento.currentText()))
        beneficiario = self.eBeneficiario.text() if self.eBeneficiario.text() != '' else None
        #print(id_transaccion, gasto, fechaEmision, cuantia, moneda, destino, formaPago, motivo, proyecto, apadrinamiento, beneficiario)
        t = Transaccion.newTransaccion(id_transaccion, gasto, fechaEmision, cuantia, moneda, destino, formaPago, motivo, proyecto, apadrinamiento, beneficiario)
        self.atras()