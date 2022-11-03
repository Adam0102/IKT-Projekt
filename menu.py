from file import *
from itallap import *
from desszertek import *
from etlap import *
from foetelek import *
from kosar import *
from levesek import * 
from menuk import * 
from rendelesek import * 


name = input('Kérjük, adja meg nevét: ')
print(f'Üdv, {name}! Köszöntjük a KKFood-ban!')
valasztas = input('Kérem válasszon az alábbi lehetőségek közül: \n\tHelybenfogyasztás \n\tElvitel \nAz ön választása: ').upper()
if valasztas == 'helybenfogyasztás'.upper():
    v = input('Kérem válasszon az alábbiak közül: \n\t Étlap \n\t Itallap \n Az ön választása: ').upper()
    if v == 'Étlap'.upper():  
        f = open('étlap.csv','r', encoding='utf-8')
        for row in f:
            splitted = row.split(';')
        print(splitted)
        f.close()
    if v == 'itallap'.upper():
        f = open('itallap.csv','r', encoding='utf-8')
        for row in f:
            splitted = row.split(';')
        print(splitted)
        f.close()
elif valasztas == 'Elvitel'.upper():
    pass

