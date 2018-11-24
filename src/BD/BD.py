from __future__ import print_function
import mysql.connector
from mysql.connector import Error


class BD:

    def __init__(self,servidor: str, puerto: int, baseDeDatos: str, usuario: str, clave: str):
        try:
            self.conn = mysql.connector.connect(host=servidor,port=puerto,database=baseDeDatos,user=usuario,password=clave)
            if self.conn.is_connected():
                print('Connected to MySQL on host {}:{} to database {}'.format(servidor,puerto,baseDeDatos))
        except Error as e:
            print(e)

    def select(self, resultado: str, tabla: str, condicion = None):
        try:
            cursor = self.conn.cursor()
            if condicion is None:
                query = 'SELECT ' + resultado + ' from ' + tabla + ';'
            else:
                query = 'SELECT ' + resultado + ' from ' + tabla + ' where ' + condicion + ';'
            #print('El select es: ',self.query)
            cursor.execute(query)
            myresult = cursor.fetchall()
            cursor.close()
            return myresult
        except Error as e:
            print(e)

    def selectEscalar(self, resultado: str, tabla: str, condicion: str = None):
        return self.select(resultado, tabla, condicion)[0]

    def insert(self, valores: list, tabla: str):
        try:
            cursor = self.conn.cursor()

            #Format the insert values depending on type
            stringValores = ''
            for elemento in valores:
                if type(elemento) is bool:
                    stringValores += ('TRUE' if elemento else 'FALSE')
                elif type(elemento) is not int:
                    stringValores +='\"'+elemento+'\"'
                else:
                    stringValores += str(elemento)
                stringValores += ','
            #Elimina la ultima ','
            stringValores = stringValores[:-1]

            query = 'insert values(' + stringValores +') into ' + tabla + ';'
            #print(query)
            cursor.execute(query)
            cursor.close()
            return
        except Error as e:
            print(e)

    def delete(self, tabla: str, condicion: str = None):
        try:
            cursor = self.conn.cursor()
            if condicion is None:
                query = 'delete from ' + tabla + ';'
            else:
                query = 'delete from ' + tabla + ' where ' + condicion + ';'
            print(query)
            #cursor.execute(query)
            cursor.close()
            return
        except Error as e:
            print(e)

if __name__ == '__main__':
    bd = BD('jfaldanam.ddns.net',3306,'gestorACOES','martin','password_martin')

    #abc = bd.select('*','usuario','nombre = \'Rafael\'')
    #print(abc)
    abc = bd.select('*','usuario')
    #bd.insert(['rol1', 'descripcion1', False, 8], 'rol')
    #bd.delete('usuario', 'nombre = \'Rafael\'')
    print(abc)
