import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget


form_1, base_1 = uic.loadUiType('UI/password.ui')

class PasswordDisplay(base_1, form_1):
    def __init__(self, parent = None):
        
        super(base_1,self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.child = None
        self.lPassword.setText(parent.claveRecuperada)
        self.bExit.clicked.connect(self.salir)

    def salir(self):
        self.hide()
        self.parent.salir()
        if self.parent.passwordParent == "Correo":
            self.parent.parent.salir()
        