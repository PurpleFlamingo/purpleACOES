import sys
from BD import BD
from Usuario import Usuario

class Socio:

    tabla = 'socio'

    def __init__(self, usuario: int = None, nombre_pila: str = None, apellidos: str = None, nif: str = None
        , direccion: str = None, poblacion: str = None, codigo_postal: str = None, provincia: str = None, estado: str = None
        , telefono1: str = None, telefono2: str = None, correo_electronico: str = None, relacion: str = None
        , sector: str = None, certificado: str = None, fecha_de_alta: str = None, fecha_de_baja: str = None, observaciones: str = None):

        self.usuario = Usuario(usuario) if usuario != None else None
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
        self.sector = sector 
        self.certificado = certificado
        self.fecha_de_alta = fecha_de_alta
        self.fecha_de_baja = fecha_de_baja
        self.observaciones = observaciones

    @staticmethod
    def newSocio(self, usuario: int, nombre_pila: str = None, apellidos: str = None, nif: str = None
        , direccion: str = None, codigo_postal: str = None, provincia: str = None, estado: str = None
        , telefono1: str = None, telefono2: str = None, correo_electronico: str = None, relacion: str = None
        , sector: str = None, certificado: str = None, fecha_de_alta: str, fecha_de_baja: str = None, observaciones: str = None):
        if usuario == None or fecha_de_alta == None:
            print('Error: la identificación del socio o la fecha de alta no pueden ser nulos')
            return None
        if nombre_pila == None:
            nombre_pila = 'null'
        if apellidos == None:
            apellidos = 'null'
        if nif == None:
            nif = 'null'
        if direccion == None:
            direccion = 'null'
        if poblacion == None:
            poblacion = 'null'
        if codigo_postal == None:
            codigo_postal = 'null'
        if provincia == None:
            provincia = 'null'
        if estado == None:
            estado = 'null'
        if telefono1 == None:
            telefono1 = 'null'
        if telefono2 == None:
            telefono2 = 'null'
        if correo_electronico == None:
            correo_electronico = 'null'
        if relacion == None:
            relacion = 'null'
        if certificado == None:
            certificado = 'null'
        if sector == None:
            sector = 'null'
        if fecha_de_baja == None:
            fecha_de_baja = 'null'
        if observaciones == None:
            observaciones = 'null'

        bd = BD() 
            
        #Compruebo la existencia de la clave foranea en su tabla de origen
        condicion = 'usuario = ' + str(usuario)
        resultado = '*'
        ap = bd.selectEscalar(resultado,' usuario ',condicion)
        if not ap:
            print('Usuario no existente')
            return None
            
        #consulto si los valores estan en la tabla
        ap = bd.select('*',Socio.tabla,condicion)

        #inserto los valores en la tabla si no existen
        if not ap:
            valores = [usuario, nombre_pila, apellidos, nif, direccion, poblacion, codigo_postal, provincia, estado, telefono1, telefono2
            , correo_electronico, relacion, certificado, sector, fecha_de_alta, fecha_de_baja, observaciones]
            bd.insert(valores, Socio.tabla)
            #inicializo las variables de la instancia
            newS = Socio(usuario, nombre_pila, apellidos, nif, direccion, poblacion, codigo_postal, provincia, estado, telefono1, telefono2
            , correo_electronico, relacion, certificado, sector, fecha_de_alta, fecha_de_baja, observaciones)
            print(newS)
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
            usuario = Usuario(usuario) if usuario != None else None
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
            sector = ap[12] 
            certificado = ap[13]
            fecha_de_alta = ap[14]
            fecha_de_baja = ap[15]
            observaciones = ap[16]


    #serie de comandos que devuelven los valores de los campos de la instancia
    def getUsuario(self):
        return self.usuario

    def getUsuarioId(self):
        return self.usuario.getIdUsuario()

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
    
    

if __name__ == '__main__':
    