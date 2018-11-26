from BD.BD import BD

class BDOperaciones:

    #Recibe un usuario y contrasena y comprueba contra la base de datos si es unb login correcto o no
    #Returns boolean (False si el login es erroneo)
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

    #Recive un usuario y devuelve su contrasena y si tiene un correo electronico asociado o no
    #Returns string, boolean (Contrasena, False si no tiene correo asociado)
    #Returns NONE, NONE (si no se encuentra usuario)
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

    #Recibe un usuario y un email y actualiza el email almacenado en la base de datos
    #Reurns boolean (False si no se encuentra el usuario)
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

    #Devuelve todos los usuarios de la base de datos y su correspondiente informacion de socio/voluntario
    #Returns [users], where user is [[list with data from usuario],[list with data from voluntario/socio]]
    def getUsuarios(self):
        db = BD()
        usuarios = db.select('*', 'usuario')
        result = []
        for user in usuarios:
            if user[3] == 'Socio':
                datosSocio = db.selectEscalar('*', 'socio', 'usuario=\'' + str(user[0]) + '\'')
                result.append([user, datosSocio])
            else:
                datosVoluntario = db.selectEscalar('*', 'voluntario', 'usuario=\'' + str(user[0]) + '\'')
                result.append([user, datosVoluntario])
        return result

    def getSocio(self, ID):
    	db=BD()
    	datosSocio= db.selectEscalar('*','socio', 'id_socio='+str(ID));
    	return datosSocio;

if __name__ == '__main__':
    l = BDOperaciones()

    l.getUsuarios()

    l.login("Rafael","1234")

    l.recovery("Rafael")

    l.recovery("Paco")
