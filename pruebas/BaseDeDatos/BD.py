from __future__ import print_function
import mysql.connector
from mysql.connector import Error


class BD:

    def __init__(self,servidor: str, puerto: int, baseDeDatos: str, usuario: str, clave: str):
        try:
            self.conn = mysql.connector.connect(host=servidor,port=puerto,database=baseDeDatos,user=usuario,password=clave)
            if self.conn.is_connected():
                print('Connected to MySQL database')
        except Error as e:
            print(e)
            exit()


    def selectSimple(self, resultado: str, tabla: str):
        try:
            self.cursor = self.conn.cursor()
            self.query = "SELECT " + resultado + " from " + tabla + ";"
            self.cursor.execute(self.query)

            cursor.close()
        except Error as e:
            print(e)

    def selectCondition(self, resultado: str, tabla: str, condicion: str):
        try:
            self.cursor = self.conn.cursor()
            self.query = "SELECT " + resultado + " from " + tabla + " where " + condicion + ";"
            self.cursor.execute(self.query)

            cursor.close()
        except Error as e:
            print(e)


if __name__ == '__main__':
    bd = BD('localhost',3307,'administracion','root','intendo64R')

    bd.selectCondition("*","usuario","nombre = pepe")

    bd.selectSimple("*","agente")
