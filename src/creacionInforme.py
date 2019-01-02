import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
import datetime
from BD.Transaccion import Transaccion
from BD.Proyecto import Proyecto
from BD.Apadrinamiento import Apadrinamiento


form_1, base_1 = uic.loadUiType('UI/creacionInforme.ui')

class CreacionInforme(base_1, form_1):
    def __init__(self, parent = None):
        super(base_1,self).__init__()
        self.setupUi(self)
        self.parent = parent

        self.cTipo.addItems(['Todos', 'Ingreso', 'Gasto'])
        self.cMoneda.addItems(['Todas', 'Euros', 'Lempiras'])
        self.cApadrinamiento.addItems([''] + [str(ap.getIdApadrinamiento()) for ap in Apadrinamiento.listaApadrinamientos()])
        self.cProyecto.addItems([''] + [str(pro.getIdProyecto()) for pro in Proyecto.listaProyectos()])



        self.bCancelar.clicked.connect(self.cancelar)
        self.bGenerar.clicked.connect(self.generar)

    def cancelar(self): 
        self.close()   

    def generar(self):
        pass