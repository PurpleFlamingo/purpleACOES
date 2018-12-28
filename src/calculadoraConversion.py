import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QHeaderView
from currencyConverter import CurrencyConverter
import datetime

form_1, base_1 = uic.loadUiType('UI/calculadoraConversion.ui')

class CalculadoraConversion(base_1, form_1):
    def __init__(self, parent = None):
        super(base_1,self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.conversor = CurrencyConverter()
        self.actualizar()

        #Default Euros->Lempiras
        self.eEuros.setEnabled(True)
        self.eLempiras.setEnabled(False)

        self.bConvertir.clicked.connect(self.convertir)
        self.cTipoCambio.currentTextChanged.connect(self.cambioSeleccion)


    def actualizar(self):
        self.lRatioEurHnl.setText(str(round(self.conversor.EUR_HNL, 2)) + ' EUR/HNL')
        self.lRatioHnlEur.setText(str(round(self.conversor.HNL_EUR, 2)) + ' HNL/EUR')
        self.lFechaUltimaActualizacion.setText(self.conversor.lastUpdate)

    def convertir(self):
        try:
            if str(self.cTipoCambio.currentText()) == 'Euros -> Lempiras':
                strValue = self.eEuros.text()
                value = self.conversor.eurToHnl(float(strValue))
                self.eLempiras.setText(str(round(value, 2)))
            else:
                strValue = self.eLempiras.text()
                value = self.conversor.hnlToEur(float(strValue))
                self.eEuros.setText(str(round(value, 2)))
        except ValueError:
            self.eEuros.setText('')
            self.eLempiras.setText('')

    def cambioSeleccion(self, value):
        if value == 'Euros -> Lempiras':
            self.eEuros.setEnabled(True)
            self.eLempiras.setEnabled(False)
        else:
            self.eEuros.setEnabled(False)
            self.eLempiras.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = CalculadoraConversion()
    c.show()
    sys.exit(app.exec_())
