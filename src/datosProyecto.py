import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from BD.BDOperaciones import BDOperaciones
from BD.Proyecto import Proyecto
import recursosQT_rc

form_1, base_1 = uic.loadUiType('UI/datosProyecto.ui')

class DatosProyecto(base_1, form_1):
    def __init__(self, parent = None, proyecto = None, lastId = None):
        super(base_1,self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.child = None
        self.proyecto=proyecto
        self.lastId=lastId
        
        if self.proyecto != None :
            self.eNombre.setText(proyecto.getNombre())
            self.eTipo.setText(proyecto.getTipo())
            self.eRequisitos.setPlainText(proyecto.getRequisitosDeParticipacion())
            self.eDescripcion.setPlainText(proyecto.getDescripcion())

        self.bGuardarYSalir.clicked.connect(self.guardar)
        self.bSalirSinGuardar.clicked.connect(self.salir)

    def salir(self):
        self.parent.show()
        self.close()

    def guardar(self):
        nombre=self.eNombre.text()
        tipo=self.eTipo.text()
        req=self.eRequisitos.toPlainText()
        des=self.eDescripcion.toPlainText()
        if self.proyecto != None :
            self.proyecto.setNombre(nombre)
            self.proyecto.setTipo(tipo)
            self.proyecto.setRequisitosDeParticipacion(req)
            self.proyecto.setDescripcion(des)
        else:
            Proyecto.newProyecto(self.lastId+1, nombre, req, des, tipo)

        self.salir()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    datosProyectoW = DatosProyecto()
    datosProyectoW.show()
    sys.exit(app.exec_())
