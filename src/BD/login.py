from BD import BD

class login:

    def __init__(self,user: str, password: str):
        self.db = BD()
        self.nombre = "nombre = \"" + user + "\""
        self.claveBD = self.db.selectEscalar("clave","usuario",self.nombre)
        if password == self.claveBD[0]:
            print("login correcto")
        else:
            print("login incorrecto")

    def recovery(self,user: str):
        self.db = BD()
        self.nombre = "nombre = \"" + user + "\""
        self.claveBD = self.db.selectEscalar("identificacion, clave, rol","usuario",self.nombre)
        if self.claveBD[2] == "Socio":
            self.tabla = "socio"
        else:
            self.tabla = "agente"
        self.cond = "identificacion = " + str(self.claveBD[0])

        self.emailDB = self.db.selectEscalar("correo_electronico",self.tabla,self.cond)
        print(user)
        if(self.emailDB[0] == None):
            print("El usuario no posee correo electronico")
        else:
            print("Correo_electronico: ",self.emailDB[0])

        print("La contraseña es :", self.claveBD[1])

if __name__ == '__main__':
    l = login("Rafael","1234")

    l.recovery("Rafael")

    l.recovery("Paco")
