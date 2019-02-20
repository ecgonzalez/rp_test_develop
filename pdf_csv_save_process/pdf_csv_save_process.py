from tabula import read_pdf
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter,TextConverter,XMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io
import requests
import wget
import csv
import xlrd
import tabula
import json
import re
import time

class inicio():
	def file_reader(self,csvfile):
		contcols = 0
		print(str(csvfile))
		with open(csvfile) as cfile:
			readercsv = csv.reader(cfile)
			lreadercsv = cfile.readlines()
			eleone = lreadercsv[0]
			eleone = str(eleone).replace('\n', '')
			leleone = []
			leleone = str(eleone).split(',')
			print("list element One:\n"+str(leleone))
			print(str(lreadercsv)+"\n 2:"+str(str(readercsv)))
			print(str(type(lreadercsv))+"\n 2:"+str(str(type(readercsv))))
			ifieldscsv = int(len(leleone))
			litems = self.objectj['object']['columns']
			ifields = int(len(self.objectj['object']['columns']))
			ifields = ifields + 1
			emcolumns = []
			ldictobj = []
			dictobj = {}
			litemscols = []
			extract = {}
			objects = {}
			objout = {}
			emcolumns = self.objectj['object']['columns']
			print("Fields Number columns obj 1:\n"+str(ifields-1))
			print("Fields Number columns obj 2:\n"+str(ifieldscsv-2))
			if ifieldscsv == ifields:
				try:
					with open(csvfile) as cfile1:
						readercsv1 = csv.reader(cfile1)
						contcols = 0
						for row in readercsv1:
							if contcols > 0:
								print("333333333333333333"+str(contcols)+"Num "+str(row))
								#litemscols = str(row).split(',')
								contcols1 = 0
								dictobj = {}
								for itemscols in row:
									if contcols1 > 0:
										ckey = str(emcolumns[contcols1-1])
										cvalue = str(itemscols)
										listkeyvalue = {str(ckey):str(cvalue)}
										dictobj.update(listkeyvalue)
										
										print("__________\nKey:"+str(ckey)+"\nValue: "+str(cvalue))
									contcols1 += 1
								#ldictobj.append(dictobj)
								obj2 = {}
								obj2 = {str(contcols):dictobj}
								objects.update(obj2)
								extract.update(objects)
								print("OBJETO "+str(contcols)+str(extract))
							contcols += 1
						documentoutput = r'.\_extract_'+str(self.name_doc)+".json"
						with open(documentoutput, 'w') as fileout:
							objout = {'objects':{}}
							objout['objects']=extract
							print("8888888888888888"+str(objout))
							json.dump(objout, fileout,indent=4)
						print("LISTADO\n"+str(ldictobj))
				except Exception as exgeneratejson:
					print("Error Generte Json Object\n"+str(exgeneratejson))
			else:
				print("Index Does not correspond to the\nnumber of columns in csv File\nVerify")
	def convert_pdf_to_txt(self,skiprows):
		try:
			self.url = str(self.objectj['object']['url'])
			self.list_columns = self.objectj['object']['columns']
			self.name_doc = self.objectj['object']['document_name']
			self.list_skiprows = self.objectj['object']['skiprows']
			print(self.url+"|\n URL\n")
			print(str(self.list_columns)+"|\n COLUMNS\n")
			print(self.name_doc+"\n Document Name\n")
			print(str(self.list_skiprows)+" \n Skiprows\n")
		except Exception as exobjason:
			print("Json Object Error: "+str(exobjason))
			time.sleep(5)
			quit()
		pdfname = r'.\_download_'+str(self.name_doc)+".pdf"
		filename = wget.download(self.url, out=pdfname)
		iskiprows = int(skiprows)
		rsrcmgr = PDFResourceManager()
		retstr = io.StringIO()
		codec = 'utf-8-sig'
		laparams = LAParams()
		device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
		path_pdf = open(filename,'rb')
		pdfr = read_pdf(path_pdf,
		#guess=False,
		pages='all',
		pandas_options={'skiprows':iskiprows,'header':None}, output_format="csv")
		#headers = ['NAME', 'ADDRESS', 'CITY', 'STATE', 'ZIP', 'PHONE']
		#pdfr.columns = headers
		csvname = r'.\_generate_'+str(self.name_doc)+".csv"
		pdfre = pdfr.to_csv(csvname)
		#pdfre = tabula.convert_into('.\ppp2.xlsx', "output.csv", output_format="csv")
		print("Head Csv File Generate\n"+str(pdfr.head()))
		print("Change Options in Json Object? ")
		print("-y Change options -enter pass ")
		optdocop = input("	Change Json Document Options? >:")
		if optdocop == "-y":
			url = input("	url >:")
			if url != "" and str(url).content('http://'):
				self.objectj['object']['url'] = str(url)
				print("Change Url"+str(self.objectj['object']['url']))
			columns = input("	columns (separate fields with ,) >:")
			lcolumns = []
			lcolumns = str(columns).split(",")
			
			if columns != "":
				self.objectj['object']['columns'] = lcolumns
				print("Change columns"+str(self.objectj['object']['columns']))
			
			document_name = input("	document_name >:")
			if document_name != "":
				self.objectj['object']['document_name'] = str(document_name)
				print("Change document_name"+str(self.objectj['object']['document_name']))
			
			skiprows = input("	skiprows (separate fields with ,) >:")
			lskiprows = []
			lskiprows = str(skiprows).split(",")
			if skiprows != "":
				self.objectj['object']['skiprows'] = lskiprows
				print("Change skiprows"+str(self.objectj['object']['skiprows']))
			doctype = input("	doctype >:")
			if doctype != "":
				self.objectj['object']['doctype'] = str(doctype)
				print("Change doctype"+str(self.objectj['object']['doctype']))
			try:
				with open(self.doc, 'r') as filerin:
					self.objectj_copy = json.load(filerin) 
				with open(self.doc, 'w') as filewin:
					json.dump(self.objectj, filewin,indent=5)
			except Exception as exchangejson:
				print("Error I-O Json file"+str(exchangejson))
				time.sleep(4)
			try:
				with open(self.doc, 'r') as filerin1:
					self.objectj = json.load(filerin1)
					print("NEW OBJECT\nURL: "+str(self.objectj['object']['url']))
					print("COLUMNS: "+str(self.objectj['object']['columns']))
					print("DOCUMENT NAME: "+str(self.objectj['object']['document_name']))
					print("SKIPROWS: "+str(self.objectj['object']['skiprows']))
					print("DOCUMENT_TYPE: "+str(self.objectj['object']['doctype']))
					self.__init__()
			except Exception as exchangejson:
				print("Error I-O Json file"+str(exchangejson))
	def valtype(self,action):
		if self.objectj != {}:
			if action == "view":
				if self.type == "pdf":
					print("PDF View")
					print("COLUMNS: "+str(self.objectj['object']['columns']))
					try:
						self.list_skiprows = self.objectj['object']['skiprows']
						for item_list_skiprows in self.list_skiprows:
							self.convert_pdf_to_txt(item_list_skiprows)
							print("\n FINISH\nProcess.....\n item: "+str(item_list_skiprows))
						self.__init__()
					except Exception as exskiprows:
						print("Convert Pdf To text Function Error\n Error:"+str(exskiprows))
			if action == "generate":
				if self.type == "pdf":
					self.name_doc = str(self.objectj['object']['document_name'])
					print("PDF Generate")
					print("COLUMNS: "+str(self.objectj['object']['columns']))
					csvfile = r'.\_generate_'+str(self.name_doc)+".csv"
					print("pre "+str(csvfile))
					try:
						self.file_reader(csvfile)
						self.__init__()
					except Exception as exskiprows:
						print("File Reader Function Error\n Error:"+str(exskiprows))
		else:
			print("Json Object Empty")
	def __init__(self):
		self.path = ""
		self.name_doc = ""
		self.doc = 'object.json'
		self.action = "view"
		self.objectj = {}
		self.objectj_copy = {}
		self.objectj_new = {"object":{}}
		self.list_skiprows = []
		self.list_columns = []
		self.type = "pdf"
		print("____________________________________________________________")
		print("PDF & CSV Files Extraction Process ")
		print("____________________________________________________________")
		print("")
		print("Options: ")
		print("__________")
		print("__the default Json object is object.json \n-y to change document -Enter pass")
		optdoc = input("	Change Json Document? >:")
		

		if optdoc == "-y":
			optdoci = input("	Json Document Path >:")
			self.doc = str(optdoci)
		print("2222222222222")
		try:
			with open(self.doc, 'r') as fileri:
				self.objectj = json.load(fileri)
			print("URL: "+str(self.objectj['object']['url']))
			print("COLUMNS: "+str(self.objectj['object']['columns']))
			print("DOCUMENT NAME: "+str(self.objectj['object']['document_name']))
			print("SKIPROWS: "+str(self.objectj['object']['skiprows']))
			print("DOCUMENT_TYPE: "+str(self.objectj['object']['doctype']))
			self.type = str(self.objectj['object']['doctype'])

		except Exception as exopen:
			print("Open Json Document \nError|: "+str(exopen))
		print("-v -> View Option process")
		print("-g -> Extract data and generate json objects")
		print("-exit -> Exit to script")
		print("____________________________________________________________")
		opt = input("	Option >:")
		if opt == "-v":
			self.valtype("view")
		if opt == "-g":
			self.valtype("generate")
		if opt == "-exit":
			print("You're exit")
			time.sleep(3)
			exit()
		#url = 'http://www.kdheks.gov/asbestos/download/Kansas_Asbestos_Licensed_Contractors_List.pdf'
		#filename = wget.download(url, out=r'.\doc.pdf')



if __name__ == '__main__':
	inicio()
