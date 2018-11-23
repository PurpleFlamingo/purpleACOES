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


    def selectSimple(self, resultado: str, tabla: str):
        try:
            self.cursor = self.conn.cursor()
            self.query = "SELECT " + resultado + " from " + tabla + ";"
            self.cursor.execute(self.query)
            self.myresult = self.cursor.fetchall()
            self.cursor.close()
            return self.myresult
        except Error as e:
            print(e)

    def selectSimpleEscalar(self, resultado: str, tabla: str):
        return self.selectSimple(resultado, tabla)[0][0]

    def selectCondition(self, resultado: str, tabla: str, condicion: str):
        try:
            self.cursor = self.conn.cursor()
            self.query = "SELECT " + resultado + " from " + tabla + " where " + condicion + ";"
            #print("El select es: ",self.query)
            self.cursor.execute(self.query)
            self.myresult = self.cursor.fetchall()
            self.cursor.close()
            return self.myresult
        except Error as e:
            print(e)

    def selectConditionEscalar(self, resultado: str, tabla: str, condicion: str):
        return self.selectCondition(resultado, tabla, condicion)[0][0]



if __name__ == '__main__':
    bd = BD('localhost',3307,'gestoracoes','root','intendo64R')

    bd.selectCondition("*","usuario","nombre = Rafael")

    bd.selectSimple("*","usuario")

