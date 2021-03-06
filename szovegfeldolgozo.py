"""
PUSKA

A szöveg hossza: len(szoveg)
A szöveg utolsó karater: szoveg[len(szoveg)-1]
Csere a szövegben : szoveg.replace("H", "J") // a nagy "H"-kat nagy "J"-re cserélem
A szöveg tartalmazza az alma karaktereket?: logikaiValtozo = "alma" in szoveg // not in - nem tartalmazza

Ciklus:
ujSzoveg=""
for x in range(0,len(szoveg)-1,2):
	ujSzoveg=ujSzoveg+szoveg[x] 

Eljáras:
def szovegFordit(szöveg):
	...
	return vissza
"""
# Az eljárást készítette:
def szovegFordit(szoveg):
	fordSzoveg=""
	for x in range(len(szoveg)-1,-1,-1):
		fordSzoveg+=szoveg[x]
	return fordSzoveg
	
# Az eljárást készítette:	
def szovegCsere(szoveg):
	maganHango="aáéoöőűúóiíAÁÉOÖŐŰÚÓIÍ"
	for x in range(0,len(maganHango)):
		szoveg=szoveg.replace(maganHango[x],"e");
	return szoveg
	
# Az eljárást készítette:	
def szovegParos(szoveg):
	parosSzoveg = ""
	for x in range(0,len(szoveg),2):
		parosSzoveg += szoveg[x]
	return parosSzoveg
	
# Az eljárást készítette:	
def szovegParatlan(szoveg):
	paratlanSzoveg = ""
	for i in range(1,len(szoveg),2):
		paratlanSzoveg += szoveg[i]
	return paratlanSzoveg
	
# Itt kezdődik a főprogram
for x in range(0,3):
	szoveg=input("Írj be egy szöveget:")
	print(szovegFordit(szoveg))
	print(szovegCsere(szoveg))
	print(szovegParos(szoveg))
	print(szovegParatlan(szoveg))
