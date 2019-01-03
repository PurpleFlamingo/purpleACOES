import sys
from BD.BD import BD
from BD.Colegio import Colegio
from BD.Colonia import Colonia

class Joven:
    tabla = 'joven'
    def __init__(self, idJoven = None, nombre = None, apellidos = None, nombrePadre = None, nombreMadre = None, estado = None, 
    urlFoto = None, fechaNacimiento = None, fechaAlta = None, fechaAltaACOES = None, fechaSalidaACOES = None, grado = None, 
                 historial=None, observaciones=None, coloniaNacimiento=None, coloniaResidencia=None, colegio=None):
        self.idJoven = idJoven
        self.nombre = nombre
        self.apellidos = apellidos
        self.nombrePadre = nombrePadre
        self.nombreMadre = nombreMadre
        self.estado = estado
        self.urlFoto = urlFoto
        self.fechaNacimiento = fechaNacimiento
        self.fechaAlta = fechaAlta
        self.fechaAltaACOES = fechaAltaACOES
        self.fechaSalidaACOES = fechaSalidaACOES
        self.grado = grado
        self.historial = historial
        self.observaciones = observaciones
        self.coloniaNacimiento = coloniaNacimiento
        self.coloniaResidencia = coloniaResidencia
        self.colegio = colegio

    @staticmethod
    def newJoven(idJoven, nombre, apellidos, nombrePadre = None, nombreMadre = None, estado = None, urlFoto = None, fechaNacimiento = None, fechaAlta = None, fechaAltaACOES = None, fechaSalidaACOES = None, grado = None, historial = None, observaciones = None, coloniaNacimiento = None, coloniaResidencia = None, colegio = None):
        bd = BD()
        print('fecha alta acoes: ', fechaAltaACOES)
        if idJoven == None:
            print('idJoven no puede ser null')
            return None
        if nombre == None:
            print('el nombre no puede ser null')
            return None
        if apellidos == None:
            print('el apellido no puede ser null')
            return None
        if fechaAltaACOES == None:
            print('la fecha de alta en acoes no puede ser null')
            return None
        if coloniaNacimiento == None:
            print('la colonia de nacimiento no puede ser null')
            return None
        if coloniaResidencia == None:
            print('la colonia de residencia no puede ser null')
            return None
        if colegio == None:
            print('el colegio no puede ser null')
            return None
        
        condicion = 'id_joven = ' + str(idJoven)
        res = bd.selectEscalar('*', Joven.tabla, condicion)
        if not res:        
            valores = [idJoven, nombre, apellidos, nombrePadre if nombrePadre != None else 'null', nombreMadre if nombreMadre != None else 'null', 
                estado if estado != None else 'null', urlFoto if urlFoto != None else 'null', fechaNacimiento if fechaNacimiento != None else 'null', 
                fechaAltaACOES, fechaAlta if fechaAlta != None else 'null', fechaSalidaACOES if fechaSalidaACOES != None else 'null',
                grado if grado != None else 'null', historial if historial != None else 'null', observaciones if observaciones != None else 'null', 
                coloniaNacimiento, coloniaResidencia, colegio]
            bd.insert(valores, Joven.tabla)
            newJoven = Joven(idJoven, nombre, apellidos, nombrePadre, nombreMadre, estado, urlFoto, fechaNacimiento, fechaAlta, fechaAltaACOES, fechaSalidaACOES, grado, historial, observaciones, coloniaNacimiento, coloniaResidencia, colegio)
            return newJoven
        else:
            print('Error: El id de joven {} ya esta en uso'.format(idJoven))
            return None

    @staticmethod
    def getJoven(idJoven: int):
        bd = BD()

        condicion = 'id_joven = \'' + str(idJoven) + '\''
        res = bd.selectEscalar('*', Joven.tabla, condicion)
        if not res:
            #El joven no existe
            return None
        else:
            idJoven = res[0]
            nombre = res[1]
            apellidos = res[2]
            nombrePadre = res[3]
            nombreMadre = res[4]
            estado = res[5]
            urlFoto = res[6]
            fechaNacimiento = res[7]
            fechaAlta = res[8]
            fechaAltaACOES = res[9]
            fechaSalidaACOES = res[10]
            grado = res[11]
            historial = res[12]
            observaciones = res[13]
            coloniaNacimiento = Colonia(res[14])
            coloniaResidencia = Colonia(res[15])
            colegio = Colegio(res[16])
            newJoven = Joven(idJoven, nombre, apellidos, nombrePadre, nombreMadre, estado, urlFoto, fechaNacimiento, fechaAlta, fechaAltaACOES, fechaSalidaACOES, grado, historial, observaciones, coloniaNacimiento, coloniaResidencia, colegio)
            return newJoven
            
    @staticmethod
    def listaJovenes():
        bd = BD()
        jovenes = bd.select('*', Joven.tabla)
        listJovenes = []
        for joven in jovenes:
            idJoven = joven[0]
            nombre = joven[1]
            apellidos = joven[2]
            nombrePadre = joven[3]
            nombreMadre = joven[4]
            estado = joven[5]
            urlFoto = joven[6]
            fechaNacimiento = joven[7]
            fechaAlta = joven[8]
            fechaAltaACOES = joven[9]
            fechaSalidaACOES = joven[10]
            grado = joven[11]
            historial = joven[12]
            observaciones = joven[13]
            coloniaNacimiento = Colonia(joven[14])
            coloniaResidencia = Colonia(joven[15])
            colegio = Colegio(joven[16])
            newJoven = Joven(idJoven, nombre, apellidos, nombrePadre, nombreMadre, estado, urlFoto, fechaNacimiento, fechaAlta, fechaAltaACOES, fechaSalidaACOES, grado, historial, observaciones, coloniaNacimiento, coloniaResidencia, colegio)
            listJovenes.append(newJoven)
        return listJovenes

    #Getters
    def getIdJoven(self):
        return self.idJoven

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellidos

    def getNombrePadre(self):
        return self.nombrePadre

    def getNombreMadre(self):
        return self.nombreMadre

    def getEstado(self):
        return self.estado

    def getFoto(self):
        return self.urlFoto

    def getFechaNacimiento(self):
        return self.fechaNacimiento

    def getFechaAlta(self):
        return self.fechaAlta

    def getFechaAltaACOES(self):
        return self.fechaAltaACOES

    def getFechaSalidaACOES(self):
        return self.fechaSalidaACOES

    def getGrado(self):
        return self.grado

    def getHistorial(self):
        return self.historial

    def getObservaciones(self):
        return self.observaciones

    def getColoniaNacimiento(self):
        return self.coloniaNacimiento

    def getColoniaResidencia(self):
        return self.coloniaResidencia

    def getColegio(self):
        return self.colegio

    #Setters

    def setIdJoven(self, newID):
        if newID != None:
            bd = BD()
            condicion  = 'id_joven = \'' + idJoven + '\''
            res = bd.selectEscalar('*', Joven.tabla, condicion)
            if not res:
                condicion = 'id_joven = \'' + self.idJoven + '\''
                setter = 'id_joven = ' + newID
                bd.update(Joven.tabla, setter, condicion)
                self.idJoven = newID
                return True 
            else:
                #ID ya existe
                return False
        else:
            #No se puede insertar id null
            return False

    def setNombre(self, newNombre):
        if newNombre != None:
            bd = BD()
            condicion  = 'id_joven = \'' + idJoven + '\''
            setter = 'nombre = \'' + newNombre + '\''
            bd.update(Joven.tabla, setter, condicion)
            self.nombre = newNombre
            return True
        else:
            return False

    def setApellido(self, newApellidos):
        if newApellidos != None:
            bd = BD()
            condicion  = 'id_joven = \'' + idJoven + '\''
            setter = 'apellidos = \'' + newApellidos + '\''
            bd.update(Joven.tabla, setter, condicion)
            self.apellidos = newApellidos
            return True
        else:
            return False

    def setNombrePadre(self, newNombrePadre):
        if newNombrePadre != None:
            bd = BD()
            condicion  = 'id_joven = \'' + idJoven + '\''
            setter = 'nombre_del_padre = \'' + newNombrePadre + '\''
            bd.update(Joven.tabla, setter, condicion)
            self.nombrePadre = newNombrePadre
            return True
        else:
            return False

    def setNombreMadre(self, newNombreMadre):
        if newNombreMadre != None:
            bd = BD()
            condicion  = 'id_joven = \'' + idJoven + '\''
            setter = 'nombre_de_la_madre = \'' + newNombreMadre + '\''
            bd.update(Joven.tabla, setter, condicion)
            self.nombreMadre = newNombreMadre
            return True
        else:
            return False

    def setEstado(self, newEstado):
        if newEstado != None:
            bd = BD()
            condicion  = 'id_joven = \'' + idJoven + '\''
            setter = 'estado = \'' + newEstado + '\''
            bd.update(Joven.tabla, setter, condicion)
            self.estado = newEstado
            return True
        else:
            return False

    def setFoto(self, newURL):
        if newURL != None:
            bd = BD()
            condicion  = 'id_joven = \'' + idJoven + '\''
            setter = 'url_foto = \'' + newURL + '\''
            bd.update(Joven.tabla, setter, condicion)
            self.urlFoto = newURL
            return True
        else:
            return False

    def setFechaNacimiento(self, newFechaNacimiento):
        if newFechaNacimiento != None:
            bd = BD()
            condicion  = 'id_joven = \'' + idJoven + '\''
            setter = 'fecha_nacimiento = \'' + newFechaNacimiento + '\''
            bd.update(Joven.tabla, setter, condicion)
            self.fechaNacimiento = newFechaNacimiento
            return True
        else:
            return False

    def setFechaAlta(self, newFechaAlta):
        if newFechaAlta != None:
            bd = BD()
            condicion  = 'id_joven = \'' + idJoven + '\''
            setter = 'fecha_de_alta = \'' + newFechaAlta + '\''
            bd.update(Joven.tabla, setter, condicion)
            self.fechaAlta = newFechaAlta
            return True
        else:
            return False

    def setFechaAltaACOES(self, newFechaAltaACOES):
        if newFechaAltaACOES != None:
            bd = BD()
            condicion  = 'id_joven = \'' + idJoven + '\''
            setter = 'fecha_de_alta_acoes = \'' + newFechaAltaACOES + '\''
            bd.update(Joven.tabla, setter, condicion)
            self.fechaAltaACOES = newFechaAltaACOES
            return True
        else:
            return False

    def setFechaSalidaACOES(self, newFechaSalidaACOES):
        if newFechaSalidaACOES != None:
            bd = BD()
            condicion  = 'id_joven = \'' + idJoven + '\''
            setter = 'fecha_de_salida_acoes = \'' + newFechaSalidaACOES + '\''
            bd.update(Joven.tabla, setter, condicion)
            self.fechaSalidaACOES = newFechaSalidaACOES
            return True
        else:
            return False

    def setGrado(self, newGrado):
        if newGrado != None:
            bd = BD()
            condicion  = 'id_joven = \'' + idJoven + '\''
            setter = 'grado = \'' + newGrado + '\''
            bd.update(Joven.tabla, setter, condicion)
            self.grado = newGrado
            return True
        else:
            return False

    def setHistorial(self, newHistorial):
        if newHistorial != None:
            bd = BD()
            condicion  = 'id_joven = \'' + idJoven + '\''
            setter = 'historial = \'' + newHistorial + '\''
            bd.update(Joven.tabla, setter, condicion)
            self.historial = newHistorial
            return True
        else:
            return False

    def setObservaciones(self, newObservaciones):
        if newObservaciones != None:
            bd = BD()
            condicion  = 'id_joven = \'' + idJoven + '\''
            setter = 'observaciones = \'' + newObservaciones + '\''
            bd.update(Joven.tabla, setter, condicion)
            self.observaciones = newObservaciones
            return True
        else:
            return False

    def setColoniaNacimiento(self, newColoniaNacimiento):
        if newColoniaNacimiento != None:
            bd = BD()
            condicion  = 'id_joven = \'' + idJoven + '\''
            setter = 'colonia_nacimiento = \'' + newColoniaNacimiento.getIdColonia() + '\''
            bd.update(Joven.tabla, setter, condicion)
            self.coloniaNacimiento = newColoniaNacimiento
            return True
        else:
            return False

    def setColoniaResidencia(self, newColoniaResidencia):
        if newColoniaResidencia != None:
            bd = BD()
            condicion  = 'id_joven = \'' + idJoven + '\''
            setter = 'colonia_residencia = \'' + newColoniaResidencia.getIdColonia() + '\''
            bd.update(Joven.tabla, setter, condicion)
            self.coloniaResidencia = newColoniaResidencia
            return True
        else:
            return False

    def setColegio(self, newColegio):
        if newColegio != None:
            bd = BD()
            condicion  = 'id_joven = \'' + idJoven + '\''
            setter = 'colegio = \'' + newColegio.getIdColegio() + '\''
            bd.update(Joven.tabla, setter, condicion)
            self.colegio = newColegio
            return True
        else:
            return False


    def delete(self):
        bd = BD()
        condicion = 'id_joven = \'' + idJoven + '\''
        bd.delete(Joven.tabla, condicion)
        self.idJoven = None
        self.nombre = None
        self.apellidos = None
        self.nombrePadre = None
        self.nombreMadre = None
        self.estado = None
        self.urlFoto = None
        self.fechaNacimiento = None
        self.fechaAlta = None
        self.fechaAltaACOES = None
        self.fechaSalidaACOES = None
        self.grado = None
        self.historial = None
        self.observaciones = None
        self.coloniaNacimiento = None
        self.coloniaResidencia = None
        self.colegio = None


    def __repr__(self):
        toStr = ''
        if self.idJoven != None:
            toStr += 'Id Joven: ' + str(self.idJoven) + ' - '
        if self.nombre != None:
            toStr += 'Nombre: ' + self.nombre + ' - '
        if self.apellidos != None:
            toStr += 'Apellidos: ' + self.apellidos + ' - '
        if self.nombrePadre != None: 
            toStr += 'Nombre padre: ' + self.nombrePadre + ' - '
        if self.nombreMadre != None: 
            toStr += 'Nombre madre: ' + self.nombreMadre + ' - '
        if self.estado != None: 
            toStr += 'estado: ' + self.estado + ' - '
        if self.urlFoto != None: 
            toStr += 'Foto: ' + self.urlFoto + ' - '
        if self.fechaNacimiento != None: 
            toStr += 'Fecha nacimiento: ' + self.fechaNacimiento + ' - '
        if self.fechaAlta != None: 
            toStr += 'Fecha alta: ' + self.fechaAlta + ' - '
        if self.fechaAltaACOES != None:
            toStr += 'Fecha alta ACOES: ' + self.fechaAltaACOES + ' - '
        if self.fechaSalidaACOES != None: 
            toStr += 'Fecha salida ACOES: ' + self.fechaSalidaACOES + ' - '
        if self.grado != None: 
            toStr += 'Grado: ' + self.grado + ' - '
        if self.historial != None: 
            toStr += 'Historial: ' + self.historial + ' - '
        if self.observaciones != None: 
            toStr += 'Observaciones: ' + self.observaciones + ' - '
        if self.coloniaNacimiento != None:
            toStr += 'Colonia nacimiento: ' + str(self.coloniaNacimiento) + ' - '
        if self.coloniaResidencia != None:
            toStr += 'Colonia residencia: ' + str(self.coloniaResidencia) + ' - '
        if self.colegio != None:
            toStr += 'Colegio: ' + str(self.colegio) + ' - '
        if toStr == '':
            toStr = 'Joven sin inicializar - '
        return toStr[:-3]

if __name__ == '__main__':
    print('e')
