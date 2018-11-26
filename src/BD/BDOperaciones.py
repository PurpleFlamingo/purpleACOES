from BD.BD import BD

class BDOperaciones:

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

    def getUsuarios(self):
        db = BD()
        return db.select('*', 'usuario')

if __name__ == '__main__':
    l = BDOperaciones()

    l.getUsuarios()

    l.login("Rafael","1234")

    l.recovery("Rafael")

    l.recovery("Paco")
