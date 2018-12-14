import sys
from BD import BD


class Colonia:

    def __init__(self, id_colonia: int = None, nombre: str = None, numero_de_habitantes: int = None, descripcion: str = None, enBase = False):
        self.tabla = 'colonia'
        #si todas las variables son nulas crea una instancia nula del objeto (sirve para crear listas de tuplas de la base de datos)
        if (id_colonia == None and nombre == None and numero_de_habitantes == None and descripcion == None):
            self.id_colonia = None
            self.nombre = None
            self.numero_de_habitantes = None
            self.descripcion = None
        else:
            #si la variable enBase es True se indica que el apadrinamiento se encuentra en la tabla, por lo que no hace falta comprobarlo
            #vale principalmente para la creación de listas, que se hace luego de hacer una consulta en la base de datos y con las tuplas
            #obtenidas se crean instancias de la clase
            if enBase == False:
                #me conecto a la base de datos
                bd = BD() 
                #consulto si los valores estan en la tabla
                condicion = 'id_colonia = ' + str(id_colonia)
                ap = bd.select('*',self.tabla,condicion)

                #inserto los valores en la tabla si no existen
                if ap == None or ap == []:
                    print ('Inserto la colonia en la tabla')
                    if descripcion == None:
                        descripcion = 'null'
                    valores = [id_colonia, nombre, numero_de_habitantes, descripcion]
                    bd.insert(valores, self.tabla)
            #inicializo las variables de la instancia
            self.id_colonia = id_colonia
            self.nombre = nombre
            self.numero_de_habitantes = numero_de_habitantes
            self.descripcion = descripcion

    
    #serie de comandos que devuelven los valores de los campos de la instancia
    def getIdColonia(self):
        return self.id_colonia

    def getNombre(self):
        return self.Nombre

    def getNumeroDeHabitaciones(self):
        return self.numero_de_habitantes

    def getDescripcion(self):
        return self.descripcion

    #se borra la instancia actual de apadrinamiento de la base de datos y la instancia se convierte en nula
    def delete(self):
        bd = BD()   
        condicion = 'id_colonia = ' + str(id_colonia)
        bd.delete(self.tabla,condicion)
        self.id_colonia = None
        self.nombre = None
        self.numero_de_habitantes = None
        self.descripcion = None

    def setIdColonia(self, id_colonia: int = None):
        #comprobación de que el valor no sea nulo
        if id_colonia != None:
            bd = BD()
            condicion = 'id_colonia = ' + str(id_colonia)
            resultado = '*'
            ap = bd.selectEscalar(resultado,self.tabla,condicion)
            #compruebo que el valor no existe en la tabla para no incumplir la unicidad del atributo
            if ap == None or ap == []:
                condicion = 'id_colonia = ' + str(self.id_colonia)
                setter = 'id_colonia = ' + str(id_colonia)
                bd.update(self.tabla,setter,condicion)
                self.id_colonia = id_colonia
            else:
                print ('id_colonia existente')
        else:
            print ('id_colonia no puede ser null')

    def setNombre(self, nombre: str = None):
        #comprobación de que el valor no sea nulo
        if nombre != None:
            bd = BD()
            condicion = 'id_colonia = ' + str(id_colonia)
            setter = 'nombre = ' + str(nombre)
            bd.update(self.tabla,setter,condicion)
            self.nombre = nombre       
        else:
            print ('nombre no puede ser null') 

    def setNumeroDeHabitantes(self, numero_de_habitantes: int = None):
        #comprobación de que el valor no sea nulo
        if numero_de_habitantes != None:
            bd = BD()
            condicion = 'id_colonia = ' + str(id_colonia)
            setter = 'numero_de_habitantes = ' + str(numero_de_habitantes)
            bd.update(self.tabla,setter,condicion)
            self.numero_de_habitantes = numero_de_habitantes       
        else:
            print ('el numero de habitantes no puede ser null') 

    def setDescripcion(self, descripcion: str = None):
        bd = BD()
        condicion = 'id_colonia = ' + str(id_colonia)
        setter = 'descripcion = ' + str(descripcion)
        bd.update(self.tabla,setter,condicion)
        self.descripcion = descripcion

    def listaProyectos(self):
        bd = BD()
        condicion = None
        ap = bd.select('*',self.tabla,condicion)
        #creo una lista vacia (que se usara para devolver el resultado)
        lista = []
        #cada tupla en la lista obtenida en la consulta se usa para crear una instancia de apadrinamiento y se agregan a la lista vacia
        for apad in ap:
            id_colonia = apad[0]
            nombre = apad[1]
            numero_de_habitantes = apad[2]
            descripcion = apad[3]
            coloniza = Colonia(id_colonia, nombre, numero_de_habitantes, descripcion, True)
            lista.append(coloniza)
        return lista

    def toString(self):
        cadena = ''
        if self.id_colonia != None: 
            cadena += 'Colonia '+ str(self.id_colonia) + ' - '
        if self.nombre != None: 
            cadena += 'Nombre ' + self.nombre + ' - '
        if self.numero_de_habitantes != None: 
            cadena += 'Número de habitantes ' + str(self.numero_de_habitantes) + ' - '
        if self.descripcion != None:
            cadena += 'Descripción ' + self.descripcion 
        if cadena == '':
            cadena = 'Proyecto vacío' 
        
        print(cadena)

if __name__ == '__main__':
    col = Colonia()
    lista = col.listaProyectos()
    if lista == []:
        print ('Tabla vacía')
    for c in lista:
        c.toString()