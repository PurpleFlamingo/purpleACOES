from BD.BD import BD
from BD.Proyecto import Proyecto
from BD.Apadrinamiento import Apadrinamiento
from datetime import datetime


class Transaccion:
    tabla = 'transaccion'
    def __init__(self, id_transaccion = None, gasto = None, fechaEmision = None, cuantia = None, moneda = None, destino = None, formaPago = None, motivo = None, proyecto = None, apadrinamiento = None, beneficiario = None):
        self.id_transaccion = id_transaccion
        self.gasto = gasto
        self.fechaEmision = fechaEmision
        self.cuantia = cuantia
        self.moneda = moneda
        self.destino = destino
        self.formaPago = formaPago
        self.motivo = motivo
        self.proyecto = Proyecto.getProyecto(proyecto) if proyecto != None else None
        self.apadrinamiento = Apadrinamiento.getApadrinamiento(apadrinamiento) if apadrinamiento != None else None
        self.beneficiario = beneficiario

    @staticmethod
    def newTransaccion(id_transaccion, gasto, fechaEmision, cuantia, moneda, destino = None, formaPago = None, motivo = None, proyecto = None, apadrinamiento = None, beneficiario = None):
        bd = BD()

        condicion = 'id_transaccion = ' + str(id_transaccion)
        #Compruebo que el valor es unico
        res = bd.selectEscalar('*', Transaccion.tabla, condicion)
        if not res:
            valores = [id_transaccion, gasto, fechaEmision, cuantia, moneda, destino if destino != None else 'null', formaPago if formaPago != None else 'null', motivo if motivo != None else 'null', proyecto if proyecto != None else 'null', apadrinamiento if apadrinamiento != None else 'null', beneficiario if beneficiario != None else 'null']

            bd.insert(valores, Transaccion.tabla)
            newTrans = Transaccion(id_transaccion, gasto, fechaEmision, cuantia, moneda, destino, formaPago, motivo, proyecto, apadrinamiento, beneficiario)
            return newTrans
        else:
            print('Error: La id {} ya esta en uso'.format(id_transaccion))
            return None

    @staticmethod
    def getTransaccion(id_transaccion: int):
        bd = BD()
        cond = 'id_transaccion = ' + str(id_transaccion)
        trans = bd.selectEscalar('*', Transaccion.tabla, cond)
        if not trans:
            #La transaccion solicitada no existe
            return None
        else:
            id_transaccion = trans[0]
            gasto = True if (trans[1] == 1) else False
            fechaEmision = datetime.strptime(trans[2], '%Y-%m-%d')
            cuantia = trans[3]
            moneda = trans[4]
            destino = trans[5]
            formaPago = trans[6]
            motivo = trans[7]
            proyecto = trans[8]
            apadrinamiento = trans[9]
            beneficiario = trans[10]
            newTrans = Transaccion(id_transaccion, gasto, fechaEmision, cuantia, moneda, destino, formaPago, motivo, proyecto, apadrinamiento, beneficiario)
            return newTrans

    @staticmethod
    def listaTransacciones(apadrinamiento:int = None, gasto: int = None):
        bd = BD()
        if apadrinamiento == None or gasto == None:
            condicion = None
        else:
            condicion = ' apadrinamiento = ' + str(apadrinamiento) + ' and gasto = ' + str(gasto)

        trans = bd.select('*', Transaccion.tabla, condicion)
        listTransacciones = []
        for transaccion in trans:
            id_transaccion = transaccion[0]
            gasto = True if (transaccion[1] == 1) else False
            fechaEmision = transaccion[2]
            cuantia = transaccion[3]
            moneda = transaccion[4]
            destino = transaccion[5]
            formaPago = transaccion[6]
            motivo = transaccion[7]
            proyecto = transaccion[8]
            apadrinamiento = transaccion[9]
            beneficiario = transaccion[10]
            newTrans = Transaccion(id_transaccion, gasto, fechaEmision, cuantia, moneda, destino, formaPago, motivo, proyecto, apadrinamiento, beneficiario)
            listTransacciones.append(newTrans)
        return listTransacciones

#Getters
    def getIdTransaccion(self):
        return self.id_transaccion

    def getGasto(self):
        return self.gasto

    def getFechaEmision(self):
        return self.fechaEmision

    def getCuantia(self):
        return self.cuantia

    def getMoneda(self):
        return self.moneda

    def getDestino(self):
        return self.destino

    def getFormaPago(self):
        return self.formaPago

    def getMotivo(self):
        return self.motivo

    def getProyecto(self):
        return self.proyecto

    def getApadrinamiento(self):
        return self.apadrinamiento

    def getBeneficiario(self):
        return self.beneficiario

#Setters
    def setIdTransaccion(self, newId: int):
        #No se pueden modificar transacciones
        return False

    def setGasto(self, newGasto: bool):
        #No se pueden modificar transacciones
        return False

    def setFechaEmision(self, newFecha: str):
        #No se pueden modificar transacciones
        return False

    def setCuantia(self, newCuantia: int):
        #No se pueden modificar transacciones
        return False

    def setMoneda(self, newMoneda: str):
        #No se pueden modificar transacciones
        return False

    def setDestino(self, newDestino: str):
        #No se pueden modificar transacciones
        return False

    def setFormaPago(self, newForma: str):
        #No se pueden modificar transacciones
        return False

    def setMotivo(self, newMotivo: str):
        #No se pueden modificar transacciones
        return False

    def setProyecto(self, newProyecto: Proyecto):
        #No se pueden modificar transacciones
        return False

    def setApadrinamiento(self, newApadrinamiento: Apadrinamiento):
        #No se pueden modificar transacciones
        return False

    def setBeneficiario(self, newBeneficiario: str):
        #No se pueden modificar transacciones
        return False



    def delete(self):
        bd = BD()
        condicion = 'id_transaccion = ' + str(self.id_transaccion)
        bd.delete(Transaccion.tabla, condicion)
        self.id_transaccion = None
        self.gasto = None
        self.fechaEmision = None
        self.cuantia = None
        self.moneda = None
        self.destino = None
        self.formaPago = None
        self.motivo = None
        self.proyecto = None
        self.apadrinamiento = None
        self.beneficiario = None

    def __repr__(self):
        toStr = ''
        if self.id_transaccion != None:
            toStr+=('ID: ' + str(self.id_transaccion) + ' - ')
        if self.gasto != None:
            toStr+=('Tipo: ' + ('Gasto' if self.gasto else 'Ingreso') + ' - ')
        if self.fechaEmision != None:
            toStr+=('Fecha de emision: ' + self.fechaEmision.strftime('%Y-%m-%d') + ' - ')
        if self.cuantia != None:
            toStr+=('Cuantia: ' + str(self.cuantia) + ' - ')
        if self.moneda != None:
            toStr+=('Moneda: ' + self.moneda + ' - ')
        if self.destino != None:
            toStr+=('Destino: ' + self.destino + ' - ')
        if self.formaPago != None:
            toStr+=('Forma de pago: ' + self.formaPago + ' - ')
        if self.motivo != None:
            toStr+=('Motivo: ' + self.motivo + ' - ')
        if self.proyecto != None:
            toStr+=('Proyecto: ' + self.proyecto.getNombre() + ' - ')
        if self.apadrinamiento != None:
            toStr+=('Apadrinamiento: ' + str(self.apadrinamiento.getIdApadrinamiento()) + ' - ')
        if self.beneficiario != None:
            toStr+=('Beneficiario: ' + self.beneficiario + ' - ')
        return toStr[:-3]

if __name__ == '__main__':
    Transaccion.newTransaccion(4, 1, '2017-1-1', 128, 'Euros', 'Honduras', 'Transferencia', 'Porque si', None, None, 'Yo')
    t = Transaccion.getTransaccion(4)
    print(t.getFechaEmision())
    #print(t.setApadrinamiento())
    print(Transaccion.listaTransacciones())
