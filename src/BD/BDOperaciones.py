from BD.BD import BD

class BDOperaciones:

    def login(self,user: str, password: str):
        db = BD()
        nombre = "nombre = \"" + user + "\""
        claveBD = db.selectEscalar("clave","usuario",nombre)
        if password == claveBD[0]:
            print("login correcto")
        else:
            print("login incorrecto")

    def recovery(self,user: str):
        db = BD()
        nombre = "nombre = \"" + user + "\""
        claveBD = db.selectEscalar("identificacion, clave, rol","usuario",nombre)
        if claveBD[2] == "Socio":
            tabla = "socio"
        else:
            tabla = "agente"
        cond = "identificacion = " + str(claveBD[0])

        emailDB = db.selectEscalar("correo_electronico",tabla,cond)
        print(user)
        if(emailDB[0] == None):
            print("El usuario no posee correo electronico")
        else:
            print("Correo_electronico: ",emailDB[0])

        print("La contraseña es :", claveBD[1])

    def getUsuarios(self):
        db = BD()
        return db.select('*', 'usuario')

if __name__ == '__main__':
    l = BDOperaciones()

    l.getUsuarios()

    l.login("Rafael","1234")

    l.recovery("Rafael")

    l.recovery("Paco")
