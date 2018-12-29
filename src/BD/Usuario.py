import sys
from BD.BD import BD
from BD.Rol import Rol
from BD.Permiso import Permiso


class Usuario:

    tabla = 'usuario'

    def __init__(self, id_usuario: int = None, nombre: str = None, clave: str = None, rol: str = None, permiso: str = None):
            self.id_usuario = id_usuario
            self.nombre = nombre
            self.clave = clave
            self.rol = Rol(rol) if rol != None else None
            self.permiso = Permiso(permiso) if permiso != None else None

    @staticmethod
    def newUsuario(self, nombre: str, clave: str, rol: str, permiso: str):
            if nombre == None or clave == None or rol == None or permiso == None:
                print('Error: ningún dato de un usuario puede ser nulo')
                return None
            bd = BD() 
            
            #compruebo que las claves foraneas existen en sus tablas de origen (rol, permiso)
            condicion = ' rol_name = ' + str(rol)
            ap = estaEnLaTabla(' rol ',condicion)
            if not ap:
                print('Rol no existente')
                return None
            condicion = ' permiso = ' + str(permiso)
            ap = estaEnLaTabla(' permiso ',condicion)
            if not ap:
                print('Permiso no existente')
                return None
            
            #consulto si los valores estan en la tabla
            condicion = ' nombre = ' + nombre
            ap = bd.select('*',Usuario.tabla,condicion)

            #inserto los valores en la tabla si no existen
            if not ap:
                valores = ['null',nombre, clave, rol, permiso]
                bd.insert(valores, Colegio.tabla)
                #inicializo las variables de la instancia
                #obtengo el id del usuario (que es autoincremental)
                resultado = ' MAX(id_usuario) '
                user = bd.selectEscalar(resultado, Usuario.tabla,None)
                newCol = Colegio(user, nombre, clave, rol, permiso)
                print(newCol)
                return newCol
            else:
                print('Error: El usuario {} ya esta en uso',format(nombre))
                return None
               
    #dado un valor de la clave se lo busca en la tabla y se crea una instancia de la clase con esos valores y en caso de no existir se 
    # devuelve el valor nulo (None) 
    @staticmethod
    def getSocio(id_usuario):
        bd = BD()
        condicion = 'id_usuario = ' + str(id_usuario)
        resultado = '*'
        ap = bd.selectEscalar(resultado,Usuario.tabla,condicion)
        if not ap:
            print('Usuario no existente')
            return None
        else:
            id_usuario = id_usuario
            nombre = ap[1]
            clave = ap[2]
            rol = Rol(ap[3]) if ap[3] != None else None
            permiso = Permiso(ap[4]) if ap[4] != None else None

    #metodo que comprueba si la condicion pasada como parametro devuelve tuplas en la query o si esta devuele un nulo 
    #el resultado es verdadero si se devuelve una tupla (o una lista de tuplas) y falso si no se encuentran tuplas
    def estaEnLaTabla(self, tabla: str, condicion: str)
        bd = BD()
        resultado = '*'
        ap = bd.selectEscalar(resultado,tabla,condicion)
        return ap != None

    #serie de comandos que devuelven los valores de los campos de la instancia
    def getIdUsuario(self):
        return self.id_usuario

    def getNombre(self):
        return self.nombre

    def getClave(self):
        return self.clave

    def getRol(self):
        return self.rol

    def getRolId(self):
        return self.rol.getRol()

    def getPermiso(self):
        return self.permiso

    def getPermisoId(self):
        return self.permiso.getPermiso()

    #se borra la instancia actual de apadrinamiento de la base de datos y la instancia se convierte en nula
    def delete(self):
        bd = BD()   
        condicion = 'id_usuario = ' + str(self.id_usuario)
        bd.delete(Usuario.tabla,condicion)
        self.id_usuario = None
        self.nombre = None
        self.clave = None
        self.rol = None
        self.permiso = None

    def setIdUsuario(self):
        print('El id de usuario no es modificable, es autoincremental')
        return False

    def setNombre(self, nombre: str = None):
        #comprobación de que el valor no sea nulo
        if nombre != None:
            bd = BD()
            condicion = 'nombre = ' + nombre
            resultado = '*'
            ap = bd.selectEscalar(resultado,Usuario.tabla,condicion)
            #compruebo que el valor no existe en la tabla para no incumplir la unicidad del atributo
            if ap == None or ap == []:
                condicion = 'id_usuario = ' + str(self.id_usuario)
                setter = 'nombre = ' + nombre
                bd.update(Usuario.tabla,setter,condicion)
                self.nombre = nombre
            else:
                print ('Nombre de usuario existente')
                return False
        else:
            print ('El nombre de usuario no puede ser null')
            return False     

    def setClave(self, clave: str = None):
        #comprobación de que el valor no sea nulo
        if clave != None:
            bd = BD()
            condicion = 'id_usuario = ' + str(self.id_usuario)
            setter = 'clave = ' + clave
            bd.update(Usuario.tabla,setter,condicion)
            self.clave = clave
        else:
            print ('La clave no puede ser null')
            return False           

    def setRol(self, rol: str = None):
        #comprobación de que el valor no sea nulo
        if rol != None:
            bd = BD()
            condicion = 'rol_name = ' + rol
            resultado = '*'
            ap = bd.selectEscalar(resultado,' rol ',condicion)
            #compruebo que el valor existe en su tabla, por ser en apadrinamiento una clave foranea
            if ap != None:
                condicion = 'id_usuario = ' + str(self.id_usuario)
                setter = 'rol = ' + rol
                bd.update(Usuario.tabla,setter,condicion)
                self.rol = Rol(rol) if rol != None else None
            else:
                 print ('Rol no existente')
                 return False
        else:
            print ('El rol no puede ser null')
            return False

    def setPermiso(self, permiso: str = None):
        #comprobación de que el valor no sea nulo
        if permiso != None:
            bd = BD()
            condicion = 'permiso = ' + permiso 
            resultado = '*'
            ap = bd.selectEscalar(resultado,' permiso ',condicion)
            #compruebo que el valor existe en su tabla, por ser en apadrinamiento una clave foranea
            if ap != None:
                condicion = 'id_usuario = ' + str(self.id_usuario)
                setter = 'permiso = ' + permiso
                bd.update(Usuario.tabla,setter,condicion)
                self.permiso = Permiso(permiso) if permiso != None else None
            else:
                 print ('Permiso no existente')
                 return False
        else:
            print ('El permiso no puede ser null')
            return False


    # método que permite crear una lista de colegios
    @staticmethod
    def listaUsuarios():
        bd = BD()
        condicion = None
        ap = bd.select('*',Usuario.tabla,condicion)
        #creo una lista vacia (que se usara para devolver el resultado)
        lista = []
        #cada tupla en la lista obtenida en la consulta se usa para crear una instancia de apadrinamiento y se agregan a la lista vacia
        for col in ap:
            id_usario = col[0]
            nombre = col[1]
            clave = col[2]
            rol = col[3]
            permiso = col[4]
            user = Colegio(id_usuario, nombre, clave, rol, permiso)
            lista.append(user)
        return lista


    # método que retorna una representación de la instancia de la clase
    def __repr__(self):
        cadena = ''
        if self.id_usuario != None: 
            cadena += 'Usuario '+ str(self.id_usuario) + ' - '
        if self.nombre != None: 
            cadena += 'Nombre ' + self.nombre + ' - '
        if self.clave != None: 
            cadena += 'Clave ' + self.clave + ' - '
        if self.rol != None:
            cadena += 'Rol ' + str(self.rol.getRol()) + ' - '
        if self.permiso != None:
            cadena += 'Permiso ' + str(self.permiso.getPermiso())
        if cadena == '':
            cadena = 'Proyecto vacío - ' 
        
        return cadena[:-3]

if __name__ == '__main__':
    