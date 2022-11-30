
from Etlap import Etlap, Itallap
from lists import etlap, itallap
from kosar import addCart, removeCart, printCart
import rendeles

italtipusok = {}
kategoria = ''

etelek = []
italok = []

def menu():
    print('Menü:')
    print('0 - Folytatás')
    print('1 - Kosár')
    print('2 - Rendeléseim')
    print('x - Kilépés')
    menuChoice = input('Mit szeretne csinálni? ')
    while menuChoice != 'x':
        if menuChoice == '0':
            v = input('Kérem válasszon az alábbiak közül: \n\t1 - Étlap \n\t2 - Itallap \n Az ön választása: ')
            if v == '1':  
                print('Az étlap:')
                etlapok()
            if v == '2':
                print('Az itallap:')
                itallapok()
        elif menuChoice == '1':
            printCart()
            break
        elif menuChoice == '2':
            rendeles.rendelesek()
        elif menuChoice == 'x':
            print('Köszönjük, hogy nálunk vásárolt!')   


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
        splittedData = row.strip().split(';')
        print(splittedData[0] + ' - ' + splittedData[1])
    f.close()
    
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
        etelek.append(id)
    if v == 2:
        foetelek = kategoriaEtelei('Főételek')
        for foetel in foetelek:
            print(f'{foetel.id} {foetel.nev} {foetel.ar},-Ft')
            id = int(input('Válasszon az ételek közül: '))
            etelek.append(id)       
    if v == 3:
        tesztak = kategoriaEtelei('Tészták')
        for teszta in tesztak:
            print(f'{teszta.id} {teszta.nev} {teszta.ar},-Ft')
            id = int(input('Válasszon az ételek közül: '))
            etelek.append(id)
    if v == 4:
        pizzak = kategoriaEtelei('Pizzák')
        for pizza in pizzak:
            print(f'{pizza.id} {pizza.nev} {pizza.ar},-Ft')
            id = int(input('Válasszon az ételek közül: '))
            etelek.append(id) 
    if v == 5:
        desszertek = kategoriaEtelei('Desszertek')
        for desszert in desszertek:
            print(f'{desszert.id} {desszert.nev} {desszert.ar},-Ft')
            id = int(input('Válasszon az ételek közül: '))
            etelek.append(id) 
    if v == 6:
        menük = kategoriaEtelei('Menük')
        for menü in menük:
            print(f'{menü.id} {menü.nev} {menü.ar},-Ft')
            id = int(input('Válasszon az ételek közül: '))
            etelek.appendCart(id)
    print('Menü:')
    print('0 - Folytatás')
    print('1 - Kosár')
    print('2 - Rendeléseim')
    print('x - Kilépés')
    menuChoice = input('Mit szeretne csinálni? ')
    if menuChoice == '0':
        v = input('Kérem válasszon az alábbiak közül: \n\t1 - Étlap \n\t2 - Itallap \n Az ön választása: ')
        if v == '1':  
            print('Az étlap:')
            etlapok()
        if v == '2':
            print('Az itallap:')
            itallapok()
    elif menuChoice == '1':
        printCart()
    elif menuChoice == '2':
        rendeles.rendelesek()
    else:
        print('Köszönjük, hogy nálunk vásárolt!')


# def italtipusokBeolvas():
#     file = open('italtipusok.csv','r')

#     for row in file:
#         splitted = row.split(';')
#         italtipusok[int(splitted[0])] = splitted[1]
#     file.close()


def itallapok():
    print('Válasszon az alábbiak közül:')
    print('1 - Ásványvizek')
    print('2 - Szénsavas üdítők')
    print('3 - Rostos üdítők')
    print('4 - Házi limonádék')
    print('5 - Sörök')
    print('6 - Röviditalok')
    v = int(input('Kérem adja meg: '))
    if v == 1:
        italok = kategoriaItalai('ásványvízek')
        for ital in italok:
            print(f' {ital.id} {ital.nev} {ital.ar},-Ft')
            id = input('Válasszon az ételek közül: ')
            italok.append(id)
    if v == 2:
        uditok = kategoriaEtelei('szénsavas üdítők')
        for udito in uditok:
            print(f'{udito.id} {udito.nev} {udito.ar},-Ft')
            id = int(input('Válasszon az ételek közül: '))
            italok.append(id)       
    if v == 3:
        rostosok = kategoriaEtelei('rostos üdítők')
        for rostos in rostosok:
            print(f'{rostos.id} {rostos.nev} {rostos.ar},-Ft')
            id = int(input('Válasszon az ételek közül: '))
            italok.append(id)
    if v == 4:
        limonadek = kategoriaEtelei('házi limonádék')
        for limonade in limonadek:
            print(f'{limonade.id} {limonade.nev} {limonade.ar},-Ft')
            id = int(input('Válasszon az ételek közül: '))
            italok.append(id) 
    if v == 5:
        sorok = kategoriaEtelei('csapolt sörök')
        for sor in sorok:
            print(f'{sor.id} {sor.nev} {sor.ar},-Ft')
            id = int(input('Válasszon az ételek közül: '))
            italok.append(id) 
    if v == 6:
        rovidek = kategoriaEtelei('rövid italok')
        for rovid in rovidek:
            print(f'{rovid.id} {rovid.nev} {rovid.ar},-Ft')
            id = int(input('Válasszon az ételek közül: '))
            italok.append(id)
    menu()
    

    valsztas = int(input('Kérem válasszon: '))

    italok = kategoriaItalai(valsztas)
    for ital in italok:
        print(f'{ital.id} {ital.nev} {ital.ar},-Ft') 
        id = int(input('Válasszon az ételek közül: '))
        addCart(id) 
