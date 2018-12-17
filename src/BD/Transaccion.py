from BD import BD


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
        db = BD()
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

        db.insert(valores, Transaccion.tabla)
        newTrans = Transaccion(id_transaccion, gasto, fechaEmision, cuantia, moneda, destino, formaPago, motivo, proyecto, apadrinamiento, beneficiario)
        return newTrans

    @staticmethod
    def getTransaccion(id_transaccion):
        db = BD()
        cond = 'id_transaccion = ' + str(id_transaccion)
        trans = db.selectEscalar('*', Transaccion.tabla, cond)
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
        db = BD()
        trans = db.select('*', Transaccion.tabla)
        listTransacciones = []
        print(trans)
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
        print(listTransacciones)

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
    Transaccion.newTransaccion(2, 1, '2017-1-1', 128, 'Euros', 'Honduras', 'Transferencia', 'Porque si', None, None, 'Yo')
    Transaccion.getTransaccion(1)
    Transaccion.listaTransacciones()