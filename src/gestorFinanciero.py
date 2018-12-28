import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QHeaderView
from BD.BDOperaciones import BDOperaciones
from calculadoraConversion import CalculadoraConversion
from BD.Transaccion import Transaccion


form_1, base_1 = uic.loadUiType('UI/gestorFinanciero.ui')

class GestorFinanciero(base_1, form_1):
    def __init__(self, parent = None, idUser = None):
        super(base_1,self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.child = None

        #Datos a mostrar con los nombres de la base de datos
        self.datos = ['id_transaccion', 'gasto', 'fechaEmision', 'cuantia', 'moneda', 'destino']
        #Lista con los nombres de las columnas
        #Referidas en la lista anterior
        self.cabeceras = ['ID', 'Tipo', 'Fecha de emision', 'Cuantia', 'Moneda', 'Destino']

        #Lista con toda la informacion de las transacciones actuales
        self.transacciones = []
        self.filtrada = []

        self.recargar()

        #Relacion entre eventos y funciones
        self.bAtras.clicked.connect(self.atras)
        self.bConversor.clicked.connect(self.calculadora)
        self.bAnadirTransaccion.clicked.connect(self.newTransaccion)
        self.bInforme.clicked.connect(self.generarInforme)
        self.bActualizar.clicked.connect(self.recargar)

        self.eId.textChanged.connect(self.busqueda)
        self.cTipo.currentIndexChanged.connect(self.busqueda)
        self.eCuantia.textChanged.connect(self.busqueda)
        self.cSimboloCuantia.currentIndexChanged.connect(self.busqueda)
        self.cMoneda.currentIndexChanged.connect(self.busqueda)
        self.cDestino.currentIndexChanged.connect(self.busqueda)
        self.eFecha.textChanged.connect(self.busqueda)
        self.cSimboloFecha.currentIndexChanged.connect(self.busqueda)
    
    #Carga la vista del padre
    def atras(self):
        self.parent.show()
        self.close()

    #Carga la vista de anadir transaccion con una vista vacia para crear una transaccion nueva
    def newTransaccion(self):
        #self.child = AnadirTransaccion(self)
        #self.child.show()
        pass

    #Carga la calculadora de conversion
    def calculadora(self):
        self.child = CalculadoraConversion(self)
        self.child.show()

    #Reinicia todos los campos usados en el filtrado
    def resetBusqueda(self):
        self.eId.setText('')
        self.cTipo.setCurrentIndex(0)
        self.eCuantia.setText('')
        self.cSimboloCuantia.setCurrentIndex(0)
        self.cMoneda.setCurrentIndex(0)
        self.cDestino.setCurrentIndex(0)
        self.eFecha.setText('')
        self.cSimboloFecha.setCurrentIndex(0)

    def generarInforme(self):
        pass


    #Actualiza la informacion de usuarios de la base de datos y los muestra todos en la tabla
    def recargar(self):
        transacciones = Transaccion.listaTransacciones()
        self.tTransacciones.verticalHeader().hide()
        self.tTransacciones.setColumnCount(len(self.cabeceras))
        self.tTransacciones.setRowCount(len(transacciones))
        self.tTransacciones.setHorizontalHeaderLabels(self.cabeceras)
        self.tTransacciones.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

        tipo = ['', 'Gasto', 'Ingreso']
        simbolos = ['=', '!=', '<', '<=', '>', '>=']
        moneda = ['']
        destino = ['']

        #Mostramos los datos de todas las transacciones y almacenamos 
        for i, trans in enumerate(transacciones):
            for j, key in enumerate(self.datos):
                if key == 'id_transaccion':
                    self.tTransacciones.setItem(i, j, QTableWidgetItem(str(trans.getIdTransaccion())))
                elif key == 'gasto':
                    self.tTransacciones.setItem(i, j, QTableWidgetItem('Gasto' if trans.getGasto() else 'Ingreso'))
                elif key == 'fechaEmision':
                    self.tTransacciones.setItem(i, j, QTableWidgetItem(trans.getFechaEmision().strftime('%Y-%m-%d')))
                elif key == 'cuantia':
                    self.tTransacciones.setItem(i, j, QTableWidgetItem(str(trans.getCuantia())))
                elif key == 'moneda':
                    mon = trans.getMoneda()
                    if mon not in moneda:
                        moneda.append(mon)
                    self.tTransacciones.setItem(i, j, QTableWidgetItem(trans.getMoneda()))
                elif key == 'destino':
                    dest = trans.getDestino()
                    if dest not in destino:
                        destino.append(dest)
                    self.tTransacciones.setItem(i, j, QTableWidgetItem(trans.getDestino()))
                elif key == 'formaPago':
                    self.tTransacciones.setItem(i, j, QTableWidgetItem(trans.getFormaPago()))
                elif key == 'motivo':
                    self.tTransacciones.setItem(i, j, QTableWidgetItem(trans.getMotivo()))
                elif key == 'proyecto':
                    self.tTransacciones.setItem(i, j, QTableWidgetItem(trans.getProyecto().getNombre()))
                elif key == 'apadrinamiento':
                    self.tTransacciones.setItem(i, j, QTableWidgetItem(trans.getApadrinamiento().getIdApadrinamiento))
                elif key == 'beneficiario':
                    self.tTransacciones.setItem(i, j, QTableWidgetItem(trans.getBeneficiario()))

        #Cargar lista de opciones en cada comboBox
        self.cTipo.clear()
        self.cTipo.addItems(tipo) 
        self.cDestino.clear()
        print(destino)
        self.cDestino.addItems(destino)
        self.cMoneda.clear()
        self.cMoneda.addItems(moneda)
        self.cSimboloCuantia.clear()
        self.cSimboloCuantia.addItems(simbolos)
        self.cSimboloFecha.clear()
        self.cSimboloFecha.addItems(simbolos)

        #self.resetBusqueda()

        self.transacciones = transacciones

    #Filtra el contenido de la tabla y actualiza la vista
    def busqueda(self):
        #lectura de los campos de filtrado
        id = self.eId.text()
        tipo = self.cTipo.currentText()
        tipoBool = tipo == 'Gasto'
        cuantia = self.eCuantia.text()
        simboloCuantia = self.cSimboloCuantia.currentText()
        moneda = self.cMoneda.currentText()
        destino = self.cDestino.currentText()
        fecha = self.eFecha.text()
        simboloFecha = self.cSimboloFecha.currentText()

        #Filtramos todos los resultados por todos los campos

        result = self.transacciones

        result = [trans for trans in result if id == '' or trans.getIdTransaccion() == int(id)]
        result = [trans for trans in result if tipo == '' or (trans.getGasto == tipoBool) ]
        result = [trans for trans in result if cuantia == '' or self.checkSimbolo(trans.getCuantia(), simboloCuantia, int(cuantia))]
        result = [trans for trans in result if moneda == '' or trans.getMoneda() == moneda]
        result = [trans for trans in result if destino == '' or trans.getDestino() == destino]
        result = [trans for trans in result if fecha == '' or self.checkSimbolo(trans.getFechaEmision().strftime('%Y-%m-%d'), simboloFecha, fecha)]
        
        self.filtrada = result
        #Actualizamos la vista por los contenidos fitrados
        self.tTransacciones.setRowCount(len(result))
        for i, trans in enumerate(result):
            for j, key in enumerate(self.datos):
                if key == 'id_transaccion':
                    self.tTransacciones.setItem(i, j, QTableWidgetItem(str(trans.getIdTransaccion())))
                elif key == 'gasto':
                    self.tTransacciones.setItem(i, j, QTableWidgetItem('Gasto' if trans.getGasto() else 'Ingreso'))
                elif key == 'fechaEmision':
                    self.tTransacciones.setItem(i, j, QTableWidgetItem(trans.getFechaEmision().strftime('%Y-%m-%d')))
                elif key == 'cuantia':
                    self.tTransacciones.setItem(i, j, QTableWidgetItem(str(trans.getCuantia())))
                elif key == 'moneda':
                    self.tTransacciones.setItem(i, j, QTableWidgetItem(trans.getMoneda()))
                elif key == 'destino':
                    self.tTransacciones.setItem(i, j, QTableWidgetItem(trans.getDestino()))
                elif key == 'formaPago':
                    self.tTransacciones.setItem(i, j, QTableWidgetItem(trans.getFormaPago()))
                elif key == 'motivo':
                    self.tTransacciones.setItem(i, j, QTableWidgetItem(trans.getMotivo()))
                elif key == 'proyecto':
                    self.tTransacciones.setItem(i, j, QTableWidgetItem(trans.getProyecto().getNombre()))
                elif key == 'apadrinamiento':
                    self.tTransacciones.setItem(i, j, QTableWidgetItem(trans.getApadrinamiento().getIdApadrinamiento))
                elif key == 'beneficiario':
                    self.tTransacciones.setItem(i, j, QTableWidgetItem(trans.getBeneficiario()))

    #Recibe x e y comparables y un simbolo como string y devuelve el resultado de operar `x simbolo y`
    #Returns bool
    def checkSimbolo(self, x, simbolo, y):
        if simbolo == '<':
            return x < y
        elif simbolo == '<=':
            return x <= y
        elif simbolo == '>':
            return x > y
        elif simbolo == '>=':
            return x >= y
        elif simbolo == '=' or simbolo == '==':
            return x == y
        elif simbolo == '!=':
            return x != y
        else:
            raise ValueError('Unknown simbol', simbolo)
