import sys
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QWidget
import datetime
from BD.BDOperaciones import BDOperaciones
from BD.Transaccion import Transaccion
from BD.Proyecto import Proyecto
from BD.Apadrinamiento import Apadrinamiento
import easygui
import os


form_1, base_1 = uic.loadUiType('UI/creacionInforme.ui')

class CreacionInforme(base_1, form_1):
    def __init__(self, parent = None):
        super(base_1,self).__init__()
        self.setupUi(self)
        self.parent = parent

        self.cTipo.addItems(['', 'Ingreso', 'Gasto'])
        self.cMoneda.addItems(['', 'Euros', 'Lempiras'])
        self.cApadrinamiento.addItems([''] + [str(ap.getIdApadrinamiento()) for ap in Apadrinamiento.listaApadrinamientos()])
        self.cProyecto.addItems([''] + [str(pro.getIdProyecto()) for pro in Proyecto.listaProyectos()])

        self.calDateBegin.setSelectedDate(QtCore.QDate.fromString('2014-01-01', 'yyyy-MM-dd'))
        self.calDateEnd.setSelectedDate(QtCore.QDate.fromString('2020-01-01', 'yyyy-MM-dd'))

        self.bCancelar.clicked.connect(self.cancelar)
        self.bGenerar.clicked.connect(self.generar)

    def cancelar(self): 
        self.close()   

    def generar(self):
        folderName = easygui.diropenbox()
        if folderName == None:
            return
        transacciones = Transaccion.listaTransacciones()
        tipo = self.cTipo.currentText()
        tipoBool = tipo == 'Gasto'
        moneda = self.cMoneda.currentText()
        fechaEmisionMin = self.calDateBegin.selectedDate().toPyDate()
        fechaEmisionMax = self.calDateEnd.selectedDate().toPyDate()
        proyecto = self.cProyecto.currentText()
        apadrinamiento = self.cApadrinamiento.currentText()
        
        result = transacciones
        result = [trans for trans in result if tipo == '' or trans.getGasto() == tipoBool]
        result = [trans for trans in result if moneda == '' or trans.getMoneda() == moneda]
        result = [trans for trans in result if proyecto == '' or (str(trans.getProyecto().getIdProyecto() if trans.getProyecto()!=None else '')) == proyecto]
        result = [trans for trans in result if apadrinamiento == '' or (str(trans.getApadrinamiento().getIdApadrinamiento() if trans.getApadrinamiento()!= None else '')) == apadrinamiento]
        result = [trans for trans in result if trans.getFechaEmision() <= fechaEmisionMax]
        result = [trans for trans in result if trans.getFechaEmision() >= fechaEmisionMin]

        db = BDOperaciones()
        header = db.nombreColumnas(Transaccion.tabla)
        try:
            with open('{}.csv'.format(os.path.join(folderName, datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S'))), 'w') as file:
                for i, col in enumerate(header):
                    if i < len(header)-1:
                        file.write(col + ',')
                    else:
                        file.write(col + '\n')
                for trans in result:
                    file.write(str(trans.getIdTransaccion()) + ',')
                    file.write('True' if trans.getGasto() else 'False' + ',')
                    file.write(trans.getFechaEmision().strftime('%Y-%m-%d') + ',')
                    file.write(str(trans.getCuantia()) + ',')
                    file.write(trans.getMoneda() + ',')
                    file.write(trans.getDestino() if trans.getDestino()!=None else '' + ',')
                    file.write(trans.getFormaPago() if trans.getFormaPago()!=None else '' + ',')
                    file.write(trans.getMotivo() if trans.getMotivo()!=None else '' + ',')
                    file.write(str(trans.getProyecto().getIdProyecto() if trans.getProyecto()!=None else '') + ',')
                    file.write(str(trans.getApadrinamiento().getIdApadrinamiento() if trans.getApadrinamiento()!= None else '') + ',')
                    file.write((trans.getBeneficiario() if trans.getBeneficiario()!=None else '') + '\n')
            #Close the UI
            self.close()
        except FileNotFoundError:
            print("Folder not found to save the report")