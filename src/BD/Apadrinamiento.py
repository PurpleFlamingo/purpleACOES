import sys
from BD.BD import BD
from BD.Joven import Joven
from BD.Voluntario import Voluntario
from BD.Socio import Socio
from datetime import datetime


class Apadrinamiento:


    tabla = 'apadrinamiento'

    def __init__(self, id_apadrinamiento: int = None, joven: int = None, socio: int = None, agente: int = None, fecha_de_inicio: str = None, fecha_de_baja: str = None):
            self.id_apadrinamiento = id_apadrinamiento
            self.joven = joven
            self.socio = socio
            self.agente = agente
            self.fecha_de_inicio = fecha_de_inicio
            self.fecha_de_baja = fecha_de_baja

    @staticmethod
    def newApadrinamiento(id_apadrinamiento: int, joven: int, socio: int, agente: int, fecha_de_inicio, fecha_de_baja = None):
            if id_apadrinamiento == None or joven == None or socio == None or agente == None or fecha_de_inicio == None:
                print('Error: los datos del apadrinamiento (excepto la fecha de baja) no pueden ser nulos')
                return None
            if fecha_de_baja == None:
                fecha_de_baja = 'null'

            #compruebo que la combinacion de joven y socio no se encuentra en la tabla (por ser la clave primaria)
            condicion = 'joven = ' + str(joven) + ' and socio = ' + str(socio)
            ap = Apadrinamiento.estaEnLaTabla(Apadrinamiento.tabla,condicion)
            if ap:
                print('Apadrinamiento ya existente')
                return None
            #compruebo que las claves foraneas existen en sus tablas de origen (joven, socio, agente)
            condicion = ' id_joven = ' + str(joven)
            ap = Apadrinamiento.estaEnLaTabla(' joven ',condicion)
            if not ap:
                print('Joven no existente')
                return None
            condicion = ' usuario = ' + str(socio)
            ap = Apadrinamiento.estaEnLaTabla(' socio ',condicion)
            if not ap:
                print('Socio no existente')
                return None
            condicion = ' usuario = ' + str(agente)
            ap = Apadrinamiento.estaEnLaTabla(' voluntario ',condicion)
            if not ap:
                print('Agente no existente')
                return None

            bd = BD() 
            #consulto si los valores estan en la tabla
            condicion = 'id_apadrinamiento = ' + str(id_apadrinamiento)
            ap = bd.select('*',Apadrinamiento.tabla,condicion)

            #inserto los valores en la tabla si no existen
            if not ap:
                valores = [id_apadrinamiento, joven, socio, agente, fecha_de_inicio, fecha_de_baja]
                bd.insert(valores, Apadrinamiento.tabla)
                #inicializo las variables de la instancia
                fecha_de_inicio = datetime.strptime(fecha_de_inicio, '%Y-%m-%d')
                fecha_de_baja = datetime.strptime(fecha_de_baja, '%Y-%m-%d')

                newAp = Apadrinamiento(id_apadrinamiento, Joven.getJoven(joven), Socio.getSocio(socio), Voluntario.getVoluntario(agente), fecha_de_inicio, fecha_de_baja)
                print(newAp)
                return newAp
            else:
                print('Error: La id {} ya esta en uso',format(id_apadrinamiento))
                return None

    #metodo que comprueba si la condicion pasada como parametro devuelve tuplas en la query o si esta devuele un nulo 
    #el resultado es verdadero si se devuelve una tupla (o una lista de tuplas) y falso si no se encuentran tuplas
    @staticmethod
    def estaEnLaTabla(tabla: str, condicion: str):
        bd = BD()
        resultado = '*'
        ap = bd.selectEscalar(resultado,tabla,condicion)
        return ap != None
        
    #dado un valor de la clave se lo busca en la tabla y se crea una instancia de la clase con esos valores y en caso de no existir se 
    # devuelve el valor nulo (None) 
    @staticmethod
    def getApadrinamiento(id_apadrinamiento: int):
        bd = BD()
        condicion = 'id_apadrinamiento = ' + str(id_apadrinamiento)
        resultado = '*'
        ap = bd.selectEscalar(resultado,Apadrinamiento.tabla,condicion)
        if not ap:
            print('Apadrinamiento no existente')
            return None
        else:
            id_apdrinamiento = id_apadrinamiento
            joven = Joven.getJoven(ap[1]) if ap[1] != None else None
            socio = Socio.getSocio(ap[2]) if ap[2] != None else None
            agente = Voluntario.getVoluntario(ap[3]) if ap[3] != None else None
            fecha_de_inicio = ap[4]
            fecha_de_baja = ap[5]
            newAp = Apadrinamiento(id_apadrinamiento, joven, socio, agente, fecha_de_inicio, fecha_de_baja)
            return newAp

    #serie de comandos que devuelven los valores de los campos de la instancia
    def getIdApadrinamiento(self):
        return self.id_apadrinamiento

    def getJoven(self):
        return self.joven
    
    def getJovenID(self):
        return self.joven.getIdJoven()

    def getSocio(self):
        return self.socio

    def getSocioId(self):
        return self.socio.getUsuario()

    def getAgente(self):
        return self.agente

    def getAgenteId(self):
        return self.agente.getUsuario()

    def getFechaDeInicio(self):
        return self.fecha_de_inicio

    def getFechaDeBaja(self):
        return self.fecha_de_baja

    #se borra la instancia actual de apadrinamiento de la base de datos y la instancia se convierte en nula
    def delete(self):
        bd = BD()   
        condicion = 'joven = ' + str(self.joven) + ' and socio = ' + str(self.socio)
        bd.delete(Apadrinamiento.tabla,condicion)
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
            ap = bd.selectEscalar(resultado,Apadrinamiento.tabla,condicion)
            #compruebo que el valor no existe en la tabla para no incumplir la unicidad del atributo
            if ap == None or ap == []:
                condicion = 'joven = ' + str(self.joven) + ' and socio = ' + str(self.socio)
                setter = 'id_apadrinamiento = ' + str(id_apadrinamiento)
                bd.update(Apadrinamiento.tabla,setter,condicion)
                self.id_apadrinamiento = id_apadrinamiento
            else:
                print ('id_apadrinamiento existente')
                return False
        else:
            print ('id_apadrinamiento no puede ser null')
            return False

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
                ap = bd.selectEscalar(resultado,Apadrinamiento.tabla,condicion)
                #compruebo que la combinacion de joven y socio no se encuentre en la tabla de apadrinamientos al ser ambas la clave primaria
                if ap == None or ap == []:
                    condicion = 'joven = ' + str(self.joven) + ' and socio = ' + str(self.socio)
                    setter = 'joven = ' + str(joven)
                    bd.update(Apadrinamiento.tabla,setter,condicion)
                    self.joven = joven       
                else:
                    print ('apadrinamiento existente')
                    return False
            else:
                print ('joven no existente')
                return False
        else:
            print ('joven no puede ser null') 
            return False

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
                ap = bd.selectEscalar(resultado,Apadrinamiento.tabla,condicion)
                #compruebo que la combinacion de joven y socio no se encuentre en la tabla de apadrinamientos al ser ambas la clave primaria
                if ap == None or ap == []:
                    condicion = 'joven = ' + str(self.joven) + ' and socio = ' + str(self.socio)
                    setter = 'socio = ' + str(socio)
                    bd.update(Apadrinamiento.tabla,setter,condicion)
                    self.socio = socio
                else:
                    print ('apadrinamiento existente')
                    return False
            else:
                print ('socio no existente')
                return False
        else:
            print ('socio no puede ser null')
            return False

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
                bd.update(Apadrinamiento.tabla,setter,condicion)
                self.agente = agente
            else:
                 print ('agente no existente')
                 return False
        else:
            print ('agente no puede ser null')
            return False
           

    def setFechaDeInicio(self, fecha_de_inicio = None):
        #comprobación de que el valor no sea nulo
        if fecha_de_inicio != None:
            bd = BD()
            condicion = 'joven = ' + str(self.joven) + ' and socio = ' + str(self.socio)
            setter = 'fecha_de_inicio = ' + str(fecha_de_inicio)
            bd.update(Apadrinamiento.tabla,setter,condicion)
            self.fecha_de_inicio = fecha_de_inicio
        else:
            print ('fecha de inicio no puede ser null')
            return False

    def setFechaDeBaja(self, fecha_de_baja = None):
        bd = BD()
        condicion = 'joven = ' + str(self.joven) + ' and socio = ' + str(self.socio)
        setter = 'fecha_de_baja = ' + str(fecha_de_baja)
        bd.update(Apadrinamiento.tabla,setter,condicion)
        self.fecha_de_baja = fecha_de_baja

    # método que permite crear una lista de proyectos y que permite filtrarlos por tipo
    @staticmethod
    def listaApadrinamientos(socio: int = None, agente: int = None):
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
        ap = bd.select('*',Apadrinamiento.tabla,condicion)
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
                apadrina = Apadrinamiento(id_apadrinamiento, Joven.getJoven(joven), Socio.getSocio(socio), Voluntario.getVoluntario(agente), fecha_de_inicio, None)
            else:
                apadrina = Apadrinamiento(id_apadrinamiento, Joven.getJoven(joven), Socio.getSocio(socio), Voluntario.getVoluntario(agente), fecha_de_inicio, fecha_de_baja)
            lista.append(apadrina)
        return lista
        
    # método que retorna una representación de la instancia de la clase
    def __repr__(self):
        cadena = ''
        if self.id_apadrinamiento != None: 
            cadena += 'Apadrinamiento '+ str(self.id_apadrinamiento) + ' - '
        if self.joven != None: 
            cadena += 'Joven ' + str(self.joven) + ' - '
        if self.socio != None: 
            cadena += 'Socio ' + str(self.socio.getUsuario()) + ' - '
        if self.agente != None:
            cadena += 'Agente ' + str(self.agente.getUsuario()) + ' - '
        if self.fecha_de_inicio != None:
            cadena += 'Fecha de inicio ' + self.fecha_de_inicio.strftime('%Y-%m-%d') + ' - '
        if self.fecha_de_baja != None:
            cadena += 'Fecha de baja ' + self.fecha_de_baja.strftime('%Y-%m-%d') + ' - '
        else:
            cadena += 'Sin fecha de baja - '
        if cadena == '':
            cadena = 'Apadrinamiento vacío - ' 

        return cadena[:-3]


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
