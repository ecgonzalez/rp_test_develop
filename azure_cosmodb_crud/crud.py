
Conversación abierta; 1 mensaje no leído

Ir al contenido
Cómo usar Gmail con lectores de pantalla
1 de 2,580
crud
Recibidos
	x
Edward Gonzalez
	
Archivos adjuntos22:10 (Hace 27 minutos.)
	
para mí
   
Traducir mensaje
Desactivar para: inglés
crud
Área de archivos adjuntos
	
	
	

import config
import argparse

class inicio():
	def menu(self):
		# First Optional Argument
		self.ANALIZER.add_argument(
		  "-",
		  "--aviso",
		  help="",
		  #type=int
		)
		
		if argumento.aviso:
		  print("Argumento opcional solicitado: --aviso")
		  for x in range(0, argumento.aviso):
		    print("Argumento acompañado de:"+str(argumento.aviso))
		else:
		  print("Ningún argumento solicitado")
	def create_collection(self,CLIENT,ID_DB,):
		self.DB = self.CLIENT.ReadDatabase(self.DATABASE)
	def create_db(self,CLIENT,ID_DB):
		self.DB = self.CLIENT.CreateDatabase({'id': ID_DB})

	def __init__(self):
		#menu Analizer
		self.ANALIZER = argparse.ArgumentParser(description='CRUD AZURE-COSMOS_DB PROCESS')
		#menu Argument
		self.ARGUMENT = analizador.parse_args()
		#Cosmo DB variables
		self.ID_DATABASE = 'test_osha_extraction'
		self.ID_COLLECTION = 'test900'
		self.DATABASE = 'dbs/'+str(ID_DATABASE)
		self.COLLECTION = database_link + '/colls/' + ID_COLLECTION
		self.CLIENT = document_client.DocumentClient(ENDPOINT, {'masterKey': MASTERKEY})
		self.DB = ""

if __name__ == '__main__':
	inicio()

crud.py
Mostrando crud.py
