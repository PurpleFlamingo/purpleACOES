import sys
from BD import BD


class Proyecto:

    def __init__(self, id_proyecto: int = None, nombre: str = None, requisitos_participacion: str = None, descripcion: str = None, tipo: str = None, enBase = False):
        self.tabla = 'proyecto'
        #si todas las variables son nulas crea una instancia nula del objeto (sirve para crear listas de tuplas de la base de datos)
        if (id_proyecto == None and nombre == None and requisitos_participacion == None and descripcion == None and tipo == None):
            self.id_proyecto = None
            self.nombre = None
            self.requisitos_participacion = None
            self.descripcion = None
            self.tipo = None
        else:
            #si la variable enBase es True se indica que el apadrinamiento se encuentra en la tabla, por lo que no hace falta comprobarlo
            #vale principalmente para la creación de listas, que se hace luego de hacer una consulta en la base de datos y con las tuplas
            #obtenidas se crean instancias de la clase
            if enBase == False:
                #me conecto a la base de datos
                bd = BD() 
                #consulto si los valores estan en la tabla
                condicion = 'id_proyecto = ' + str(id_proyecto)
                ap = bd.select('*',self.tabla,condicion)

                #inserto los valores en la tabla si no existen
                if ap == None or ap == []:
                    print ('Inserto el proyecto en la tabla')
                    if requisitos_participacion == None:
                        requisitos_participacion = 'null'
                    if descripcion == None:
                        descripcion = 'null'
                    if tipo == None:
                        tipo = 'null'
                    valores = [id_proyecto, nombre, requisitos_participacion, descripcion, tipo]
                    bd.insert(valores, self.tabla)
            #inicializo las variables de la instancia
            self.id_proyecto = id_proyecto
            self.nombre = nombre
            self.requisitos_participacion = requisitos_participacion
            self.descripcion = descripcion
            self.tipo = tipo

    
    #serie de comandos que devuelven los valores de los campos de la instancia
    def getIdProyecto(self):
        return self.id_proyecto

    def getNombre(self):
        return self.Nombre

    def getRequisitosDeParticipacion(self):
        return self.requisitos_participacion

    def getDescripcion(self):
        return self.descripcion

    def getTipo(self):
        return self.tipo


    #se borra la instancia actual de apadrinamiento de la base de datos y la instancia se convierte en nula
    def delete(self):
        bd = BD()   
        condicion = 'id_proyecto = ' + str(self.id_proyecto)
        bd.delete(self.tabla,condicion)
        self.id_proyecto = None
        self.nombre = None
        self.requisitos_participacion = None
        self.descripcion = None
        self.tipo = None

    def setIdProyecto(self, id_proyecto: int = None):
        #comprobación de que el valor no sea nulo
        if id_proyecto != None:
            bd = BD()
            condicion = 'id_proyecto = ' + str(id_proyecto)
            resultado = '*'
            ap = bd.selectEscalar(resultado,self.tabla,condicion)
            #compruebo que el valor no existe en la tabla para no incumplir la unicidad del atributo
            if ap == None or ap == []:
                condicion = 'id_proyecto = ' + str(self.id_proyecto)
                setter = 'id_proyecto = ' + str(id_proyecto)
                bd.update(self.tabla,setter,condicion)
                self.id_proyecto = id_proyecto
            else:
                print ('id_proyecto existente')
        else:
            print ('id_proyecto no puede ser null')

    def setNombre(self, nombre: str = None):
        #comprobación de que el valor no sea nulo
        if nombre != None:
            bd = BD()
            condicion = 'id_proyecto = ' + str(self.id_proyecto)
            setter = 'nombre = ' + str(nombre)
            bd.update(self.tabla,setter,condicion)
            self.nombre = nombre       
        else:
            print ('joven no puede ser null') 

    def setRequisitosDeParticipacion(self, requisitos_participacion: str = None):
        bd = BD()
        condicion = 'id_proyecto = ' + str(self.id_proyecto)
        setter = 'requisitos_participacion = ' + str(requisitos_participacion)
        bd.update(self.tabla,setter,condicion)
        self.requisitos_participacion = requisitos_participacion

    def setDescripcion(self, descripcion: str = None):
        bd = BD()
        condicion = 'id_proyecto = ' + str(self.id_proyecto)
        setter = 'descripcion = ' + str(descripcion)
        bd.update(self.tabla,setter,condicion)
        self.descripcion = descripcion

    def setTipo(self, tipo: str = None):
        bd = BD()
        condicion = 'id_proyecto = ' + str(self.id_proyecto)
        setter = 'tipo = ' + str(tipo)
        bd.update(self.tabla,setter,condicion)
        self.tipo = tipo

    def listaProyectos(self, tipo: str = None):
        bd = BD()
        #si tipo es nulo la busqueda es total
        if tipo == None:
            condicion = None
        #busqueda por tipo
        elif tipo != None:
            condicion = ' tipo = ' + tipo
        ap = bd.select('*',self.tabla,condicion)
        #creo una lista vacia (que se usara para devolver el resultado)
        lista = []
        #cada tupla en la lista obtenida en la consulta se usa para crear una instancia de apadrinamiento y se agregan a la lista vacia
        for apad in ap:
            id_proyecto = apad[0]
            nombre = apad[1]
            requisitos_participacion = apad[2]
            descripcion = apad[3]
            tipo = apad[4]
            proyecta = Proyecto(id_proyecto, nombre, requisitos_participacion, descripcion, tipo, True)
            lista.append(proyecta)
        return lista

    def toString(self):
        cadena = ''
        if self.id_proyecto != None: 
            cadena += 'Apadrinamiento '+ str(self.id_proyecto) + ' - '
        if self.nombre != None: 
            cadena += 'Nombre ' + self.nombre + ' - '
        if self.requisitos_participacion != None: 
            cadena += 'Requisitos de participación ' + self.requisitos_participacion + ' - '
        else:
            cadena += 'Sin requisitos de participación - '
        if self.descripcion != None:
            cadena += 'Descripción ' + self.decripcion + ' - '
        if self.tipo != None:
            cadena += 'Tipo ' + self.tipo
        if cadena == '':
            cadena = 'Proyecto vacío' 
        
        print(cadena)

if __name__ == '__main__':
    pr = Proyecto()
    lista = pr.listaProyectos()
    if lista == []:
        print ('Tabla vacía')
    for p in lista:
        p.toString()