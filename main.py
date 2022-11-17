
from adat import *
# from kosar import * 
from rendeles import *
from Drink_essen import * 



name = input('Kérjük, adja meg nevét: ')
phoneNumber = int(input(' Kérjük adja meg telefonszámát is: '))
dataOfBirth = int(input('Adja meg születési dátumát: '))
city = input('Adja meg tartózkodási heylét: ')
dataRegister(name, dataOfBirth, city, phoneNumber)
print(f'Üdv, {name}! Köszöntjük a KKFood-ban!')
valasztas = input('Kérem válasszon az alábbi lehetőségek közül: \n\t1 - Elmegyek érte \n\t2 - Házhoz kérem \nAz ön választása: ')
if valasztas == 1:
    v = input('Kérem válasszon az alábbiak közül: \n\t1 - Étlap \n\t2 - Itallap \n Az ön választása: ')
    if v == 1:  
        print('Az étlap:')
        etlap()
    if v == 2:
        print('Az itallap:')
        itallap()
elif valasztas == 2:
    v = input('Kérem válasszon az alábbiak közül: \n\t1 - Étlap \n\t2 - Itallap \n Az ön választása: ')
    if v == 1:  
        print('Az étlap:')
        etlap()
    if v == 2:
        print('Az itallap:')
        itallap()   

print('Menü:')
print('0- Folytatás')
print('1 - Kosár')
print('2 - Rendeléseim')
print('x - Kilépés')
a = ('Adja meg: ')
if a == 'a':
    v = input('Kérem válasszon az alábbiak közül: \n\t1 - Étlap \n\t2 - Itallap \n Az ön választása: ')
    if v == 'a':  
        print('Az étlap:')
        etlap()
    if v == 'a':
        print('Az itallap:')
        itallap()
if b == 'a':
    kosar()
if c == 'a':
    rendelesek()
if d == 'a':
    print('Köszönjük, hogy nálunk vásárolt!')