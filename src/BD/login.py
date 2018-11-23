from BD import BD

class login:

    def __init__(self,user: str, password: str):
        self.server = "localhost"
        self.puerto = 3307
        self.base = "gestoracoes"
        self.usuario = "root"
        self.clave = "intendo64R"
        self.db = BD(self.server,self.puerto,self.base,self.usuario,self.clave)
        self.nombre = "nombre = \"" + user + "\""
        self.claveBD = self.db.selectConditionEscalar("clave","usuario",self.nombre)
        if password == self.claveBD:
            print("login correcto")
        else:
            print("login incorrecto")

if __name__ == '__main__':
    login("Rafael","1234")
 