import sys
from BD.BD import BD


class Envios:

    tabla = 'envios'

    def __init__(self, id_envios: int = None, descripcion: str = None, enviado_por_socio: bool = None, recibido: bool = None, respuestaA: int = None, apadrinamiento: int = None):
            self.id_envios = id_envios
            self.descripcion = descripcion
            self.enviado_por_socio = enviado_por_socio
            self.recibido = recibido
            self.respuestaA = Envios(respuestaA) if respuestaA != None else None
            self.apadrinamiento = Apadrinamiento(apadrinamiento) if apadrinamiento != None else Noneº

    @staticmethod
    def newEnvios(self, id_envios: int, descripcion: str = None, enviado_por_socio: bool = None, recibido: bool = None, respuestaA: int = None, apadrinamiento: int):
            if id_envios == None or apadrinamiento == None:
                print('Error: la identificación del envio o del apadrinamientos no pueden ser nulos')
                return None
            if descripcion == None:
                descripcion = 'null'
            if enviado_por_socio == None:
                enviado_por_socio = 'null'
            if recibido == None:
                recibido = 'null'
            if respuestaA == None:
                respuestaA = 'null'

            bd = BD() 
            
            #compruebo que las claves foraneas existen en sus tablas de origen (respuestaA, apadrinamiento)
            if respuestaA != None:
                condicion = ' id_envios = ' + str(respuestaA)
                ap = estaEnLaTabla(Envios.tabla,condicion)
                if not ap:
                    print('Envio previo no existente')
                    return None
            condicion = ' id_apadrinamiento = ' + str(apadrinamiento)
            ap = estaEnLaTabla(' apadrinamiento ',str(apadrinamiento))
            if not ap:
                print('Apadrinamiento no existente')
                return None
            
            #consulto si los valores estan en la tabla
            condicion = 'id_envios = ' + str(id_envios)
            ap = bd.select('*',Envios.tabla,condicion)

            #inserto los valores en la tabla si no existen
            if not ap:
                valores = [id_envios, descripcion, enviado_por_socio, recibido, respuestaA, apadrinamiento]
                bd.insert(valores, Envios.tabla)
                #inicializo las variables de la instancia
                newE = Envios(id_envios, descripcion, enviado_por_socio, recibido, respuestaA, apadrinamiento)
                print(newE)
                return newE
            else:
                print('Error: La id {} ya esta en uso',format(id_envios))
                return None
               
    #dado un valor de la clave se lo busca en la tabla y se crea una instancia de la clase con esos valores y en caso de no existir se 
    # devuelve el valor nulo (None) 
    @staticmethod
    def getEnvios(id_envios):
        bd = BD()
        condicion = 'id_envios = ' + str(id_envios)
        resultado = '*'
        ap = bd.selectEscalar(resultado,Envios.tabla,condicion)
        if not ap:
            print('Envio no existente')
            return None
        else:
            id_envios = id_envios
            descripcion = ap[1]
            enviado_por_socio = ap[2]
            recibido = ap[3]
            respuestaA = Envios(ap[4]) if ap[4] != None else None
            apadrinamiento = Apadrinamiento(ap[5]) if ap[5] != None else None


    #metodo que comprueba si la condicion pasada como parametro devuelve tuplas en la query o si esta devuele un nulo 
    #el resultado es verdadero si se devuelve una tupla (o una lista de tuplas) y falso si no se encuentran tuplas
    def estaEnLaTabla(self, tabla: str, condicion: str)
        bd = BD()
        resultado = '*'
        ap = bd.selectEscalar(resultado,tabla,condicion)
        return ap != None

    #serie de comandos que devuelven los valores de los campos de la instancia
    def getIdEnvios(self):
        return self.id_envios

    def getDescripcion(self):
        return self.descripcion

    def getEnviadoPorSocio(self):
        return self.enviado_por_socio

    def getRecibido(self):
        return self.recibido

    def getRespuestaA(self):
        return self.respuestaA

    def getRepuestaAId(self):
        return self.respuestaA.getIdEnvios()

    def getApadrinamiento(self):
        return self.apadrinamiento

    def getApadrinamientoId(self):
        return self.apadrinamiento.getIdApadrinamiento()

    #se borra la instancia actual de apadrinamiento de la base de datos y la instancia se convierte en nula
    def delete(self):
        bd = BD()   
        condicion = 'id_envios = ' + str(self.id_envios)
        bd.delete(Envios.tabla,condicion)
        self.id_envios = None
        self.descripcion = None
        self.enviado_por_socio = None
        self.recibido = None
        self.respuestaA = None
        self.apadrinamiento = None

    def setIdEnvios(self, id_envios: int = None):
        #comprobación de que el valor no sea nulo
        if id_envios != None:
            bd = BD()
            condicion = 'id_envios = ' + str(id_envios)
            resultado = '*'
            ap = bd.selectEscalar(resultado,Envios.tabla,condicion)
            #compruebo que el valor no existe en la tabla para no incumplir la unicidad del atributo
            if ap == None or ap == []:
                condicion = 'id_envios = ' + str(self.id_envios)
                setter = 'id_envios = ' + str(id_envios)
                bd.update(Envios.tabla,setter,condicion)
                self.id_envios = id_envios
            else:
                print ('id_envios existente')
                return False
        else:
            print ('id_envios no puede ser null')
            return False
    
    def setDescripcion(self, descripcion: str = None):
        bd = BD()
        condicion = 'id_envios = ' + str(self.id_envios)
        setter = 'descripcion = ' + str(descripcion)
        bd.update(Envios.tabla,setter,condicion)
        self.descripcion = descripcion

    def setEnviadoPorSocio(self, enviado_por_socio: bool = None):
        bd = BD()
        condicion = 'id_envios = ' + str(self.id_envios)
        setter = 'enviado_por_socio = ' + str(enviado_por_socio)
        bd.update(Envios.tabla,setter,condicion)
        self.enviado_por_socio = enviado_por_socio

    def setRecibido(self, recibido: str = None):
        bd = BD()
        condicion = 'id_envios = ' + str(self.id_envios)
        setter = 'recibido = ' + str(recibido)
        bd.update(Envios.tabla,setter,condicion)
        self.recibido = recibido

    def setRespuestaA(self, respuestaA: int = None):
        bd = BD()
        #compruebo la existencia del envio al que se le responde en la tabla 
        condicion = ' id_envios = ' + str(respuestaA)
        ap = estaEnLaTabla(Envios.tabla,str(respuestaA))
        if not ap:
            print('Envio previo no existente')
            return False
        condicion = 'id_envios = ' + str(id_envios)
        if not respuestaA:
            setter = 'respuestaA = null'
        else:
            setter = 'respuestaA = ' + str(asociado_ACOES)
        bd.update(Envios.tabla,setter,condicion)
        self.respuestaA = getEnvios(respuestaA)

    def setApadrinamiento(self, apadrinamiento: int = None):
        if apadrinamiento:
            bd = BD()
            #compruebo la existencia del apadrinamiento
            condicion = 'id_apadrinamiento = ' + str(apadrinamiento)
            ap = bd.selectEscalar('*',' apadrinamiento ',condicion)
            if ap:
                condicion = 'id_envios = ' + str(id_envios)
                setter = 'apadrinamiento = ' + str(apadrinamiento)
                bd.update(Envios.tabla,setter,condicion)
                self.apadrinamiento = getApadrinamiento(apadrinamiento)
            else:
                print('Apadrinamiento no existente')
                return False
        else:
            print('La identificacion del apadrinamiento no puede ser nula')
            return False


    # método que permite crear una lista de colegios
    @staticmethod
    def listaEnvios():
        bd = BD()
        condicion = None
        ap = bd.select('*',Envios.tabla,condicion)
        #creo una lista vacia (que se usara para devolver el resultado)
        lista = []
        #cada tupla en la lista obtenida en la consulta se usa para crear una instancia de apadrinamiento y se agregan a la lista vacia
        for col in ap:
            id_envios = col[0]
            descripcion = col[1]
            enviado_por_socio = col[2]
            recibido = col[3]
            repuestaA = col[4]
            apadrinamiento = col[5]
            enviado = Envios(id_envios, descripcion, enviado_por_socio, recibido, respuestaA, apadrinamiento)
            lista.append(enviado)
        return lista


    # método que retorna una representación de la instancia de la clase
    def __repr__(self):
        cadena = ''
        if self.id_envios != None: 
            cadena += 'Envio'+ str(self.id_envios) + ' - '
        if self.descripcion != None: 
            cadena += 'Descripcion ' + self.descripcion + ' - '
        if self.enviado_por_socio != None:
            cadena += 'Enviado por socio ' + str(self.enviado_por_socio) + ' - '
        if self.recibido != None: 
            cadena += 'Recibido ' + str(self.recibido) + ' - '
        if self.respuestaA != None:
            cadena += 'Respuesta a envio ' + str(self.respuestaA.getIdEnvios()) + ' - '
        if self.apadrinamiento != None:
            cadena += 'Apadrinamiento ' + str(self.apadrinamiento.getIdApadrinamiento()) + ' - '
        if cadena == '':
            cadena = 'Envio vacío - ' 
        
        return cadena[:-3]

if __name__ == '__main__':
    