from BD.BD import BD

class Permiso:
    tabla = 'permiso'
    def __init__(self, permiso: str = None, alcance: str = None, descripcion: str = None):
        self.permiso = permiso
        self.alcance = alcance
        self.descripcion = descripcion

    @staticmethod
    def newPermiso(permiso: str, alcance: str, descripcion: str):
        bd = BD()

        condicion = 'permiso = \'' + permiso + '\''
        res = bd.selectEscalar('*', Permiso.tabla, condicion)
        if not res:
            valores = [permiso, alcance, descripcion]
            bd.insert(valores, Permiso.tabla)
            newPermiso = Permiso(permiso, alcance, descripcion)
            return newPermiso
        else:
            print('Error: El nombre de permiso {} ya esta en uso'.format(permiso))
            return None

    @staticmethod
    def getPermiso(permiso: str):
        bd = BD()

        condicion = 'permiso = \'' + permiso + '\''
        res = bd.selectEscalar('*', Permiso.tabla, condicion)
        if not res:
            #El permiso no existe
            return None
        else:
            permiso = res[0]
            alcance = res[1]
            descripcion = res[2]
            newPermiso = Permiso(permiso, alcance, descripcion)
            return newPermiso

    @staticmethod
    def listaPermisos():
        bd = BD()
        permisos = bd.select('*', Permiso.tabla)
        listPermisos = []
        for perm in permisos:
            permiso = perm[0]
            alcance = perm[1]
            descripcion =  perm[2]
            newPermiso = Permiso(permiso, alcance, descripcion)
            listPermisos.append(newPermiso)
        return listPermisos

    #Getters
    def getNombre(self):
        return self.permiso

    def getAlcance(self):
        return self.alcance

    def getDescripcion(self):
        return self.descripcion

    #Setters

    def setNombre(self, newName: str = None):
        if newName != None:
            bd = BD()
            condicion = 'permiso = \'' + newName + '\''
            res = bd.selectEscalar('*', Permiso.tabla, condicion)
            if not res:
                condicion = 'permiso = \'' + self.permiso + '\''
                setter = 'permiso = \'' + newName + '\''
                bd.update(Permiso.tabla, setter, condicion)
                self.permiso = newName
                return True
            else:
                #Permiso ya existe
                return False
        else:
            #No se puede insertar nombre null
            return False

    def setAlcance(self, newAlcance: str = None):
        if newAlcance != None:
            bd = BD()
            condicion = 'permiso = \'' + self.permiso + '\''
            setter = 'alcance = \'' + newAlcance + '\''
            bd.update(Permiso.tabla, setter, condicion)
            self.alcance = newAlcance
            return True
        else:
            return False

    def setDescripcion(self, newDesc: str = None):
        if newDesc != None:
            bd = BD()
            condicion = 'permiso = \'' + self.permiso + '\''
            setter = 'descripcion_del_alcance = \'' + newDesc + '\''
            bd.update(Permiso.tabla, setter, condicion)
            self.descripcion = newDesc
            return True
        else:
            return False

    def delete(self):
        bd = BD()
        condicion = 'permiso = \'' + self.permiso + '\''
        bd.delete(Permiso.tabla, condicion)
        self.permiso = None
        self.alcance = None
        self.descripcion = None

    def __repr__(self):
        cadena = ''
        if self.permiso != None: 
            cadena += ('Nombre: ' + self.permiso + ' - ')
        if self.alcance != None:
            cadena += ('Alcance: ' + self.alcance + ' - ')
        if self.descripcion != None:
            cadena += ('Descripcion: ' + self.descripcion + ' - ')
        if cadena == '':
            cadena = 'Permiso sin inicializar - ' 
        return cadena[:-3]
       

if __name__ == '__main__':
    print(Permiso.getPermiso('asd'))
    print(Permiso.listaPermisos())
    temp = Permiso.getPermiso('Hola')
    #print('\n\n')
    #print(temp.setDescripcion('Adios'))
    #print(Permiso.listaPermisos())
    #print('\n\n')
    #print(temp.setDescripcion('Esto en una pruebaca impresionante'))
    temp.delete()
    print(Permiso.listaPermisos())
