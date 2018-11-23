from __future__ import print_function
import mysql.connector
from mysql.connector import Error


class BD:

    def __init__(self,servidor: str, puerto: int, baseDeDatos: str, usuario: str, clave: str):
        try:
            self.conn = mysql.connector.connect(host=servidor,port=puerto,database=baseDeDatos,user=usuario,password=clave)
            #if self.conn.is_connected():
            #    print('Connected to MySQL database')
        except Error as e:
            print(e)

    def select(self, resultado: str, tabla: str, condicion = None):
        try:
            self.cursor = self.conn.cursor()
            if(condicion == None):
                self.query = "SELECT " + resultado + " from " + tabla + ";"
            else:
                self.query = "SELECT " + resultado + " from " + tabla + " where " + condicion + ";"
            #print("El select es: ",self.query)
            self.cursor.execute(self.query)
            self.myresult = self.cursor.fetchall()
            self.cursor.close()
            return self.myresult
        except Error as e:
            print(e)

    def selectEscalar(self, resultado: str, tabla: str, condicion = None):
        return self.select(resultado, tabla, condicion)[0]



if __name__ == '__main__':
    bd = BD('localhost',3307,'gestoracoes','root','intendo64R')

    abc = bd.select("*","usuario","nombre = \"Rafael\"")
    print(abc)
    abc = bd.select("*","usuario")
    print(abc)
