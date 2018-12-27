import sys
from BD import BD

class PertenecerProyecto:
    tabla = 'pertencer_proyecto'

    def __init__(self, joven, proyecto, fechaAlta, fechaBaja):
        self.joven = joven
        self.proyecto = proyecto
        self.fechaAlta = fechaAlta
        self.fechaBaja = fechaBaja
    
    @staticmethod
    def newPertenecerProyecto(joven, proyecto, fechaAlta, fechaBaja = None):
        if fechaBaja == None:
            fechaBaja = 'null'
        
        bd = BD()
        condicion = 'joven = ' + str(joven.getIdjoven()) + ' and proyecto = ' + str(proyecto.getIdProyecto())
        res = bd.selectEscalar('*', PertenecerProyecto.tabla, condicion)
        if not res:
            valores = [joven.getIdjoven(), proyecto.getIdProyecto(), fechaAlta, fechaBaja]
            newPert = PertenecerProyecto(joven, proyecto, fechaAlta, fechaBaja)
            return newPert
        else:
            print('Error: La id \'{}\'-\'{}\' ya esta en uso'.format(joven.getIdjoven(),proyecto.getIdProyecto()))
            return None

    @staticmethod
    def getPertenecerProyecto(joven, proyecto):
        bd = BD()
        condicion = 'joven = ' + str(joven.getIdjoven()) + ' and proyecto = ' + str(proyecto.getIdProyecto())
        res = bd.selectEscalar('*', PertenecerProyecto.tabla, condicion)
        if not res:
            #El joven no pertenece a proyecto
            return None
        else:
            joven = Joven(res[0])
            proyecto = Proyecto(res[1])
            fechaAlta = res[2]
            fechaBaja = res[3]
            newPert = PertenecerProyecto(joven, proyecto, fechaAlta, fechaBaja)
            return newPert
    
    @staticmethod
    def listaPertenerProyectos():
        bd = BD()
        perts = bd.select('*', PertenecerProyecto.tabla)
        listPerts = []
        for pert in perts:
            joven = Joven(pert[0])
            proyecto = Proyecto(pert[1])
            fechaAlta = pert[2]
            fechaBaja = pert[3]
            newPert = PertenecerProyecto(joven, proyecto, fechaAlta, fechaBaja)
            listPerts.append(newPert)
        return listPerts
    
    #Getters
    def getJoven(self):
        return self.joven

    def getProyecto(self):
        return self.proyecto

    def getFechaAlta(self):
        return self.fechaAlta

    def getFechabaja(self):
        return self.fechaBaja


    #Setters
    def setJoven(self, newJoven):
        #No se puede modificar claves de pertenerProyecto
        return False

    def setProyecto(self, newProyecto):
        #No se puede modificar claves de pertenerProyecto
        return False

    def setFechaAlta(self, newFechaAlta):
        #No se puede modificar fecha de alta de pertenerProyecto
        return False

    def setFechabaja(self, newFechaBaja):
        if newFechaBaja != None:
            bd = BD()
            condicion = 'joven = ' + str(self.joven.getIdjoven()) + ' and proyecto = ' + str(self.proyecto.getIdProyecto())
            setter = 'fecha_de_baja = \'' + newFechaBaja = '\''
            bd.update(PertenecerProyecto.tabla, setter, condicion)
            self.fechaBaja = newFechaBaja
            return True
        else:
            return False

    def delete(self):
        bd = BD()
        condicion = 'joven = ' + str(self.joven.getIdjoven()) + ' and proyecto = ' + str(self.proyecto.getIdProyecto())
        bd.delete(PertenecerProyecto.tabla, condicion)
        self.joven = None
        self.proyecto = None
        self.fechaAlta = None
        self.fechaBaja = None

    def __repr__(self):
        toStr = ''
        toStr += ('Joven: ' + self.joven + ' - ')
        toStr += ('Proyecto: ' + self.proyecto + ' - ')
        toStr += ('Fecha de Alta: ' + self.fechaAlta + ' - ')
        if self.fechaBaja != None:
            toStr += ('Fecha de Baja: ' + self.fechaBaja + ' - ')
        return toStr[:-3]

if __name__ == '__main__':
    print('e')