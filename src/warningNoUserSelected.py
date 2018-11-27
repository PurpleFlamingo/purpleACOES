import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget

form_1, base_1 = uic.loadUiType('UI/warningNoUserSelected.ui')

class WarningNoUserSelected(base_1, form_1):
    def __init__(self, parent = None):
        super(base_1,self).__init__()
        self.setupUi(self)
        self.parent = parent

        self.bAtras.clicked.connect(self.hide)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    warning = WarningNoUserSelected()
    warning.show()
    sys.exit(app.exec_())