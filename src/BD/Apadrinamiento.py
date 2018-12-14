import sys
from BD import BD


class Apadrinamiento:

    def __init__(self, id_apadrinamiento: int = None, joven: int = None, socio: int = None, agente: int = None, fecha_de_inicio: str = None, fecha_de_baja: str = None, enBase = False):
        self.tabla = 'apadrinamiento'
        #si todas las variables son nulas crea una instancia nula del objeto (sirve para crear listas de tuplas de la base de datos)
        if (id_apadrinamiento == None and joven == None and socio == None and agente == None and fecha_de_inicio == None and fecha_de_baja == None):
            self.id_apadrinamiento = None
            self.joven = None
            self.socio = None
            self.agente = None
            self.fecha_de_inicio = None
            self.fecha_de_baja = None
        else:
            #si la variable enBase es True se indica que el apadrinamiento se encuentra en la tabla, por lo que no hace falta comprobarlo
            #vale principalmente para la creación de listas, que se hace luego de hacer una consulta en la base de datos y con las tuplas
            #obtenidas se crean instancias de la clase
            if enBase == False:
                #me conecto a la base de datos
                bd = BD() 
                #consulto si los valores estan en la tabla
                condicion = 'joven = ' + str(joven) + ' and socio = ' + str(socio)
                ap = bd.select('*',self.tabla,condicion)

                #inserto los valores en la tabla si no existen
                if ap == None or ap == []:
                    print ('Inserto el apadrinamiento en la tabla')
                    if fecha_de_baja == None:
                        fecha_de_baja = 'null'
                    valores = [id_apadrinamiento, joven, socio, agente, fecha_de_inicio, fecha_de_baja]
                    bd.insert(valores, self.tabla)
            #inicializo las variables de la instancia
            self.id_apadrinamiento = id_apadrinamiento
            self.joven = joven
            self.socio = socio
            self.agente = agente
            self.fecha_de_inicio = fecha_de_inicio
            self.fecha_de_baja = fecha_de_baja

    
    #serie de comandos que devuelven los valores de los campos de la instancia
    def getIdApadrinamiento(self):
        return self.id_apadrinamiento

    def getJoven(self):
        return self.joven

    def getSocio(self):
        return self.socio

    def getAgente(self):
        return self.agente

    def getFechaDeInicio(self):
        return self.fecha_de_inicio

    def getFechaDeBaja(self):
        return self.fecha_de_baja

    #se borra la instancia actual de apadrinamiento de la base de datos y la instancia se convierte en nula
    def delete(self):
        bd = BD()   
        condicion = 'joven = ' + str(self.joven) + ' and socio = ' + str(self.socio)
        bd.delete(self.tabla,condicion)
        self.id_apadrinamiento = None
        self.joven = None
        self.socio = None
        self.agente = None
        self.fecha_de_inicio = None
        self.fecha_de_baja = None

    def setIdApadrinamiento(self, id_apadrinamiento: int = None):
        #comprobación de que el valor no sea nulo
        if id_apadrinamiento != None:
            bd = BD()
            condicion = 'id_apadrinamiento = ' + str(id_apadrinamiento)
            resultado = '*'
            ap = bd.selectEscalar(resultado,self.tabla,condicion)
            #compruebo que el valor no existe en la tabla para no incumplir la unicidad del atributo
            if ap == None or ap == []:
                condicion = 'joven = ' + str(self.joven) + ' and socio = ' + str(self.socio)
                setter = 'id_apadrinamiento = ' + str(id_apadrinamiento)
                bd.update(self.tabla,setter,condicion)
                self.id_apadrinamiento = id_apadrinamiento
            else:
                print ('id_apadrinamiento existente')
        else:
            print ('id_apadrinamiento no puede ser null')

    def setJoven(self, joven: int = None):
        #comprobación de que el valor no sea nulo
        if joven != None:
            bd = BD()
            condicion = 'id_joven = ' + str(joven)
            resultado = '*'
            ap = bd.selectEscalar(resultado,' joven ',condicion)
            #compruebo que el valor existe en su tabla, por ser en apadrinamiento una clave foranea
            if ap != None:
                condicion = 'joven = ' + str(joven) + ' and socio = ' + str(self.socio)
                resultado = '*'
                ap = bd.selectEscalar(resultado,self.tabla,condicion)
                #compruebo que la combinacion de joven y socio no se encuentre en la tabla de apadrinamientos al ser ambas la clave primaria
                if ap == None or ap == []:
                    condicion = 'joven = ' + str(self.joven) + ' and socio = ' + str(self.socio)
                    setter = 'joven = ' + str(joven)
                    bd.update(self.tabla,setter,condicion)
                    self.joven = joven       
                else:
                    print ('apadrinamiento existente')
            else:
                print ('joven no existente')
        else:
            print ('joven no puede ser null') 

    def setSocio(self, socio: int = None):
        #comprobación de que el valor no sea nulo
        if socio != None:
            bd = BD()
            condicion = 'usuario = ' + str(socio)
            resultado = '*'
            ap = bd.selectEscalar(resultado,' socio ',condicion)
            #compruebo que el valor existe en su tabla, por ser en apadrinamiento una clave foranea
            if ap != None:
                condicion = 'joven = ' + str(self.joven) + ' and socio = ' + str(socio)
                resultado = '*'
                ap = bd.selectEscalar(resultado,self.tabla,condicion)
                #compruebo que la combinacion de joven y socio no se encuentre en la tabla de apadrinamientos al ser ambas la clave primaria
                if ap == None or ap == []:
                    condicion = 'joven = ' + str(self.joven) + ' and socio = ' + str(self.socio)
                    setter = 'socio = ' + str(socio)
                    bd.update(self.tabla,setter,condicion)
                    self.socio = socio
                else:
                    print ('apadrinamiento existente')
            else:
                print ('socio no existente')
        else:
            print ('socio no puede ser null')

    def setAgente(self, agente: int = None):
        #comprobación de que el valor no sea nulo
        if agente != None:
            bd = BD()
            condicion = 'usuario = ' + str(agente)
            resultado = '*'
            ap = bd.selectEscalar(resultado,' voluntario ',condicion)
            #compruebo que el valor existe en su tabla, por ser en apadrinamiento una clave foranea
            if ap != None:
                condicion = 'joven = ' + str(self.joven) + ' and socio = ' + str(self.socio)
                setter = 'agente = ' + str(agente)
                bd.update(self.tabla,setter,condicion)
                self.agente = agente
            else:
                 print ('agente no existente')
        else:
            print ('agente no puede ser null')
           

    def setFechaDeInicio(self, fecha_de_inicio: str = None):
        #comprobación de que el valor no sea nulo
        if fecha_de_inicio != None:
            bd = BD()
            condicion = 'joven = ' + str(self.joven) + ' and socio = ' + str(self.socio)
            setter = 'fecha_de_inicio = ' + str(fecha_de_inicio)
            bd.update(self.tabla,setter,condicion)
            self.fecha_de_inicio = fecha_de_inicio
        else:
            print ('fecha de inicio no puede ser null')

    def setFechaDeBaja(self, fecha_de_baja: str = None):
        bd = BD()
        condicion = 'joven = ' + str(self.joven) + ' and socio = ' + str(self.socio)
        setter = 'fecha_de_baja = ' + str(fecha_de_baja)
        bd.update(self.tabla,setter,condicion)
        self.fecha_de_baja = fecha_de_baja

    def listaApadrinamientos(self, socio: int = None, agente: int = None):
        bd = BD()
        #si agente y socio son nulos la busqueda es total
        if socio == None and agente == None:
            condicion = None
        #busqueda por socio y agente
        elif socio != None and agente != None:
            condicion = ' socio = ' + str(socio) + ' agente = ' + str(agente)
        #busqueda pro socio
        elif socio != None:
            condicion = ' socio = ' + str(socio)
        #busqueda por agente
        elif agente != None:
            condicion = ' agente = ' + str(agente)
        ap = bd.select('*',self.tabla,condicion)
        #creo una lista vacia (que se usara para devolver el resultado)
        lista = []
        #cada tupla en la lista obtenida en la consulta se usa para crear una instancia de apadrinamiento y se agregan a la lista vacia
        for apad in ap:
            id_apadrinamiento = apad[0]
            joven = apad[1]
            socio = apad[2]
            agente = apad[3]
            fecha_de_inicio = apad[4]
            fecha_de_baja = apad[5]
            if fecha_de_baja == None:
                apadrina = Apadrinamiento(id_apadrinamiento, joven, socio, agente, fecha_de_inicio.strftime('%Y-%m-%d'), None, True)
            else:
                apadrina = Apadrinamiento(id_apadrinamiento, joven, socio, agente, fecha_de_inicio.strftime('%Y-%m-%d'), fecha_de_baja.strftime('%Y-%m-%d'), True)
            lista.append(apadrina)
        return lista

    def toString(self):
        cadena = ''
        if self.id_apadrinamiento != None: 
            cadena += 'Apadrinamiento '+ str(self.id_apadrinamiento) + ' - '
        if self.joven != None: 
            cadena += 'Joven ' + str(self.joven) + ' - '
        if self.socio != None: 
            cadena += 'Socio ' + str(self.socio) + ' - '
        if self.agente != None:
            cadena += 'Agente ' + str(self.agente) + ' - '
        if self.fecha_de_inicio != None:
            cadena += 'Fecha de inicio ' + self.fecha_de_inicio + ' - '
        if self.fecha_de_baja != None:
            cadena += 'Fecha de baja ' + self.fecha_de_baja
        else:
            cadena += 'Sin fecha de baja'
        if cadena == '':
            cadena = 'Apadrinamiento vacío' 
        
        print(cadena)

if __name__ == '__main__':
    
    #print ('Apadrinamiento 1, joven 1, socio 1, agente 2, inicio 2017-12-12, fin 2019-01-02')
    #ap = Apadrinamiento(1,1,1,2,'2017-12-12','2019-01-02')
    #ap.toString()
    #print ('Imprimo la lista de apadrinamientos')
    #print (ap.listaApadrinamientos())
    
    #print ('Modifico el id del apadrinamiento de 1 a 2')
    #ap.setIdApadrinamiento(2)
    #ap.toString()
    #print ('Imprimo la lista de apadrinamientos')
    #print (ap.listaApadrinamientos())
    
    #print ('Borro la entrada')
    #ap.delete()
    #print ('Datos de la instancia luego del borrado: ')
    #ap.toString()

    ap = Apadrinamiento()
    lista = ap.listaApadrinamientos()
    ap1 = lista[0]
    ap1.toString()
    #ap1.delete()
    #ap1.toString()
