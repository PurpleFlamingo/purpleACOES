import sys
from BD.BD import BD
from BD.Usuario import Usuario

class Socio:

    tabla = 'socio'

    def __init__(self, usuario: int = None, nombre_pila: str = None, apellidos: str = None, nif: str = None
        , direccion: str = None, poblacion: str = None, codigo_postal: str = None, provincia: str = None, estado: str = None
        , telefono1: str = None, telefono2: str = None, correo_electronico: str = None, relacion: str = None
        , certificado: int = None,  sector: str = None, fecha_de_alta: str = None, fecha_de_baja: str = None, observaciones: str = None, cuota: int= None):

        self.usuario = Usuario.getUsuario(usuario) if usuario != None else None
        self.nombre_pila = nombre_pila
        self.apellidos = apellidos 
        self.nif = nif 
        self.direccion = direccion 
        self.poblacion = poblacion
        self.codigo_postal = codigo_postal 
        self.provincia = provincia
        self.estado = estado 
        self.telefono1 = telefono1
        self.telefono2 =  telefono2
        self.correo_electronico = correo_electronico
        self.relacion = relacion
        self.certificado = certificado
        self.sector = sector 
        self.fecha_de_alta = fecha_de_alta
        self.fecha_de_baja = fecha_de_baja
        self.observaciones = observaciones
        self.cuota = cuota

    @staticmethod
    def newSocio(usuario: int = None, nombre_pila: str = None, apellidos: str = None, nif: str = None, direccion: str = None
        , poblacion: str = None, codigo_postal: str = None, provincia: str = None, estado: str = None, telefono1: str = None
                 , telefono2: str = None, correo_electronico: str = None, relacion: str = None, certificado: int = None, sector: str = None
        , fecha_de_alta: str = None, fecha_de_baja: str = None, observaciones: str = None, cuota: str = None):
        if usuario == None or fecha_de_alta == None:
            print('Error: la identificación del socio o la fecha de alta no pueden ser nulos')
            return None

        bd = BD() 
            
        #Compruebo la existencia de la clave foranea en su tabla de origen
        condicion = 'id_usuario = ' + str(usuario)
        resultado = '*'
        ap = bd.selectEscalar(resultado,' usuario ',condicion)
        if not ap:
            print('Usuario no existente')
            return None
            
        condicion = 'usuario = ' + str(usuario) 
        #consulto si los valores estan en la tabla
        ap = bd.select('*',Socio.tabla,condicion)

        #inserto los valores en la tabla si no existen
        if not ap:
            valores = [usuario, nombre_pila if nombre_pila != None else 'null', apellidos if apellidos != None else 'null', nif if nif != None else 'null', direccion if direccion != None else 'null', poblacion if poblacion != None else 'null', codigo_postal if codigo_postal != None else 'null', provincia if provincia != None else 'null', estado if estado != None else 'null', telefono1 if telefono1 != None else 'null', telefono2 if telefono2  != None else 'null', correo_electronico if correo_electronico != None else 'null', relacion if relacion != None else 'null', certificado if certificado != None else 'null', sector if sector != None else 'null', fecha_de_alta, fecha_de_baja if fecha_de_baja != None else 'null', observaciones if observaciones != None else 'null', cuota if cuota != None else 'null']
            #print('Los valores a ingresar en la tabla son: ',valores)

            bd.insert(valores, Socio.tabla)
            #inicializo las variables de la instancia
            newS = Socio(usuario, nombre_pila, apellidos, nif, direccion, poblacion, codigo_postal, provincia, estado, telefono1, telefono2
            , correo_electronico, relacion, certificado, sector, fecha_de_alta, fecha_de_baja, observaciones, cuota)
            #print(newS)
            return newS
        else:
            print('Error: La id {} ya esta en uso',format(usuario))
            return None
               
    #dado un valor de la clave se lo busca en la tabla y se crea una instancia de la clase con esos valores y en caso de no existir se 
    # devuelve el valor nulo (None) 
    @staticmethod
    def getSocio(usuario):
        bd = BD()
        condicion = 'usuario = ' + str(usuario)
        resultado = '*'
        ap = bd.selectEscalar(resultado,Socio.tabla,condicion)
        if not ap:
            print('Usuario no existente')
            return None
        else:
            usuario = usuario
            nombre_pila = ap[1]
            apellidos = ap[2] 
            nif = ap[3] 
            direccion = ap[4] 
            poblacion = ap[5]
            codigo_postal = ap[6] 
            provincia = ap[7]
            estado = ap[8] 
            telefono1 = ap[9]
            telefono2 =  ap[10]
            correo_electronico = ap[11]
            relacion = ap[12]
            certificado = ap[13]
            sector = ap[14]
            fecha_de_alta = ap[15]
            if not fecha_de_alta:
                fecha_de_alta = None
            else:
                fecha_de_alta = fecha_de_alta.strftime('%Y-%m-%d')
            fecha_de_baja = ap[16]
            if not fecha_de_baja:
                fecha_de_baja = None
            else:
                fecha_de_baja = fecha_de_baja.strftime('%Y-%m-%d')
            observaciones = ap[17]
            cuota = ap[18]
            newSocio = Socio(usuario, nombre_pila, apellidos, nif, direccion, poblacion, codigo_postal
                        , provincia, estado, telefono1, telefono2, correo_electronico, relacion, certificado
                        , sector, fecha_de_alta, fecha_de_baja, observaciones, cuota)
            return (newSocio)


    #serie de comandos que devuelven los valores de los campos de la instancia
    def getUsuario(self):
        return self.usuario

    def getUsuarioId(self):
        return self.usuario.getIdUsuario()

    def getNif(self):
        return self.nif

    def getNombreDePila(self):
        return self.nombre_pila

    def getApellidos(self):
        return self.apellidos

    def getDireccion(self):
        return self.direccion

    def getPoblacion(self):
        return self.poblacion

    def getCodigoPostal(self):
        return self.codigo_postal

    def getProvincia(self):
        return self.provincia
    
    def getEstado(self):
        return self.estado
    
    def getTelefono1(self):
        return self.telefono1
    
    def getTelefono2(self):
        return self.telefono2
    
    def getCorreoElectronico(self):
        return self.correo_electronico
    
    def getRelacion(self):
        return self.relacion
    
    def getCertificado(self):
        return self.certificado
    
    def getSector(self):
        return self.sector
    
    def getFechaDeAlta(self):
        return self.fecha_de_alta
    
    def getFechaDeBaja(self):
        return self.fecha_de_baja
    
    def getObservaciones(self):
        return self.observaciones

    def getCuota(self):
        return self.cuota
    
    def delete(self):
        bd = BD()
        condicion = 'nif = \'' + str(self.nif) + '\''
        bd.delete(Socio.tabla, condicion)
        self.usuario = None
        self.nombre_pila = None
        self.apellidos = None
        self.nif = None
        self.direccion = None
        self.poblacion = None
        self.codigo_postal = None
        self.provincia = None
        self.estado = None
        self.telefono1 = None
        self.telefono2 = None
        self.correo_electronico = None
        self.relacion = None
        self.sector = None
        self.certificado = None
        self.fecha_de_alta = None
        self.fecha_de_baja = None
        self.observaciones = None
        self.cuota = None

    def setUsuario(self):
        print ('El id de usuaro no es modificable, es autoincremental')
        return False

    def setNombrePila(self, nombre_pila:str = None):
        if nombre_pila != None:
            bd = BD()
            condicion = 'usuario = ' + str(self.usuario.getIdUsuario())
            setter = 'nombre_pila = \'' + nombre_pila + '\''
            bd.update(Socio.tabla, setter, condicion)
            self.nombre_pila = nombre_pila
        else:
            print('El nombre de pila no puede ser null')
            return False

    def setApellidos(self, apellidos:str = None):
        if apellidos != None:
            bd = BD()
            condicion = 'usuario = ' + str(self.usuario.getIdUsuario())
            setter = 'apellidos = \'' + apellidos + '\''
            bd.update(Socio.tabla, setter, condicion)
            self.apellidos = apellidos
        else:
            print('Los apellidos no pueden ser null')
            return False

    def setNif(self, nif:str = None):
        if nif != None:
            bd = BD()
            condicion = 'nif = \'' + nif + '\''
            resultado = '*'
            ap = bd.selectEscalar(resultado, Socio.tabla, condicion)
            if ap == None or ap == []:
                condicion = 'usuario = ' + str(self.usuario.getIdUsuario())
                setter = 'nif = \'' + nif + '\''
                bd.update(Socio.tabla, setter, condicion)
                self.nif = nif
            else:
                print('Nif existente')
                return False
        else:
            print('El nif no puede ser null')
            return False

    def setDireccion(self, direccion:str = None):
        if direccion != None:
            bd = BD()
            condicion = 'usuario = ' + str(self.usuario.getIdUsuario())
            setter = 'direccion = \'' + direccion + '\''
            bd.update(Socio.tabla, setter, condicion)
            self.direccion = direccion
        else:
            print('La direccion no puede ser null')
            return False

    def setPoblacion(self, poblacion:str = None):
        if poblacion != None:
            bd = BD()
            condicion = 'usuario = ' + str(self.usuario.getIdUsuario())
            setter = 'poblacion = \'' + poblacion + '\''
            bd.update(Socio.tabla, setter, condicion)
            self.poblacion = poblacion
        else:
            print('La poblacion no pueden ser null')
            return False

    def setCodigoPostal(self, codigo_postal: str = None):
        if codigo_postal != None:
            bd = BD()
            condicion = 'usuario = ' + str(self.usuario.getIdUsuario())
            setter = 'codigo_postal = \'' + codigo_postal + '\''
            bd.update(Socio.tabla, setter, condicion)
            self.codigo_postal = codigo_postal
        else:
            print('Los apellidos no pueden ser null')
            return False

    def setProvincia(self, provincia: str = None):
        if provincia != None:
            bd = BD()
            condicion = 'usuario = ' + str(self.usuario.getIdUsuario())
            setter = 'provincia = \'' + provincia + '\''
            bd.update(Socio.tabla, setter, condicion)
            self.provincia = provincia
        else:
            print('La provincia no puede ser null')
            return False

    def setEstado(self, estado: str = None):
        if estado != None:
            bd = BD()
            condicion = 'usuario = ' + str(self.usuario.getIdUsuario())
            setter = 'estado = \'' + estado + '\''
            bd.update(Socio.tabla, setter, condicion)
            self.estado = estado
        else:
            print('El estado no puede ser null')
            return False

    def setTelefono1(self, telefono1: str = None):
        if telefono1 != None:
            bd = BD()
            condicion = 'usuario = ' + str(self.usuario.getIdUsuario())
            setter = 'telefono1 = \'' + telefono1 + '\''
            bd.update(Socio.tabla, setter, condicion)
            self.telefono1 = telefono1
        else:
            print('El telefono1 no puede ser null')
            return False

    def setTelefono2(self, telefono2: str = None):
        bd = BD()
        condicion = 'usuario = ' + str(self.usuario.getIdUsuario())
        setter = 'telefono2 = \'' + telefono2 + '\''
        bd.update(Socio.tabla, setter, condicion)
        self.telefono2 = telefono2

    def setCorreoElectronico(self, correo_electronico: str = None):
        if correo_electronico != None:
            bd = BD()
            condicion = 'correo_electronico = \'' + correo_electronico + '\''
            resultado = '*'
            ap = bd.selectEscalar(resultado, Socio.tabla, condicion)
            if ap == None or ap == []:
                condicion = 'usuario = ' + str(self.usuario.getIdUsuario())
                setter = 'correo_electronico = \'' + correo_electronico + '\''
                bd.update(Socio.tabla, setter, condicion)
                self.correo_electronico = correo_electronico
            else:
                print ('Correo electronico existente')
                return False
        else:
            print('El correo electronico no puede ser null')
            return False

    def setRelacion(self, relacion: str = None):
            bd = BD()
            condicion = 'usuario = ' + str(self.usuario.getIdUsuario())
            setter = 'relacion = \'' + relacion + '\''
            bd.update(Socio.tabla, setter, condicion)
            self.relacion = relacion

    def setSector(self, sector: str = None):
            bd = BD()
            condicion = 'usuario = ' + str(self.usuario.getIdUsuario())
            setter = 'sector = \'' + sector + '\''
            bd.update(Socio.tabla, setter, condicion)
            self.sector = sector

    def setCertificado(self, certificado: int = None):
        bd = BD()
        condicion = 'usuario = ' + str(self.usuario.getIdUsuario())
        setter = 'certificado = ' + str(certificado)
        bd.update(Socio.tabla, setter, condicion)
        self.certificado = certificado

    def setFechaDeAlta(self, fecha_de_alta: str = None):
        if fecha_de_alta != None:
            bd = BD()
            condicion = 'usuario = ' + str(self.usuario.getIdUsuario())
            setter = 'fecha_de_alta = \'' + fecha_de_alta + '\''
            bd.update(Socio.tabla, setter, condicion)
            self.fecha_de_alta = fecha_de_alta
        else:
            print('La fecha de alta no puede ser null')
            return False

    def setFechaDeBaja(self, fecha_de_baja: str = None):
        bd = BD()
        condicion = 'usuario = ' + str(self.usuario.getIdUsuario())
        if not fecha_de_baja:
            setter = 'fecha_de_baja = null'
        else:
            setter = 'fecha_de_baja = \'' + fecha_de_baja + '\''
        print('Setter = ',setter)
        bd.update(Socio.tabla, setter, condicion)
        self.fecha_de_baja = fecha_de_baja

    def setObservaciones(self, observaciones: str = None):
        bd = BD()
        condicion = 'usuario = \'' + str(self.usuario) + '\''
        setter = 'observaciones = \'' + observaciones + '\''
        bd.update(Socio.tabla, setter, condicion)
        self.observaciones = observaciones

    def setCuota(self, cuota: int = None):
        bd = BD()
        condicion = 'usuario = \'' + str(self.usuario) + '\''
        setter = 'cuota = ' + str(cuota) 
        bd.update(Socio.tabla, setter, condicion)
        self.observaciones = observaciones


    @staticmethod
    def listaSocios():
        bd = BD()
        condicion = None
        soc = bd.select('*',Socio.tabla,condicion)
        #creo una lista vacia (que se usara para devolver el resultado)
        lista = []
        #cada tupla en la lista obtenida en la consulta se usa para crear una instancia de apadrinamiento y se agregan a la lista vacia
        for ap in soc:
            usuario = ap[0] 
            nombre_pila = ap[1]
            apellidos = ap[2] 
            nif = ap[3] 
            direccion = ap[4] 
            poblacion = ap[5]
            codigo_postal = ap[6] 
            provincia = ap[7]
            estado = ap[8] 
            telefono1 = ap[9]
            telefono2 =  ap[10]
            correo_electronico = ap[11]
            relacion = ap[12]
            sector = ap[13]
            certificado = ap[14]
            fecha_de_alta = ap[15].strftime('%Y-%m-%d')
            fecha_de_baja = ap[16].strftime('%Y-%m-%d') if ap[16] != None else None
            observaciones = ap[17]
            cuota = ap[18]
            newSocio = Socio(usuario, nombre_pila, apellidos, nif, direccion, poblacion, codigo_postal
                        , provincia, estado, telefono1, telefono2, correo_electronico, relacion, certificado
                        , sector, fecha_de_alta, fecha_de_baja, observaciones,cuota)
            lista.append(newSocio)
        return lista

    # método que retorna una representación de la instancia de la clase
    def __repr__(self):
        cadena = ''
        if self.usuario != None and self.usuario != 'null':
            cadena += 'Usuario ' + str(self.usuario.getIdUsuario()) + ' - '
        if self.nombre_pila != None and self.nombre_pila != 'null':
            cadena += 'Nombre de pila ' + self.nombre_pila + ' - '
        if self.apellidos != None and self.apellidos != 'null':
            cadena += 'Apellidos ' + self.apellidos + ' - '
        if self.nif != None and self.nif != 'null':
            cadena += 'NIF ' + self.nif + ' - '
        if self.direccion != None and self.direccion != 'null':
            cadena += 'Direccion ' + self.direccion + ' - '
        if self.poblacion != None and self.poblacion != 'null':
            cadena += 'Poblacion ' + self.poblacion + ' - '
        if self.codigo_postal != None and self.codigo_postal != 'null':
            cadena += 'Codigo Postal ' + self.codigo_postal + ' - '
        if self.provincia != None and self.provincia != 'null':
            cadena += 'Provincia ' + self.provincia + ' - '
        if self.estado != None and self.estado != 'null':
            cadena += 'Pais ' + self.estado + ' - '
        if self.telefono1 != None and self.telefono1 != 'null':
            cadena += 'Telefono 1 ' + self.telefono1 + ' - '
        if self.telefono2 != None and self.telefono2 != 'null':
            cadena += 'Telefono 2 ' + self.telefono2 + ' - '
        if self.correo_electronico != None and self.correo_electronico != 'null':
            cadena += 'Correo Electronico ' + self.correo_electronico + ' - '
        if self.relacion != None and self.relacion != 'null':
            cadena += 'Relacion ' + self.relacion + ' - '
        if self.certificado != None and self.certificado != 'null':
            cadena += 'Certificado ' + ('Si' if self.certificado else 'No') + ' - '
        if self.sector != None and self.sector != 'null':
            cadena += 'Sector ' + self.sector + ' - '
        if self.fecha_de_alta != None and self.fecha_de_alta != 'null':
            cadena += 'Fecha de alta ' + self.fecha_de_alta + ' - '
        if self.fecha_de_baja != None and self.fecha_de_baja != 'null':
            cadena += 'Fecha de baja ' + self.fecha_de_baja + ' - '
        if self.observaciones != None and self.observaciones != 'null':
            cadena += 'Observaciones ' + self.observaciones + ' - '
        if self.cuota != None:
            cadena += 'Cuota ' + str(self.cuota) + ' - '
        if cadena == '':
            cadena = 'Socio sin inicializar - '
        return cadena[:-3]

if __name__ == '__main__':
    pass
