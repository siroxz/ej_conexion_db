#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
'''
Ejemplo de Clase para conexion a base de datos 
'''
import sys
import MySQLdb
import defs

class Consulta_bd:
    '''
        Clase para consultar BD
    '''
    def __init__(self, host, user, passwd, dbase):
    	self._host = host
    	self._user = user
    	self._passwd = passwd
    	self._dbase = dbase
    	self._conn = None

    def conectar(self):
    	'''
    		Conecta a la BD
            True=Conexion exitos
            False=Error en conexion
    	'''
    	try:
    		self._conn=MySQLdb.connect(host=self._host, user=self._user, passwd=self._passwd, db=self._dbase)
    		self._conn.autocommit(True)
    		return True
    	except Exception as e:
    		print(sys.exc_info()[1])
    		return False

    def _verifica_conexion(self):
    	'''
    		Verifica que se haya realizado una conexion a la base de datos
    		retorna True si ya se realizo la conexion
		'''
    	if not self._conn:
    		print("Error. Todavia no se ha conectado a la base de datos %s" % self._dbase)
    		return False
    	return True


    def listar_artist(self):
    	'''
    		Lista tabla Artist
    		retorna True si pudo realizar la operacion exitosamente
    	'''
    	if not self._verifica_conexion():
    		return False
    	
    	exit = False
    	try:
    		cur=self._conn.cursor()
    		cur.execute('SELECT * FROM Artist ORDER BY ArtistId ASC')
    		for rows in cur.fetchall():
    			print(rows)

    		exit = True
    	except Exception as e:
    		print(sys.exc_info()[1])
    		exit = False

    	finally:
    		cur.close()
    	return exit

    def insertar_artist(self,dato):
        if not self._verifica_conexion():
            return False
        exit = False
        
        try:
            cur=self._conn.cursor()
            cur.execute("INSERT INTO Artist (Name) VALUES (%s)",(dato,))


        except Exception as e:
            print(sys.exc_info()[1])
            exit = False

        finally:
            cur.close()
        return exit



if __name__ == '__main__':

	# creo la clase
    bd = Consulta_bd(defs.HOST, defs.USER, defs.PASSWORD, defs.DBASE)

    # hago la conexion
    if bd.conectar():
    	print('Conexion con bd=%s exitosa' %defs.DBASE)
    else:
    	print('Erro conexion con bd=%s' %defs.DBASE)
    	sys.exit()

    print('**********')
    print('1- Listar Artist')
    print('2- Agregar Artist')

    input_var = input('Ingrese opcion:')

    if input_var=='1':
        bd.listar_artist()
    elif input_var=='2':
        name = input('Ingrese nombre de Artista:')
        bd.insertar_artist(name)
    else:
        pass
