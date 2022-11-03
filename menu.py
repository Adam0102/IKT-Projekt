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
        print('Az étlap:')
        etlap()
    if v == 'itallap'.upper():
        print('Az itallap:')
        itallap()
elif valasztas == 'Elvitel'.upper():
    v = input('Kérem válasszon az alábbiak közül: \n\t Étlap \n\t Itallap \n Az ön választása: ').upper()
    if v == 'Étlap'.upper():  
        print('Az étlap:')
        etlap()
    if v == 'itallap'.upper():
        print('Az itallap:')
        itallap()   

