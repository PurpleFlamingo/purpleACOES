import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QHeaderView
from BD.Proyecto import Proyecto
from BD.BDOperaciones import BDOperaciones
from datosProyecto import DatosProyecto
from warningNoUserSelected import WarningNoUserSelected

import datetime

form_1, base_1 = uic.loadUiType('UI/gestorProyectos.ui',resource_suffix='')

class GestorProyecto(base_1, form_1):
    def __init__(self, parent = None):
        super(base_1,self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.child = None

        self.proyectos = []
        self.filtrada =  []
        self.actual = None
        self.lastId = 1

        self.eDescripcion.setEnabled(False)
        self.eRequisitos.setEnabled(False)

        self.recargar()

        #Relacion entre eventos y funciones
        self.bSalir.clicked.connect(self.salir)
        self.bAnadir.clicked.connect(self.nuevoProyecto)
        self.bEditar.clicked.connect(self.editarProyecto)
        self.bBusqueda.clicked.connect(self.busqueda)
        self.cProyecto.currentIndexChanged.connect(self.mostrarDatos)
        self.bActualizar.clicked.connect(self.recargar)




    #Carga la vista del padre
    def salir(self):
        self.parent.show()
        self.close()

    def mostrarDatos(self):
    	nombre = self.cProyecto.currentText()
    	for proyecto in self.filtrada:
    		if(proyecto.getNombre()==nombre):
    			self.actual=proyecto
    			self.eRequisitos.setPlainText(proyecto.getRequisitosDeParticipacion())
    			self.eDescripcion.setPlainText(proyecto.getDescripcion())

    #Carga la vista de datos de proyecto con una vista vacia para crear un proyecto nuevo
    def nuevoProyecto(self):
        self.child = DatosProyecto(self, lastId = self.lastId)
        self.child.show()

    #Carga la vista de datos de proyecto con los datos del proyecto seleccionado
    def editarProyecto(self):
        if self.actual != None :
            self.child = DatosProyecto(self, proyecto = self.actual)
        else :
            self.child = WarningNoUserSelected(self)
        self.child.show()

        

    #Actualiza la informacion de proyecto de la base de datos y actualiza los comboBox
    def recargar(self):

        #Cargamos los datos
        listpro=Proyecto.listaProyectos()
        self.proyectos=listpro
        self.filtrada=listpro
        if len(self.proyectos) > 0 :
            self.lastId=self.proyectos[len(self.proyectos)-1].getIdProyecto()
        nombres=[]
        tipos=['']

        for proyecto in listpro:
        	nombres.append(proyecto.getNombre())
        	if proyecto.getTipo() not in tipos:
        	    tipos.append(proyecto.getTipo())

        #Cargar lista de opciones en cada comboBox
        self.cProyecto.clear()
        self.cProyecto.addItems(nombres)
        self.cTipo.clear()
        self.cTipo.addItems(tipos)
        self.eNombre.setText(None)

        #Hace visibles los datos del primer proyecto almacenado en la lista
        if len(self.filtrada) > 0 :
            proyecto=self.filtrada[0]
            self.actual=proyecto
            self.eRequisitos.setPlainText(proyecto.getRequisitosDeParticipacion())
            self.eDescripcion.setPlainText(proyecto.getDescripcion())
        else:
            self.actual=None
            self.eRequisitos.setPlainText(None)
            self.eDescripcion.setPlainText(None)

    #Filtra el contenido del comboBox de seleccion de proyecto y lo actualiza 
    def busqueda(self):
        #lectura de los campos de filtrado
        nombre=self.eNombre.text()
        tipo= self.cTipo.currentText()
        self.filtrada=[]
        nombres=[]
        #actualizamos la lista filtrada y obtenemos la lista para el comboBox
        #Filtramos por todos los campos

        for proyecto in self.proyectos:
            if (nombre== '' or proyecto.getNombre()==nombre) and (tipo== '' or proyecto.getTipo()==tipo):
                self.filtrada.append(proyecto)
                nombres.append(proyecto.getNombre())

        self.cProyecto.clear()
        self.cProyecto.addItems(nombres)

        #Hace visibles los datos del primer proyecto almacenado en la lista
        if len(self.filtrada) > 0 :
            proyecto=self.filtrada[0]
            self.actual=proyecto
            self.eRequisitos.setPlainText(proyecto.getRequisitosDeParticipacion())
            self.eDescripcion.setPlainText(proyecto.getDescripcion())
        else:
            self.actual=None
            self.eRequisitos.setPlainText("")
            self.eDescripcion.setPlainText("")
        
       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gestorProyectoW = GestorProyecto()
    gestorProyectoW.show()
    sys.exit(app.exec_())
