import sys
from BD import BD


class Colegio:

    tabla = 'colegio'

    def __init__(self, id_colegio: int = None, asociado_ACOES: bool = None, nombre_colegio: str = None, colonia: int = None):
            self.id_colegio = id_colegio
            self.asociado_ACOES = asociado_ACOES
            self.nombre_colegio = nombre_colegio
            self.colonia = Colonia(colonia) if colonia != None else None

    @staticmethod
    def newColegio(self, id_colegio: int, asociado_ACOES: bool = None, nombre_colegio: str = None, colonia: int):
            if id_colegio == None or colonia == None:
                print('Error: la identificación del colegio o de la colonia no pueden ser nulos')
                return None
            if asociado_ACOES == None:
                asociado_ACOES = 'null'
            if nombre_colegio == None:
                nombre_colegio = 'null'

            bd = BD() 
            
            #Compruebo la existencia de la clave foranea en su tabla de origen
            condicion = 'id_colonia = ' + str(colonia)
            resultado = '*'
            ap = bd.selectEscalar(resultado,' colonia ',condicion)
            if not ap:
                print('Colonia no existente')
                return None
            
            #consulto si los valores estan en la tabla
            condicion = 'id_colegio = ' + str(id_colegio)
            ap = bd.select('*',Colegio.tabla,condicion)

            #inserto los valores en la tabla si no existen
            if not ap:
                valores = [id_colegio, asociado_ACOES, nombre_colegio, colonia]
                bd.insert(valores, Colegio.tabla)
                #inicializo las variables de la instancia
                newCol = Colegio(id_colegio, asociado_ACOES, nombre_colegio, colonia)
                print(newCol)
                return newCol
            else:
                print('Error: La id {} ya esta en uso',format(id_colegio))
                return None
               
    #dado un valor de la clave se lo busca en la tabla y se crea una instancia de la clase con esos valores y en caso de no existir se 
    # devuelve el valor nulo (None) 
    @staticmethod
    def getColegio(id_colegio):
        bd = BD()
        condicion = 'id_colegio = ' + str(id_colegio)
        resultado = '*'
        ap = bd.selectEscalar(resultado,Colegio.tabla,condicion)
        if not ap:
            print('Colegio no existente')
            return None
        else:
            id_colegio = id_colegio
            asociado_ACOES = ap[1]
            nombre_colegio = ap[2]
            colonia = Colonia(ap[3]) if ap[3] != None else None


    #serie de comandos que devuelven los valores de los campos de la instancia
    def getIdColegio(self):
        return self.id_colegio

    def getAsociadoDeACOES(self):
        return self.asociado_ACOES

    def getNombreDeColegio(self):
        return self.nombre_colegio

    def getColonia(self):
        return self.colonia

    def getColoniaId(self):
        return self.colonia.getIdColonia

    #se borra la instancia actual de apadrinamiento de la base de datos y la instancia se convierte en nula
    def delete(self):
        bd = BD()   
        condicion = 'id_colegio = ' + str(self.id_colegio)
        bd.delete(Colegio.tabla,condicion)
        self.id_colegio = None
        self.asociado_ACOES = None
        self.nombre_colegio = None
        self.colonia = None

    def setIdColegio(self, id_colegio: int = None):
        #comprobación de que el valor no sea nulo
        if id_colegio != None:
            bd = BD()
            condicion = 'id_colegio = ' + str(id_colegio)
            resultado = '*'
            ap = bd.selectEscalar(resultado,Colegio.tabla,condicion)
            #compruebo que el valor no existe en la tabla para no incumplir la unicidad del atributo
            if ap == None or ap == []:
                condicion = 'id_colegio = ' + str(self.id_colegio)
                setter = 'id_colegio = ' + str(id_colegio)
                bd.update(Colegio.tabla,setter,condicion)
                self.id_colegio = id_colegio
            else:
                print ('id_colegio existente')
                return False
        else:
            print ('id_colonia no puede ser null')
            return False

    def setAsociadoDeACOES(self, asociado_ACOES: bool = None):
        bd = BD()
        condicion = 'id_colegio = ' + str(id_colegio)
        if not asociado_ACOES:
            setter = 'asociado_ACOES = null'
        else:
            setter = 'asociado_ACOES = ' + str(asociado_ACOES)
        bd.update(Colegio.tabla,setter,condicion)
        self.asociado_ACOES = asociado_ACOES       

    def setNombreDeColegio(self, nombre_colegio: str = None):
        bd = BD()
        condicion = 'id_colonia = ' + str(id_colonia)
        if not nombre_colegio:
            setter = 'nombre_colegio = null'
        else:
            setter = 'nombre_colegio = ' + str(nombre_colegio)
        bd.update(Colegio.tabla,setter,condicion)
        self.nombre_colegio = nombre_colegio       

    def setColonia(self, colonia: str = None):
        if colonia:
            bd = BD()
            condicion = 'id_colonia = ' + str(colonia)
            ap = bd.selectEscalar('*',' colonia ',condicion)
            if ap:
                condicion = 'id_colegio = ' + str(id_colegio)
                setter = 'colonia = ' + str(colonia)
                bd.update(Colegio.tabla,setter,condicion)
                self.colonia = getColonia(colonia)
            else:
                print('Colonia no existente')
                return false
        else:
            print('La identificacion de la colonia no puede ser nula')
            return false


    # método que permite crear una lista de colegios
    @staticmethod
    def listaColegios():
        bd = BD()
        condicion = None
        ap = bd.select('*',Proyecto.tabla,condicion)
        #creo una lista vacia (que se usara para devolver el resultado)
        lista = []
        #cada tupla en la lista obtenida en la consulta se usa para crear una instancia de apadrinamiento y se agregan a la lista vacia
        for col in ap:
            id_colegio = col[0]
            asociado_ACOES = col[1]
            nombre_colegio = col[2]
            colonia = col[3]
            colegia = Colegio(id_colegio, asociado_ACOES, nombre_colegio, colonia)
            lista.append(colegia)
        return lista


    # método que retorna una representación de la instancia de la clase
    def __repr__(self):
        cadena = ''
        if self.id_colegio != None: 
            cadena += 'Colegio '+ str(self.id_colegio) + ' - '
        if self.asociado_ACOES != None: 
            cadena += 'Asociado de ACOES ' + str(self.asociado_ACOES) + ' - '
        if self.nombre_colegio != None: 
            cadena += 'Nombre de colegio ' + self.nombre_colegio + ' - '
        if self.colonia != None:
            cadena += 'Colonia ' + str(self.colonia.getIdColonia()) + ' - '
        if cadena == '':
            cadena = 'Proyecto vacío - ' 
        
        return cadena[:-3]

if __name__ == '__main__':
    