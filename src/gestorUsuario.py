import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from BD.BDOperaciones import BDOperaciones

form_1, base_1 = uic.loadUiType('UI/gestorUsuario.ui')

class GestorUsuario(base_1, form_1):
    def __init__(self, parent = None):
        super(base_1,self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.child = []

        self.bAtras.clicked.connect(self.atras)

        usuarios = self.getUsuarios()
        print(usuarios)
        tabla = self.tUsuarios
        tabla.setRowCount(len(usuarios))
        #tabla.setColCount(len(usuarios))

    def atras(self):
        self.hide()
        self.parent.show()

    #TODO: Esta funcion debe recoger de la base de datos todos los usuarios y mostrarlos en la vista
    def getUsuarios(self):
        db = BDOperaciones()
        return db.getUsuarios()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gestorUsuarioW = GestorUsuario()
    gestorUsuarioW.show()
    sys.exit(app.exec_())
