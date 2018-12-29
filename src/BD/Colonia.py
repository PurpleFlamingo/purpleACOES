import sys
from BD.BD import BD


class Colonia:

    tabla = 'colonia'

    def __init__(self, id_colonia: int = None, nombre: str = None, numero_de_habitantes: int = None, descripcion: str = None):
            self.id_colonia = id_colonia
            self.nombre = nombre
            self.numero_de_habitantes = numero_de_habitantes
            self.descripcion = descripcion

    @staticmethod
    def newColonia(self, id_colonia: int, nombre: str, numero_de_habitantes: int, descripcion: str = None):
            if id_colonia == None or nombre == None or numero_de_habitantes == None:
                print('Error: la identificación o el nombre del proyecto o el numero de habitantes no pueden ser nulos')
                return None
            if descripcion == None:
                descripcion = 'null'

            bd = BD() 
            #consulto si los valores estan en la tabla
            condicion = 'id_colonia = ' + str(id_colonia)
            ap = bd.select('*',Colonia.tabla,condicion)

            #inserto los valores en la tabla si no existen
            if not ap:
                valores = [id_colonia, nombre, numero_de_habitantes, descripcion]
                bd.insert(valores, Proyecto.tabla)
                #inicializo las variables de la instancia
                newCol = Colonia(id_colonia, nombre, numero_de_habitantes, descripcion)
                print(newCol)
                return newCol
            else:
                print('Error: La id {} ya esta en uso',format(id_colonia))
                return None
               
    #dado un valor de la clave se lo busca en la tabla y se crea una instancia de la clase con esos valores y en caso de no existir se 
    # devuelve el valor nulo (None) 
    @staticmethod
    def getColonia(id_colonia):
        bd = BD()
        condicion = 'id_colonia = ' + str(id_colonia)
        resultado = '*'
        ap = bd.selectEscalar(resultado,Colonia.tabla,condicion)
        if not ap:
            print('Colonia no existente')
            return None
        else:
            id_colonia = id_colonia
            nombre = ap[1]
            numero_de_habitantes = ap[2]
            descripcion = ap[3]

    #serie de comandos que devuelven los valores de los campos de la instancia
    def getIdColonia(self):
        return self.id_colonia

    def getNombre(self):
        return self.Nombre

    def getNumeroDeHabitaciones(self):
        return self.numero_de_habitantes

    def getDescripcion(self):
        return self.descripcion

    #se borra la instancia actual de colonia de la base de datos y la instancia se convierte en nula
    def delete(self):
        bd = BD()   
        condicion = 'id_colonia = ' + str(self.id_colonia)
        bd.delete(Colonia.tabla,condicion)
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
            ap = bd.selectEscalar(resultado,Colonia.tabla,condicion)
            #compruebo que el valor no existe en la tabla para no incumplir la unicidad del atributo
            if ap == None or ap == []:
                condicion = 'id_colonia = ' + str(self.id_colonia)
                setter = 'id_colonia = ' + str(id_colonia)
                bd.update(Colonia.tabla,setter,condicion)
                self.id_colonia = id_colonia
            else:
                print ('id_colonia existente')
                return False
        else:
            print ('id_colonia no puede ser null')
            return False

    def setNombre(self, nombre: str = None):
        #comprobación de que el valor no sea nulo
        if nombre != None:
            bd = BD()
            condicion = 'id_colonia = ' + str(id_colonia)
            setter = 'nombre = ' + str(nombre)
            bd.update(Colonia.tabla,setter,condicion)
            self.nombre = nombre       
        else:
            print ('nombre no puede ser null') 
            return False

    def setNumeroDeHabitantes(self, numero_de_habitantes: int = None):
        #comprobación de que el valor no sea nulo
        if numero_de_habitantes != None:
            bd = BD()
            condicion = 'id_colonia = ' + str(id_colonia)
            setter = 'numero_de_habitantes = ' + str(numero_de_habitantes)
            bd.update(Colonia.tabla,setter,condicion)
            self.numero_de_habitantes = numero_de_habitantes       
        else:
            print ('el numero de habitantes no puede ser null') 
            return False

    def setDescripcion(self, descripcion: str = None):
        bd = BD()
        condicion = 'id_colonia = ' + str(id_colonia)
        setter = 'descripcion = ' + str(descripcion)
        bd.update(Colonia.tabla,setter,condicion)
        self.descripcion = descripcion


    # método que permite crear una lista de colonias
    @staticmethod
    def listaColonias():
        bd = BD()
        condicion = None
        ap = bd.select('*',Proyecto.tabla,condicion)
        #creo una lista vacia (que se usara para devolver el resultado)
        lista = []
        #cada tupla en la lista obtenida en la consulta se usa para crear una instancia de apadrinamiento y se agregan a la lista vacia
        for col in ap:
            id_colonia = col[0]
            nombre = col[1]
            numero_de_habitantes = col[2]
            descripcion = col[3]
            coloniza = Colonia(id_colonia, nombre, numero_de_habitantes, descripcion)
            lista.append(coloniza)
        return lista


    # método que retorna una representación de la instancia de la clase
    def __repr__(self):
        cadena = ''
        if self.id_colonia != None: 
            cadena += 'Colonia '+ str(self.id_colonia) + ' - '
        if self.nombre != None: 
            cadena += 'Nombre ' + self.nombre + ' - '
        if self.numero_de_habitantes != None: 
            cadena += 'Número de habitantes ' + str(self.numero_de_habitantes) + ' - '
        if self.descripcion != None:
            cadena += 'Descripción ' + self.descripcion + ' - '
        if cadena == '':
            cadena = 'Proyecto vacío - ' 
        
        return cadena[:-3]

if __name__ == '__main__':
   