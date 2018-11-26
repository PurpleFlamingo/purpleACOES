from BD.BD import BD

class BDOperaciones:

    def login(self,user: str, password: str):
        db = BD()
        nombre = "LOWER(`nombre`) = \"" + user + "\""
        claveBD = db.selectEscalar("clave","usuario",nombre)
        if password == claveBD[0]:
            print("login correcto")
            return True
        else:
            print("login incorrecto")
            return False

    def recovery(self,user: str):
        db = BD()
        nombre = "LOWER(`nombre`) = \"" + user + "\""
        claveBD = db.selectEscalar("id_usuario, clave, rol","usuario",nombre)
        if claveBD != None:
            claveRecuperada = claveBD[1]
            if claveBD[2] == "Socio":
                tabla = "socio"
            else:
                tabla = "voluntario"
            cond = "LOWER(`usuario`) = " + (str(claveBD[0])).lower()

            emailDB = db.selectEscalar("correo_electronico",tabla,cond)
            if(emailDB[0] != None):
                return claveRecuperada, False
            else:
                return claveRecuperada, True
        else:
            return None, None


    def getUsuarios(self):
        db = BD()
        return db.select('*', 'usuario')

if __name__ == '__main__':
    l = BDOperaciones()

    l.getUsuarios()

    l.login("Rafael","1234")

    l.recovery("Rafael")

    l.recovery("Paco")
