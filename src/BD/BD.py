from __future__ import print_function
import mysql.connector
from mysql.connector import Error


class BD:

    def __init__(self):
        try:
            credenciales = self.leerCredenciales()
            self.conn = mysql.connector.connect(host=credenciales[0],port=credenciales[1],database=credenciales[2],user=credenciales[3],password=credenciales[4])
            if self.conn.is_connected():
                print('Connected to MySQL on host {}:{} to database {}'.format(credenciales[0],credenciales[1],credenciales[2]))
        except Error as e:
            print(e)

    def leerCredenciales(self):
        with open ('BD/database.config') as file:
            i = 0
            credenciales = [None]*5
            for line in file:
                credenciales[i] = line.strip().split(':')[1]
                i = i + 1
            return credenciales

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
        lista = self.select(resultado, tabla, condicion)
        if lista == None or lista == []:
            return None
        else:
            return lista[0]

    def insert(self, valores: list, tabla: str):
        try:
            cursor = self.conn.cursor()

            #Format the insert values depending on type
            stringValores = ''
            for elemento in valores:
                if type(elemento) is bool:
                    stringValores += ('TRUE' if elemento else 'FALSE')
                elif elemento == 'null':
                    stringValores += elemento
                elif type(elemento) is not int:
                    stringValores +='\"'+elemento+'\"'
                else:
                    stringValores += str(elemento)
                stringValores += ','
            #Elimina la ultima ','
            stringValores = stringValores[:-1]
            query = 'insert into ' + tabla + ' values (' + stringValores +');'
            #print(query)
            cursor.execute(query)
            self.conn.commit()
            cursor.close()
            return
        except Error as e:
            print(e)

    def insertParcial(self,columnas: list, valores: list, tabla: str):
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

            stringColumnas = ''
            for elemento in columnas:
                stringColumnas+=elemento
                stringColumnas+=','
            stringColumnas = stringColumnas[:-1]
            query = 'insert into ' + tabla + '(' + stringColumnas + ') values (' + stringValores +');'
            #print(query)
            cursor.execute(query)
            self.conn.commit()
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
            #print(query)
            cursor.execute(query)
            self.conn.commit()
            cursor.close()
            return
        except Error as e:
            print(e)

    def update(self, tabla: str, setData: str, condicion: str = None):
        try:
            cursor = self.conn.cursor()
            if condicion is None:
                query = 'UPDATE ' + tabla + ' SET ' + setData + ';'
            else:
                query = 'UPDATE ' + tabla + ' SET ' + setData + ' WHERE ' + condicion + ';'
            #print(query)
            cursor.execute(query)
            self.conn.commit()
            cursor.close()
        except Error as e:
            print(e)

    def describe(self, tabla: str):
        try:
            cursor = self.conn.cursor()
            query = 'describe ' + tabla + ';'
            #print('El select es: ',self.query)
            cursor.execute(query)
            myresult = cursor.fetchall()
            cursor.close()
            return myresult
        except Error as e:
            print(e)

if __name__ == '__main__':
    bd = BD()
    print("Me he conectado")
    #abc = bd.select('*','usuario','nombre = \'Rafael\'')
    #print(abc)
    abc = bd.select('*','usuario')
    #bd.insert(['rol1', 'descripcion1', False, 8], 'rol')
    #bd.delete('usuario', 'nombre = \'Rafael\'')
    print(abc)
