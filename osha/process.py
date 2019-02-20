#https://www.osha.gov/pls/imis/establishment.html

import requests
from bs4 import BeautifulSoup
import os
import psycopg2
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from time import sleep
import re
import hashlib
import threading
import json

class inicio():
	def extractextra(self,itemll):
		with open('activities.json', 'r') as filer:
			objextra = json.load(filer)
		valit = str(objextra['name'])
		linkitemm = objextra['activities']

		if str(valit) == str(itemll):
			print("runing process console intern")
			for ittt in linkitemm:
				print("ARRAY ___________________________________________________________"+str(ittt))
	def extract(self,item, nnum,obj,doc,itobj):
		browser = webdriver.Chrome()
		gralcount = 0
		objetlistint = 0
		browser.get('https://www.osha.gov/pls/imis/establishment.html')
		esta1 = browser.find_element_by_xpath('//*[@id="estab_search"]/div[3]/div/select')
		esta = Select(browser.find_element_by_xpath('//*[@id="estab_search"]/div[3]/div/select'))
		esta.select_by_value(item)
		
		browser.implicitly_wait(15)
		nameesta = esta1.get_attribute('value')
		print("????????????????????????"+str(nameesta))
		if nnum == 1:
			self.fin1 = False
		if nnum == 2:
			self.fin2 = False
		if nnum == 3:
			self.fin3 = False
		if nnum == 4:
			self.fin4 = False
		
		select2 = browser.find_element_by_xpath('//*[@id="estab_search"]/div[6]/div/label[2]/input')
		select2.click()
		submit = browser.find_element_by_xpath('//*[@id="estab_search"]/div[10]/div/button[1]')
		submit.click()
		browser.implicitly_wait(15)
		dataint = {}
		valres = True
		try:
			#aa = browser.find_element_by_xpath('//*[@id="maincontain"]/div/div[4]/table/tbody/tr[1]/td[3]/a')
			#alink = aa.get_attribute('href')
			#print("LINK"+str(alink))
			spags = browser.find_element_by_xpath('//*[@id="maincontain"]/div/div[2]/div[2]/div')
			tspags = spags.text
			tspagss = str(tspags).replace("Results 1 - 20 of","")
			tspagss = str(tspagss).strip()
			itspags = 0
			itspags = int(tspagss)/20
			litspags = str(itspags).split(".")
			lenlistpags = int(len(litspags))
			if lenlistpags != 0:
				itspags = int(litspags[0])
			else:
				itspags = int(itspags)
			iitspags = 0
			iitspags = int(tspagss)%20
			if iitspags == 0:
				itspags -= 1
			listalinks = []

			print("pags "+str(tspagss))
			print("pags mod "+str(iitspags))
			print("pags dov "+str(itspags))
			try:
				obj['results_int'] = str(tspagss)
				obj['name']= str(item)
				obj['verresult']= True
				obj['activities'] = []
				obj['results_insert'] = ""
				print(str(obj))
				obj1 = {}
				valinobj1  = ""
				with open(doc, 'r') as filerin1:
					obj1 = json.load(filerin1)

				with open(doc, 'w') as filewin1:
					obj1['offices'].append(obj)
					json.dump(obj1, filewin1,indent=5)
			except Exception as errins:
				print("Error json :")
			try:
				for itera in range(1,int(itspags)):
					print("_____________________________________________________PAGS")
					print("Iterando pag: "+str(itera))
					ac = browser.find_element_by_xpath('//*[@id="maincontain"]/div/div[2]/div[3]')
					acc = ac.find_elements_by_tag_name('a')
					objetlistint = int(int(item)-2)
					acarray = []
					for itarray1 in acc:
						acarray.append(itarray1)
					objurllist = acarray[-1] 
					ulrefpags = acarray[-1].get_attribute('href')
					print("LINK: "+str(ulrefpags)+str(acarray[-1].text))
					print("LLLLL"+str(acarray))
					ab = browser.find_element_by_xpath('//*[@id="maincontain"]/div/div[4]/table/tbody')
					aslink = ab.find_elements_by_tag_name('tr')
					
					conitins = 0
					for itaslink in aslink:
						itlink = itaslink.find_elements_by_tag_name('td')
						tdlinkit = itlink[2]
						aitlink = tdlinkit.find_element_by_tag_name('a')
						rlinks = aitlink.get_attribute('href')
						print(rlinks)
						listalinks.append(str(rlinks))
						conitins += 1
						itobj += 1
						gralcount += 1
						objfin = {}
						objfin1 = {
							"offices":[

							]

						}
						valinobj  = ""
						#obj['activities'].append(str(rlinks))
						with open(doc, 'r') as filerin:
							objfin = json.load(filerin)
						for iteobjin in objfin['offices']:
							valinobj = iteobjin['name']
							if str(valinobj) == str(item):
								iteobjin['activities'] = listalinks
								iteobjin['results_insert'] = str(itobj)
								with open(doc, 'w') as filewin:
									objfin1['offices'].append(iteobjin)
									json.dump(objfin1, filewin,indent=5)
					objurllist.click()
					print("Siguiente pag....."+str(itera)+" | HILO | "+str(nnum)+"| OBJETO |"+str(item))
					

				browser.quit()
				if nnum == 1:
					self.fin1 = True
				if nnum == 2:
					self.fin2 = True
				if nnum == 3:
					self.fin3 = True
				if nnum == 4:
					self.fin4 = True
				print("______________________________________________")
				print("Fin Hilo "+str(nnum)+" |Objeto: "+str(item))
			except Exception as ecxint:
				print("Error interno Funcion Extract :"+str(ecxint))

			#res = requests.get(str(alink))
			#bsobjeto = BeautifulSoup(res.text, 'html.parser')
			#objins = bsobjeto.find('div',{'id':'maincontain'})
			#div1 =objins.find_all('div')
			#divu = div1[0]
			#div2 =divu.find_all('div')
			#divd = div1[1]
			#tablef = divu.find_all('table')
			#trs = tablef[2].find_all('tr')
			#print(str(trs))
		except Exception as excext:
			#print("No hay resultados"+str(excext))
			print("Fin Hilo "+str(nnum)+" |Objeto: "+str(item)+" | Sin Resultados")
			obj2 = {}
			obj2['results_int'] = str("0")
			obj2['name']= str(item)
			obj2['verresult']= False
			obj2['activities'] = []
			obj2['results_insert'] = "0"
			print(str(obj2))
			with open(doc, 'r') as filero:
				objfie = json.load(filero)
			with open(doc, 'w') as filewio:
				objfie['offices'].append(obj2)
				json.dump(objfie, filewio,indent=5)
				




	def __init__(self):
		self.hilo1val = False
		self.hilo2val = False
		self.hilo3val = False
		self.hilo4val = False
		listate = ["1050210","213100","625100","317900","950615","1032100","521100","950411","950412","418100","418200","111100","521400","625400","213400","950647","316100","112900",
	"625700","215600","1032300","830100","418300","830300","1032500","111500","213600","950600","316400","524200","521700","950654","522000","522300","418500","522500","111700",
	"150900","626000","950681","626300","830500","728100","316120","523900","627500","627410","830600","336000","524530","636900","950613","419000","950612","950625","418800",
	"934000","934010","316700","112000","214500","951510","950661","950662","936300","626600","626700","551702","551701","551800","523100","751910","419400","419700","728500",
	"452110","950667","950665","522900","936500","627100","950635","214700","950641","627400","627510","523300","152300","215000","213900","352400","352460","352450","352440",
	"352430","352420","352410","552600","552651","552652","570100","523400","523700","552700","729710","418600","950624","950644","453730","453710","453720","253400","253410",
	"253420","953220","953210","253600","253620","253690","253680","253670","253660","253650","253610","253630","253640","420100","953200","653510","316300","134000","453700",
	"1054195","1054115","1054194","1054119","1054114","1054196","1054116","1054112","1054191","1054192","1054111","1054190","1054118","1054199","1054100","1054113","1054193",
	"936100","950614","570110","627700","728900","257210","257220","257230","257200","257240","257250","257260","214200","524500","317000","936400","317500","1032700","950673",
	"950671","950674","950672","112300","215300","420300","950623","100000","1000000","200000","300000","400000","500000","600000","700000","800000","900000","950621","950651",
	"830700","625500","625410","950633","950653","936200","950632","935000","950611","950631","418400","830400","111400","454510","454520","112600","729300","215800","454723",
	"454733","454713","454726","454716","454725","454735","454715","454736","454724","454734","454714","454721","454731","454711","454722","454732","454712","420600","216000",
	"454700","524700","854910","355110","355117","355125","355114","355124","355112","355121","355111","355123","355118","355122","355116","355115","257800","257810","257820",
	"950643","950652","155010","355100","355126","1055310","1055320","1055360","1055330","1055340","1055370","1055380","1055350","1055300","729700","317700","317300","570120","855610"]
		self.userdbr = os.environ['USERRISKD']
		self.hostdbr = os.environ['HOSTRISKD']
		self.portbdr = os.environ['PORTRISKD']
		self.passdbr = os.environ['PSERISKD']
		self.baser = os.environ['BDRISKD']
		self.userdbl = os.environ['LOCALU']
		self.hostdbl = os.environ['LOCALH']
		self.portbdl = os.environ['LOCALP']
		self.passdbl = os.environ['LOCALC']
		self.basel = os.environ['LOCALD']
		self.fin1 = False
		self.fin2 = False
		self.fin3 = False
		self.fin4 = False
		self.ccone = "RISK"
		print("2222")
		if self.ccone == "RISK": 
			try:
				self.con = psycopg2.connect("dbname="+self.baser+" user="+self.userdbr+" host="+self.hostdbr+" password="+self.passdbr+"")
				print("DB Amazon Risk Connection")
			except:
				#print("Conexion:"+str(con))
				print("Unable to connect to the Amazon database")
				quit()
		else:
			if self.ccone == "LOCAL": 
				try:
					self.con = psycopg2.connect("dbname="+self.basel+" user="+self.userdbl+" host="+self.hostdbl+" password="+self.passdbl+"")
					print("DB LocalHost Connection")
				except:
					#print("Conexion:"+str(con))
					print("Unable to connect to LocalHost database")
					quit()
			else:
				print("No se configuro conexion")

		contadortt = 0
		for iteml in listate:
			contadortt += 1
			if contadortt <= 4:
				print(str(iteml))
				if contadortt ==1:
					obj1 = {
					'results_int': "",
					'name': "",
					'verresult': True,
					'activities': [],
					'results_insert' : ""}
					itobj1 = 0
					hilo1 = threading.Thread(target=self.extract,args=(iteml,contadortt,obj1,'activitiesthread1.json',itobj1,))
					print("Arrancando Hilo 1")
					obj11 = str(iteml)
						
				if contadortt ==2:
					obj2 = {
					'results_int': "",
					'name': "",
					'verresult': True,
					'activities': [],
					'results_insert' : ""}
					itobj2 = 0
					hilo2 = threading.Thread(target=self.extract, args=(iteml,contadortt,obj2,'activitiesthread2.json',itobj2,))
					print("Arrancando Hilo 2")
					obj21 = str(iteml)	
					
				if contadortt ==3:
					obj3 = {
					'results_int': "",
					'name': "",
					'verresult': True,
					'activities': [],
					'results_insert' : ""}
					itobj3 = 0
					hilo3 = threading.Thread(target=self.extract, args=(iteml,contadortt,obj3,'activitiesthread3.json',itobj3,))
					print("Arrancando Hilo 3")
					obj31 = str(iteml)	
					
					
				if contadortt ==4:
					obj4 = {
					'results_int': "",
					'name': "",
					'verresult': True,
					'activities': [],
					'results_insert' : ""}
					itobj4 = 0
					hilo4 = threading.Thread(target=self.extract, args=(iteml,contadortt,obj4,'activitiesthread4.json',itobj4,))
					print("Arrancando Hilo 4")
					obj41 = str(iteml)	
					hilo1.start()
					hilo2.start()
					hilo3.start()
					hilo4.start()
					hilo1.join()
					hilo1in = threading.Thread(target=self.extractextra, args=(obj11,))
					hilo2.join()
					hilo2in = threading.Thread(target=self.extractextra, args=(obj21,))
					hilo3.join()
					hilo3in = threading.Thread(target=self.extractextra, args=(obj31,))
					hilo4.join()
					hilo4in = threading.Thread(target=self.extractextra, args=(obj41,))
					contadortt = 0


				
				#valialive = hilo1.is_alive()
				#if valialive == True:
				#	hilo1.join()
				#valialive2 = hilo2.is_alive()
				#if valialive2 == True:
				#	hilo2.join()
				#valialive3 = hilo3.is_alive()
				#if valialive3 == True:
				#	hilo3.join()
				#valialive4 = hilo4.is_alive()
				#if valialive4 == True:
				#	hilo4.join()
				#contadortt = 0
			#print("Next"+str(pagnext))



if __name__ == '__main__':
	inicio()
