from BD.BD import BD

class Voluntario:
    tabla = 'voluntario'
    def __init__(self, usuario, nombre, apellidos, nif, fechaNacimiento, fechaAlta, correoElectronico, telefono, direccion, codigoPostal, provincia, estado):
        self.usuario = usuario
        self.nombre = nombre
        self.apellidos = apellidos
        self.nif = nif
        self.fechaNacimiento = fechaNacimiento
        self.fechaAlta = fechaAlta
        self.correoElectronico = correoElectronico
        self.telefono = telefono
        self.direccion = direccion
        self.codigoPostal = codigoPostal
        self.provincia = provincia
        self.estado = estado

    @staticmethod
    def newVoluntario(usuario, nombre, apellidos, nif, fechaNacimiento, fechaAlta, correoElectronico, telefono, direccion, codigoPostal, provincia, estado):
        bd = BD()
        if nif == None:
            nif = 'null'
        if fechaNacimiento == None:
            fechaNacimiento = 'null'
        if correoElectronico == None:
            correoElectronico = 'null'
        if telefono == None:
            telefono = 'null'
        
        condicion = 'usuario = ' + str(usuario)
        res = bd.selectEscalar('*', Voluntario.tabla, condicion)
        if not res:
            valores = [usuario, nombre, apellidos, nif, fechaNacimiento, fechaAlta, correoElectronico, telefono, direccion, codigoPostal, provincia, estado]
            
            bd.insert(valores, Voluntario.tabla)
            newVol = Voluntario(usuario, nombre, apellidos, nif, fechaNacimiento, fechaAlta, correoElectronico, telefono, direccion, codigoPostal, provincia, estado)
            return newVol
        else:
            print('Error: La id {} ya esta en uso'.format(usuario))
            return None

    @staticmethod
    def getVoluntario(usuario):
        bd = BD()
        cond = 'usuario = ' + str(usuario)
        vol = bd.selectEscalar('*', Voluntario.tabla, cond)
        if not vol:
            #El voluntario solicitado no existe
            return None
        else:
            usuario = vol[0]
            nombre = vol[1]
            apellidos = vol[2]
            nif = vol[3]
            fechaNacimiento = vol[4]
            fechaAlta = vol[5]
            correoElectronico  = vol[6]
            telefono = vol[7]
            direccion = vol[8]
            codigoPostal = vol[9]
            provincia = vol[10]
            estado = vol[11]
            newVol = Voluntario(usuario, nombre, apellidos, nif, fechaNacimiento, fechaAlta, correoElectronico, telefono, direccion, codigoPostal, provincia, estado)
            return newVol




    @staticmethod
    def listaVoluntarios():
        bd = BD()
        voluntarios = bd.select('*', Voluntario.tabla)
        listVoluntarios = []
        for vol in voluntarios:
            usuario = vol[0]
            nombre = vol[1]
            apellidos = vol[2]
            nif = vol[3]
            fechaNacimiento = vol[4]
            fechaAlta = vol[5]
            correoElectronico  = vol[6]
            telefono = vol[7]
            direccion = vol[8]
            codigoPostal = vol[9]
            provincia = vol[10]
            estado = vol[11]
            newVol = Voluntario(usuario, nombre, apellidos, nif, fechaNacimiento, fechaAlta, correoElectronico, telefono, direccion, codigoPostal, provincia, estado)   
            listVoluntarios.append(newVol)
        return listVoluntarios

    #Getters
    def getUsuario(self):
        return self.usuario

    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos

    def getNif(self):
        return self.nif

    def getfechaNacimiento(self):
        return self.fechaNacimiento

    def getFechaAlta(self):
        return self.fechaAlta

    def getCorreoElectronico(self):
        return self.correoElectronico

    def getTelefono(self):
        return self.telefono

    def getDireccion(self):
        return self.direccion

    def getCodigoPostal(self):
        return self.codigoPostal

    def getProvincia(self):
        return self.provincia

    def getEstado(self):
        return self.estado



    #Setters
    def setUsuario(self, newUsuario: int):
        if newUsuario != None:
            bd = BD()
            condicion = 'usuario = \'' + newUsuario + '\''
            res = bd.selectEscalar('*', Voluntario.tabla, condicion)
            if not res:
                condicion = 'usuario = \'' + self.usuario + '\''
                setter = 'usuario = \'' + newUsuario + '\''
                bd.update(Voluntario.tabla, setter, condicion)
                self.usuario = newUsuario
                return True
            else:
                #Usuario ya existe
                return False
        else:
            #No se puede insertar usuario null
            return False

    def setNombre(self, newNombre: str):
        if newNombre != None:
            bd = BD()
            condicion = 'usuario = \'' + self.usuario + '\''
            setter = 'nombre_pila = \'' + newNombre + '\''
            bd.update(Voluntario.tabla, setter, condicion)
            self.nombre = newNombre
            return True
        else:
            return False

    def setApellidos(self, newApellidos: str):
        if newApellidos != None:
            bd = BD()
            condicion = 'usuario = \'' + self.usuario + '\''
            setter = 'apellidos = \'' + newApellidos + '\''
            bd.update(Voluntario.tabla, setter, condicion)
            self.apellidos = newApellidos
            return True
        else:
            return False

    def setNif(self, newNif: str):
        if newNif != None:
            bd = BD()
            condicion = 'usuario = \'' + self.usuario + '\''
            setter = 'nif = \'' + newNif + '\''
            bd.update(Voluntario.tabla, setter, condicion)
            self.nif = newNif
            return True
        else:
            return False

    def setfechaNacimiento(self, newFechaNacimiento: str):
        if newFechaNacimiento != None:
            bd = BD()
            condicion = 'usuario = \'' + self.usuario + '\''
            setter = 'fecha_nacimiento = \'' + newFechaNacimiento + '\''
            bd.update(Voluntario.tabla, setter, condicion)
            self.fechaNacimiento = newFechaNacimiento
            return True
        else:
            return False

    def setFechaAlta(self, newFechaAlta: str):
        if newFechaAlta != None:
            bd = BD()
            condicion = 'usuario = \'' + self.usuario + '\''
            setter = 'fecha_alta = \'' + newFechaAlta + '\''
            bd.update(Voluntario.tabla, setter, condicion)
            self.fechaAlta = newFechaAlta
            return True
        else:
            return False

    def setCorreoElectronico(self, newCorreo: str):
        if newCorreo != None:
            bd = BD()
            condicion = 'usuario = \'' + self.usuario + '\''
            setter = 'correo_electronico = \'' + newCorreo + '\''
            bd.update(Voluntario.tabla, setter, condicion)
            self.correoElectronico = newCorreo
            return True
        else:
            return False

    def setTelefono(self, newTelefono: str):
        if newTelefono != None:
            bd = BD()
            condicion = 'usuario = \'' + self.usuario + '\''
            setter = 'telefono_contacto = \'' + newTelefono + '\''
            bd.update(Voluntario.tabla, setter, condicion)
            self.telefono = newTelefono
            return True
        else:
            return False

    def setDireccion(self, newDireccion: str):
        if newDireccion != None:
            bd = BD()
            condicion = 'usuario = \'' + self.usuario + '\''
            setter = 'direccion = \'' + newDireccion + '\''
            bd.update(Voluntario.tabla, setter, condicion)
            self.direccion = newDireccion
            return True
        else:
            return False

    def setCodigoPostal(self, newCodigo: str):
        if newCodigo != None:
            bd = BD()
            condicion = 'usuario = \'' + self.usuario + '\''
            setter = 'codigo_postal = \'' + newCodigo + '\''
            bd.update(Voluntario.tabla, setter, condicion)
            self.codigoPostal = newCodigo
            return True
        else:
            return False

    def setProvincia(self, newProvincia: str):
        if newProvincia != None:
            bd = BD()
            condicion = 'usuario = \'' + self.usuario + '\''
            setter = 'provincia = \'' + newProvincia + '\''
            bd.update(Voluntario.tabla, setter, condicion)
            self.provincia = newProvincia
            return True
        else:
            return False

    def setEstado(self, newEstado: str):
        if newEstado != None:
            bd = BD()
            condicion = 'usuario = \'' + self.usuario + '\''
            setter = 'estado = \'' + newEstado + '\''
            bd.update(Voluntario.tabla, setter, condicion)
            self.estado = newEstado
            return True
        else:
            return False

    def delete(self):
        bd = BD()
        condicion = 'usuario = ' + str(self.usuario)
        bd.delete(Voluntario.tabla, condicion)
        self.usuario = None
        self.nombre = None
        self.apellidos = None
        self.nif = None
        self.fechaNacimiento = None
        self.fechaAlta = None
        self.correoElectronico = None
        self.telefono = None
        self.direccion = None
        self.codigoPostal = None
        self.provincia = None
        self.estado = None

    def __repr__(self):
        toStr = ''
        if self.usuario is not None:
            toStr+=('ID Usuario: ' + str(self.usuario) + ' - ')
        if self.nombre is not None:
            toStr+=('Nombre: ' + self.nombre + ' - ')
        if self.apellidos is not None:
            toStr+=('Apellidos: ' + self.apellidos + ' - ')
        if self.nif is not None:
            toStr+=('Nif: ' + self.nif + ' - ')
        if self.fechaNacimiento is not None:
            toStr+=('Fecha de Naciemiento: ' + self.fechaNacimiento.strftime('%Y-%m-%d') + ' - ')
        if self.fechaAlta is not None:
            toStr+=('Fecha de Alta: ' + self.fechaAlta.strftime('%Y-%m-%d') + ' - ')
        if self.correoElectronico is not None:
            toStr+=('Correo Electronico: ' + self.correoElectronico + ' - ')
        if self.telefono is not None:
            toStr+=('Telefono: ' + self.telefono + ' - ')
        if self.direccion is not None:
            toStr+=('Direccion: ' + self.direccion + ' - ')
        if self.codigoPostal is not None:
            toStr+=('Codigo Postal: ' + self.codigoPostal + ' - ')
        if self.provincia is not None:
            toStr+=('Provincia: ' + self.provincia + ' - ')
        if self.estado is not None:
            toStr+=('Estado: ' + self.estado + ' - ')  
        return toStr[:-3]
    
if __name__ == '__main__':
    lista = Voluntario.listaVoluntarios()
    print(lista)
    v = Voluntario.getVoluntario(16)
    #v2 = Voluntario.newVoluntario(99,'aa', 'bb', 'c', '2019-1-1', '2019-2-2', 'c', 'c', 'c', 'c', 'c', 'c')
    lista = Voluntario.listaVoluntarios()