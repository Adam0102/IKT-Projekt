from Etlap import Etlap

etlap = []
itallap = []
italtipusok = {}

def openFile():
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
def openFile():
    file = open('itallap.csv','r',encoding='utf-8')
    for row in file:
        splittedData = row.strip().split(';')
        e = Etlap()
        e.id = int(splittedData[0])
        e.nev = splittedData[1]
        e.ar = int(splittedData[2])
        e.tipus = splittedData[3]
        itallap.append(e)
    file.close()
def kategoriaEtelei(kategoria):
    etelek = []
    for e in etlap:
        if e.tipus == kategoria:
            etelek.append(e)
    return etelek

def kategoriaItalai(kategoria):
    italok = []
    for e in itallap:
        if e.tipus == kategoria:
            italok.append(e)
    return italok

def kiiras():
    f = open('italtipusok.csv','r',encoding='utf-8')
    for row in f:
        print(row[0] + row[1])
    f.close()


    
def etlapok():
    print('Válasszon az alábbiak közül:')
    print('1 - Levesek')
    print('2 - Főételek')
    print('3 - Tészták')
    print('4 - Pizzák')
    print('5- Desszertek')
    print('6 - Menük')
    v = int(input('Kérem adja meg: '))
    if v == 1:
        levesek = kategoriaEtelei('Levesek')
        for leves in levesek:
            print(leves.id + leves.nev + f'{leves.ar},-Ft')    
    if v == 2:
        foetelek = kategoriaEtelei('Főételek')
        for foetel in foetelek:
            print(foetel.id + foetel.nev + f'{foetel.ar},-Ft')       
    if v == 3:
        tesztak = kategoriaEtelei('Tészták')
        for teszta in tesztak:
            print(teszta.id + teszta.nev + f'{teszta.ar},-Ft') 
    if v == 4:
        pizzak = kategoriaEtelei('Pizzák')
        for pizza in pizzak:
            print(pizza.id + pizza.nev + f'{pizza.ar},-Ft') 

    if v == 5:
        desszertek = kategoriaEtelei('Desszertek')
        for desszert in desszertek:
            print(desszert.id + desszert.nev + f'{desszert.ar},-Ft') 


    if v == 6:
        menük = kategoriaEtelei('Menük')
        for menü in menük:
            print(menü.id + menü.nev + f'{menü.ar},-Ft') 


def italtipusokBeolvas():
    file = open('italtipusok.csv','r')

    for row in file:
        splitted = row.spli(';')
        italtipusok[int(splitted[0])] = splitted[1]
    file.close()


def itallapok():
    print('Válasszon az alábbiak közül:')
    kiiras()


    v = int(input('Kérem válasszon: '))

    for id,tipus in italtipusok.items:
        italok = kategoriaItalai(italtipusok[v])
        for ital in italok:
            print(ital.id + ital.nev + f'{ital.ar},-Ft')   
