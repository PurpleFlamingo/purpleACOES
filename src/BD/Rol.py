from BD import BD

class Rol:
    tabla = 'rol'
    def __init__(self, rol_name: str, descripcion: str, modificacion: bool):
        self.rol_name = rol_name
        self.descripcion = descripcion
        self.modificacion = modificacion

    @staticmethod
    def newRol(rol_name: str, descripcion: str, modificacion: bool):
        bd = BD()

        condicion = 'rol_name = \'' + rol_name + '\''
        res = bd.selectEscalar('*', Rol.tabla, condicion)
        if not res:
            valores = [rol_name, descripcion, modificacion]
            bd.insert(valores, Rol.tabla)
            newRol = Rol(rol_name, descripcion, modificacion)
            return newRol
        else:
            print('Error: El nombre de rol {} ya esta en uso'.format(rol_name))
            return None

    @staticmethod
    def getRol(rol_name: str):
        bd = BD()

        condicion = 'rol_name = \'' + rol_name + '\''
        res = bd.selectEscalar('*', Rol.tabla, condicion)
        if not res:
            #El rol no existe
            return None
        else:
            rol_name = res[0]
            descripcion = res[1]
            modificacion = True if (res[2] == 1) else False
            newRol = Rol(rol_name, descripcion, modificacion)
            return newRol

    @staticmethod
    def listaRoles():
        bd = BD()
        roles = bd.select('*', Rol.tabla)
        listRoles = []
        for rol in roles:
            rol_name = rol[0]
            descripcion = rol[1]
            modificacion =  True if (rol[2] == 1) else False
            newRol = Rol(rol_name, descripcion, modificacion)
            listRoles.append(newRol)
        return listRoles

    #Getters
    def getNombre(self):
        return self.rol_name

    def getDescripcion(self):
        return self.descripcion

    def getModificacion(self):
        return self.modificacion

    #Setters

    def setNombre(self, newName: str):
        if newName != None:
            bd = BD()
            condicion = 'rol_name = \'' + newName + '\''
            res = bd.selectEscalar('*', Rol.tabla, condicion)
            if not res:
                condicion = 'rol_name = \'' + self.rol_name + '\''
                setter = 'rol_name = \'' + newName + '\''
                bd.update(Rol.tabla, setter, condicion)
                self.rol_name = newName
                return True
            else:
                #Rol name ya existe
                return False
        else:
            #No se puede insertar nombre null
            return False

    def setDescripcion(self, newDesc: str):
        if newDesc != None:
            bd = BD()
            condicion = 'rol_name = \'' + self.rol_name + '\''
            setter = 'descripcion = \'' + newDesc + '\''
            bd.update(Rol.tabla, setter, condicion)
            self.descripcion = newDesc
            return True
        else:  
            return False
        
    def setModificacion(self, newModificacion: bool):
        if newModificacion != None:
            bd = BD()
            condicion = 'rol_name = \'' + self.rol_name + '\''
            setter = 'modificacion = ' + ('TRUE' if newModificacion else 'FALSE')
            bd.update(Rol.tabla, setter, condicion)
            self.modificacion = newModificacion
            return True
        else:  
            return False


    def delete(self):
        bd = BD()
        condicion = 'rol_name = \'' + self.rol_name + '\''
        bd.delete(Rol.tabla, condicion)
        self.rol_name = None
        self.descripcion = None
        self.modificacion = None
        
    def __repr__(self):
        toStr = ''
        toStr += ('Nombre: ' + self.rol_name + ' - ')
        toStr += ('Descripcion: ' + self.descripcion + ' - ')
        toStr += ('Modificacion: ' + ('Si' if self.modificacion else 'No') + ' - ')
        return toStr[:-3]

if __name__ == '__main__':
    t = Rol.getRol('Hola')
    print(Rol.listaRoles())
    t.delete()
    print(Rol.listaRoles())
    #temp = Rol.getRol('Socio')
    #print('\n\n')
    #print(temp.setModificacion(True))
    #print(Rol.listaRoles())
    #print('\n\n')
    #print(temp.setModificacion(False))
    #print(Rol.listaRoles())