from BD.BD import BD


class BDOperaciones:

    # Recibe un usuario y contrasena y comprueba contra la base de datos si es unb login correcto o no
    # Returns boolean (False si el login es erroneo)
    def login(self,user: str, password: str):
        db = BD()
        nombre = "LOWER(`nombre`) = \"" + user + "\""
        claveBD = db.selectEscalar("clave","usuario",nombre)
        if claveBD == None or password != claveBD[0]:
            print("login incorrecto")
            return False
        else:
            print("login correcto")
            return True

    # Recibe un usuario y devuelve su contrasena y si tiene un correo electronico asociado o no
    # Returns string, boolean (Contrasena, False si no tiene correo asociado)
    # Returns NONE, NONE (si no se encuentra usuario)
    def recovery(self,user: str):
        db = BD()
        nombre = "LOWER(`nombre`) = \"" + user.lower() + "\""
        claveBD = db.selectEscalar("id_usuario, clave, rol","usuario",nombre)
        if claveBD != None:
            claveRecuperada = claveBD[1]
            cond = "LOWER(`usuario`) = " + (str(claveBD[0])).lower()
            if claveBD[2] == "Socio":
                tabla = "socio"
            else:
                tabla = "voluntario"
            emailDB = db.selectEscalar("correo_electronico",tabla,cond)
            if(emailDB[0] != None):
                return claveRecuperada, False
            else:
                return claveRecuperada, True
        else:
            return None, None

    # Recibe un usuario y un email y actualiza el email almacenado en la base de datos
    # Reurns boolean (False si no se encuentra el usuario)
    def actualizarEmail(self, user: str, email: str):
        db = BD()
        nombre = "LOWER(`nombre`) = \"" + user.lower() + "\""
        claveBD = db.selectEscalar("id_usuario, rol","usuario",nombre)
        if claveBD != None:
            cond = "LOWER(`usuario`) = " + (str(claveBD[0])).lower()
            if claveBD[1] == "Socio":
                tabla = "socio"
            else:
                tabla = "voluntario"
            setter = "correo_electronico = \'" + email + "\'"
            cond = "usuario = " + str(claveBD[0])
            db.update(tabla, setter, cond)
            return True
        else:
            return False
    # Devuelve una lista con todos los nombres de columnas de una tabla
    # Returns [string]
    def nombreColumnas(self, tabla: str):
        db = BD()
        result = db.describe(tabla)
        columnas = []
        for columna in result:
            columnas.append(columna[0])
        return columnas

    # Devuelve todos los usuarios de la base de datos y su correspondiente informacion de socio/voluntario
    # Returns [users], where `user` is a dictionary with all data indexed by the column names in the database
    def getUsuarios(self):
        db = BD()
        usuarios = db.select('*', 'usuario')
        colUsuario = self.nombreColumnas('usuario')
        colSocio = self.nombreColumnas('socio')
        colVoluntario = self.nombreColumnas('voluntario')
        result = []
        for user in usuarios:
            if user[3] == 'Socio':
                datosSocio = db.selectEscalar('*', 'socio', 'usuario=\'' + str(user[0]) + '\'')
                dictSocio = {}
                for i, col in enumerate(colUsuario):
                    dictSocio[col] = user[i]
                for i, col in enumerate(colSocio):
                    dictSocio[col] = datosSocio[i]
                result.append(dictSocio)
            else:
                datosVoluntario = db.selectEscalar('*', 'voluntario', 'usuario=\'' + str(user[0]) + '\'')
                dictVoluntario = {}
                for i, col in enumerate(colUsuario):
                    dictVoluntario[col] = user[i]
                for i, col in enumerate(colVoluntario):
                    dictVoluntario[col] = datosVoluntario[i]
                result.append(dictVoluntario)
        return result

    # Devuelve la datos del socio que tiene esa ID
    # Returns []
    def getSocio(self, ID: int):
    	db=BD()
    	datosSocio= db.selectEscalar('*','socio', 'usuario=' + str(ID))
    	return datosSocio;

    # Devuelve la datos del usuario que tiene esa ID
    # Returns []
    def getUsuario(self, ID: int):
        db=BD()
        datosUsuario= db.selectEscalar('*','usuario', 'id_usuario=' + str(ID))
        return datosUsuario;

    # Devuelve la datos del voluntario que tiene esa ID
    # Returns []
    def getVoluntario(self, ID: int):
        db=BD()
        datosVoluntario= db.selectEscalar('*', 'voluntario', 'usuario=' + str(ID))
        return datosVoluntario;

    def getID(self, nombre: str):
        db = BD()
        id = db.selectEscalar('id_usuario', 'usuario', 'nombre = \'' + str(nombre) + '\'')
        return id[0]

    #Actualiza los datos de un usuario(idUser) que tiene rol(rolUser)
    #datosUsuario y datosOtros deben tener todos los campos que de usuario, con
    #None en los que no se vayan a actualizar
    def actualizarUsuario(self, datosUsuario, datosOtros, idUser, rolUser):
        db = BD()
        colUsuario = self.nombreColumnas('usuario')
        update = ''
        for i, col in enumerate(colUsuario[1:]):
            if datosUsuario[i] == None:
                continue
            else:
                update += (col + '=\'' + datosUsuario[i]+'\',')

        update = update[:-1]
        db.update('usuario', update, 'id_usuario='+str(idUser))

        if rolUser == 'Socio':
            colSocio = self.nombreColumnas('socio')
            update = ''
            for i, col in enumerate(colSocio[1:]):
                if datosOtros[i] == None:
                    continue
                else:
                    update += (col + '=\'' + datosOtros[i]+'\',')
            update = update[:-1]
            #print(update)
            db.update('socio', update, 'usuario='+str(idUser))
        else:
            colVol = self.nombreColumnas('voluntario')
            update = ''
            for i, col in enumerate(colVol[1:]):
                if datosOtros[i] == None:
                    continue
                else:
                    update += (col + '=\'' + datosOtros[i]+'\',')
            update = update[:-1]
            #print(update)
            db.update('voluntario', update, 'usuario='+str(idUser))

    #Inserta un usuario nuevo en la base de datos
    #datosUsuario y datosOtros deben tener todos los campos que de usuario, con
    #'' en los que no se vayan a actualizar
    def insertarUsuario(self, datosUsuario, datosOtros):
        db=BD()
        id=db.selectEscalar("max(id_usuario)", "usuario")[0]+1
        db.insert([id]+datosUsuario, "usuario" )
        if datosUsuario[2]=="Socio":
            allColumnas = self.nombreColumnas('socio')
            columnas = ['usuario']
            for i, col in enumerate(allColumnas[1:]):
                if datosOtros[i] != '':
                    columnas.append(col)
            datosOtros = [x for x in datosOtros if x != '']
            db.insertParcial(columnas, [id]+datosOtros,"socio")
        else:
            allColumnas = self.nombreColumnas('voluntario')
            columnas = ['usuario']
            for i, col in enumerate(allColumnas[1:]):
                if datosOtros[i] != '':
                    columnas.append(col)
            datosOtros = [x for x in datosOtros if x != '']
            db.insertParcial(columnas, [id]+datosOtros,"voluntario")




    # Cambia la contraseña del usuario de ese ID
    def setPassUsuario(self, passw: str, ID: int):
        db = BD()
        db.update('usuario', 'clave=\'' + passw + '\'', 'id_usuario=' + str(ID))



if __name__ == '__main__':
    l = BDOperaciones()

    l.getUsuarios()

    l.login("Rafael","1234")

    l.recovery("Rafael")

    l.recovery("Paco")
