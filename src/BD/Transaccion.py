from BD import BD
from Proyecto import Proyecto
from Apadrinamiento import Apadrinamiento


class Transaccion:
    tabla = 'transaccion'
    def __init__(self, id_transaccion, gasto, fechaEmision, cuantia, moneda, destino, formaPago, motivo, proyecto, apadrinamiento, beneficiario):
        self.id_transaccion = id_transaccion
        self.gasto = gasto
        self.fechaEmision = fechaEmision
        self.cuantia = cuantia
        self.moneda = moneda
        self.destino = destino
        self.formaPago = formaPago
        self.motivo = motivo
        self.proyecto = proyecto
        self.apadrinamiento = apadrinamiento
        self.beneficiario = beneficiario

    @staticmethod
    def newTransaccion(id_transaccion, gasto, fechaEmision, cuantia, moneda, destino, formaPago, motivo, proyecto, apadrinamiento, beneficiario):
        bd = BD()
        if destino == None:
            destino = 'null'
        if formaPago == None:
            formaPago = 'null'
        if motivo == None:
            motivo = 'null'
        if proyecto == None:
            proyecto = 'null'
        if apadrinamiento == None:
            apadrinamiento = 'null'
        if beneficiario == None:
            beneficiario = 'null'

        valores = [id_transaccion, gasto, fechaEmision, cuantia, moneda, destino, formaPago, motivo, proyecto, apadrinamiento, beneficiario]

        bd.insert(valores, Transaccion.tabla)
        newTrans = Transaccion(id_transaccion, gasto, fechaEmision, cuantia, moneda, destino, formaPago, motivo, proyecto, apadrinamiento, beneficiario)
        return newTrans

    @staticmethod
    def getTransaccion(id_transaccion):
        bd = BD()
        cond = 'id_transaccion = ' + str(id_transaccion)
        trans = bd.selectEscalar('*', Transaccion.tabla, cond)
        print(trans)
        id_transaccion = trans[0]
        gasto = True if (trans[1] == 1) else False
        fechaEmision = trans[2]
        cuantia = trans[3]
        moneda = trans[4]
        destino = trans[5]
        formaPago = trans[6]
        motivo = trans[7]
        proyecto = Proyecto(trans[8]) if trans[8]!=None else None
        apadrinamiento = Apadrinamiento(trans[9]) if trans[9]!=None else None
        beneficiario = trans[10]
        newTrans = Transaccion(id_transaccion, gasto, fechaEmision, cuantia, moneda, destino, formaPago, motivo, proyecto, apadrinamiento, beneficiario)
        return newTrans

    @staticmethod
    def listaTransacciones():
        bd = BD()
        trans = bd.select('*', Transaccion.tabla)
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
            proyecto = Proyecto(transaccion[8]) if transaccion[8]!=None else None
            apadrinamiento = Apadrinamiento(transaccion[9]) if transaccion[9]!=None else None
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
        if newId != None:
            bd = BD()
            condicion = 'id_transaccion = ' + str(newId)
            #Compruebo que el valor es unico
            res = bd.selectEscalar('*', Transaccion.tabla, condicion)
            if not res:
                condicion = 'id_transaccion = ' + str(self.id_transaccion)
                setter = 'id_transaccion =  '+ str(newId)
                bd.update(Transaccion.tabla, setter, condicion)
                self.id_transaccion = newId
                return True
            else:
                #El newID ya esta ocupado
                return False
        else:
            #El id no puede ser null
            return False

    def setGasto(self, newGasto: bool):
        #No se pueden modificar transacciones
        return False
        if newGasto != None:
            bd = BD()
            condicion = 'id_transaccion = ' + str(self.id_transaccion)
            setter = 'gasto =  '+ ('1' if newGasto else '0')
            bd.update(Transaccion.tabla, setter, condicion)
            self.gasto = newGasto
            return True
        else:
            return False

    def setFechaEmision(self, newFecha: str):
        #No se pueden modificar transacciones
        return False
        if newFecha != None:
            bd = BD()
            condicion = 'id_transaccion = ' + str(self.id_transaccion)
            setter = 'fechaEmision =  \'' + str(newFecha) + '\''
            bd.update(Transaccion.tabla, setter, condicion)
            self.fechaEmision = newFecha
            return True
        else:
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
            toStr+=('Proyecto: ' + self.proyecto + ' - ')
        if self.apadrinamiento != None:
            toStr+=('Apadrinamiento: ' + self.apadrinamiento + ' - ')
        if self.beneficiario != None:
            toStr+=('Beneficiario: ' + self.beneficiario + ' - ')
        return toStr[:-5]

if __name__ == '__main__':
    #Transaccion.newTransaccion(1, 1, '2017-1-1', 128, 'Euros', 'Honduras', 'Transferencia', 'Porque si', None, None, 'Yo')
    t = Transaccion.getTransaccion(4)
    #print(t.setApadrinamiento())
    print(Transaccion.listaTransacciones())