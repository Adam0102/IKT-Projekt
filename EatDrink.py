from Etlap import Etlap, Itallap
from lists import etlap, itallap
from kosar import addCart

italtipusok = {}
kategoria = ''



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
        print(row[0] + ' - ' + row[1])
    f.close()

def keresesEtel(id):
    for etel in etlap:
        if etel.id == id:
            return etel
    return False

def keresesItal(id):
    for ital in itallap:
        if ital.id == id:
            return ital
    return False
    
def etlapok():
    print('Válasszon az alábbiak közül:')
    print('1 - Levesek')
    print('2 - Főételek')
    print('3 - Tészták')
    print('4 - Pizzák')
    print('5 - Desszertek')
    print('6 - Menük')
    v = int(input('Kérem adja meg: '))
    if v == 1:
        levesek = kategoriaEtelei('Levesek')
        for leves in levesek:
            print(f' {leves.id} {leves.nev} {leves.ar},-Ft')
        id = input('Válasszon az ételek közül: ')
        addCart(id)
    if v == 2:
        foetelek = kategoriaEtelei('Főételek')
        for foetel in foetelek:
            print(f'{foetel.id} {foetel.nev} {foetel.ar},-Ft')
            id = int(input('Válasszon az ételek közül: '))
            addCart(id)       
    if v == 3:
        tesztak = kategoriaEtelei('Tészták')
        for teszta in tesztak:
            print(f'{teszta.id} {teszta.nev} {teszta.ar},-Ft')
            id = int(input('Válasszon az ételek közül: '))
            addCart(id)
    if v == 4:
        pizzak = kategoriaEtelei('Pizzák')
        for pizza in pizzak:
            print(f'{pizza.id} {pizza.nev} {pizza.ar},-Ft')
            id = int(input('Válasszon az ételek közül: '))
            addCart(id) 
    if v == 5:
        desszertek = kategoriaEtelei('Desszertek')
        for desszert in desszertek:
            print(f'{desszert.id} {desszert.nev} {desszert.ar},-Ft')
            id = int(input('Válasszon az ételek közül: '))
            addCart(id) 
    if v == 6:
        menük = kategoriaEtelei('Menük')
        for menü in menük:
            print(f'{menü.id} {menü.nev} {menü.ar},-Ft')
            id = int(input('Válasszon az ételek közül: '))
            addCart(id)


def italtipusokBeolvas():
    file = open('italtipusok.csv','r')

    for row in file:
        splitted = row.spli(';')
        italtipusok[int(splitted[0])] = splitted[1]
    file.close()


def itallapok():
    print('Válasszon az alábbiak közül:')
    kiiras()

    valsztas = int(input('Kérem válasszon: '))

    italok = kategoriaItalai(italtipusok[valsztas])
    for ital in italok:
        print(f'{ital.id} {ital.nev} {ital.ar},-Ft') 
        id = int(input('Válasszon az ételek közül: '))
        addCart(id) 
