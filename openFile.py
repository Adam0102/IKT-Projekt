
from Etlap import Etlap, Itallap
from lists import etlap, itallap

def openFileEtlap():
    file = open('etlap.csv','r',encoding='utf-8')
    for row in file:
        splittedData = row.strip().split(';')
        e = Etlap()
        e.id = int(splittedData[0])
        e.nev = splittedData[1]
        e.ar = int(splittedData[2])
        e.tipus = splittedData[3]
        etlap.append(e)
    file.close()

def openFileItallap():
    file = open('itallap.csv','r',encoding='utf-8')
    for row in file:
        splittedData = row.strip().split(';')
        e = Itallap()
        e.id = int(splittedData[0])
        e.nev = splittedData[1]
        e.ar = float(splittedData[2])
        e.tipus = splittedData[3]
        itallap.append(e)
    file.close()