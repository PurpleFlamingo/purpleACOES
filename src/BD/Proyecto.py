import sys
from BD.BD import BD

class Proyecto:
    tabla = 'proyecto'
    def __init__(self, id_proyecto: int = None, nombre: str = None, requisitos_participacion: str = None, descripcion: str = None, tipo: str = None):
            self.id_proyecto = id_proyecto
            self.nombre = nombre
            self.requisitos_participacion = requisitos_participacion
            self.descripcion = descripcion
            self.tipo = tipo

    @staticmethod
    def newProyecto(id_proyecto: int, nombre: str, requisitos_participacion: str = None, descripcion: str = None, tipo: str = None):
            if id_proyecto == None or nombre == None:
                print('Error: la identificación o el nombre del proyecto no pueden ser nulos')
                return None
            if requisitos_participacion == None:
                requisitos_participacion = 'null'
            if descripcion == None:
                descripcion = 'null'
            if tipo == None:
                tipo = 'null'

            bd = BD() 
            #consulto si los valores estan en la tabla
            condicion = 'id_proyecto = ' + str(id_proyecto)
            ap = bd.select('*',Proyecto.tabla,condicion)

            #inserto los valores en la tabla si no existen
            if not ap:
                valores = [id_proyecto, nombre, requisitos_participacion, descripcion, tipo]
                bd.insert(valores, Proyecto.tabla)
                #inicializo las variables de la instancia
                newPr = Proyecto(id_proyecto, nombre, requisitos_participacion, descripcion, tipo)
                print(newPr)
                return newPr
            else:
                print('Error: La id {} ya esta en uso',format(id_proyecto))
                return None


    #dado un valor de la clave se lo busca en la tabla y se crea una instancia de la clase con esos valores y en caso de no existir se 
    # devuelve el valor nulo (None) 
    @staticmethod
    def getProyecto(id_proyecto):
        bd = BD()
        condicion = 'id_proyecto = ' + str(id_proyecto)
        resultado = '*'
        ap = bd.selectEscalar(resultado,Proyecto.tabla,condicion)
        if not ap:
            print('Proyecto no existente')
            return None
        else:
            id_proyecto = id_proyecto
            nombre = ap[1]
            requisitos_participacion = ap[2]
            descripcion = ap[3]
            tipo = ap[4]

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
        bd.delete(Proyecto.tabla,condicion)
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
            ap = bd.selectEscalar(resultado,Proyecto.tabla,condicion)
            #compruebo que el valor no existe en la tabla para no incumplir la unicidad del atributo
            if ap == None or ap == []:
                condicion = 'id_proyecto = ' + str(self.id_proyecto)
                setter = 'id_proyecto = ' + str(id_proyecto)
                bd.update(Proyecto.tabla,setter,condicion)
                self.id_proyecto = id_proyecto
            else:
                print ('id_proyecto existente')
                return False
        else:
            print ('id_proyecto no puede ser null')
            return False

    def setNombre(self, nombre: str = None):
        #comprobación de que el valor no sea nulo
        if nombre != None:
            bd = BD()
            condicion = 'id_proyecto = ' + str(self.id_proyecto)
            setter = 'nombre = ' + str(nombre)
            bd.update(Proyecto.tabla,setter,condicion)
            self.nombre = nombre       
        else:
            print ('nombre no puede ser null') 
            return False

    def setRequisitosDeParticipacion(self, requisitos_participacion: str = None):
        bd = BD()
        condicion = 'id_proyecto = ' + str(self.id_proyecto)
        setter = 'requisitos_participacion = ' + str(requisitos_participacion)
        bd.update(Proyecto.tabla,setter,condicion)
        self.requisitos_participacion = requisitos_participacion

    def setDescripcion(self, descripcion: str = None):
        bd = BD()
        condicion = 'id_proyecto = ' + str(self.id_proyecto)
        setter = 'descripcion = ' + str(descripcion)
        bd.update(Proyecto.tabla,setter,condicion)
        self.descripcion = descripcion

    def setTipo(self, tipo: str = None):
        bd = BD()
        condicion = 'id_proyecto = ' + str(self.id_proyecto)
        setter = 'tipo = ' + str(tipo)
        bd.update(Proyecto.tabla,setter,condicion)
        self.tipo = tipo

    # método que permite crear una lista de proyectos y que permite filtrarlos por tipo
    @staticmethod
    def listaProyectos(tipo: str = None):
        bd = BD()
        #si tipo es nulo la busqueda es total
        if tipo == None:
            condicion = None
        #busqueda por tipo
        elif tipo != None:
            condicion = ' tipo = ' + tipo
        ap = bd.select('*',Proyecto.tabla,condicion)
        #creo una lista vacia (que se usara para devolver el resultado)
        lista = []
        #cada tupla en la lista obtenida en la consulta se usa para crear una instancia de apadrinamiento y se agregan a la lista vacia
        for apad in ap:
            id_proyecto = apad[0]
            nombre = apad[1]
            requisitos_participacion = apad[2]
            descripcion = apad[3]
            tipo = apad[4]
            proyecta = Proyecto(id_proyecto, nombre, requisitos_participacion, descripcion, tipo)
            lista.append(proyecta)
        return lista

    # método que retorna una representación de la instancia de la clase
    def __repr__(self):
        cadena = ''
        if self.id_proyecto != None: 
            cadena += 'Proyecto '+ str(self.id_proyecto) + ' - '
        if self.nombre != None: 
            cadena += 'Nombre ' + self.nombre + ' - '
        if self.requisitos_participacion != None: 
            cadena += 'Requisitos de participación ' + self.requisitos_participacion + ' - '
        elif self.id_proyecto != None:
            cadena += 'Sin requisitos de participación - '
        if self.descripcion != None:
            cadena += 'Descripción ' + self.descripcion + ' - '
        if self.tipo != None:
            cadena += 'Tipo ' + self.tipo + ' - '
        if cadena == '':
            cadena = 'Proyecto vacío - ' 
        return cadena[:-3]

if __name__ == '__main__':
    lista = Proyecto.listaProyectos()
    if lista == []:
        print ('Tabla vacía')
    for p in lista:
        print(p)
    p = Proyecto.newProyecto(1,'Alfa')
    print('Proyecto 1: ')
    print(p)
    p = Proyecto.newProyecto(2,'Beta')
    print('Proyecto 2: ')
    print(p)
    p = None
    print('Proyecto p: ')
    print(p)
    print('Lista de la tabla')
    lista = Proyecto.listaProyectos()
    if lista == []:
        print ('Tabla vacía')
    for p in lista:
        print(p)
    print(Proyecto.getProyecto(1))
    print('Proyecto p despues de getProyecto(1): ')
    print(p)
