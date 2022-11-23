
import adat
import kosar
import rendeles
# import EatDrink


name = input('Kérjük, adja meg nevét: ')
phoneNumber = int(input('Kérjük adja meg telefonszámát is: '))
dataOfBirth = int(input('Adja meg születési dátumát: '))
city = input('Adja meg tartózkodási heylét: ')

adat.logingIn(name, dataOfBirth, city, phoneNumber)
print(f'Üdv, {name}! Köszöntjük a KKFood-ban!')

valasztas = input('Kérem válasszon az alábbi lehetőségek közül: \n\t1 - Elmegyek érte \n\t2 - Házhoz kérem \nAz ön választása: ')
if valasztas == '1':
    v = input('Kérem válasszon az alábbiak közül: \n\t1 - Étlap \n\t2 - Itallap \n Az ön választása: ')
    if v == '1':  
        print('Az étlap:')
        # etlapok()
    if v == '2':
        print('Az itallap:')
        # itallapok()
elif valasztas == '2':
    v = input('Kérem válasszon az alábbiak közül: \n\t1 - Étlap \n\t2 - Itallap \n Az ön választása: ')
    if v == '1':  
        print('Az étlap:')
        # etlapok()
    if v == '2':
        print('Az itallap:')
        # itallapok()   



print('Menü:')
print('0- Folytatás')
print('1 - Kosár')
print('2 - Rendeléseim')
print('x - Kilépés')
menuChoice = ('Adja meg: ')
while menuChoice != 'x':
    if menuChoice == '0':
        v = input('Kérem válasszon az alábbiak közül: \n\t1 - Étlap \n\t2 - Itallap \n Az ön választása: ')
        if v == '1':  
            print('Az étlap:')
            # etlapok()
        if v == 'a':
            print('Az itallap:')
            # itallapok()
    elif menuChoice == '1':
        pass # kosar()
    elif menuChoice == '2':
        pass # rendelesek()
print('Köszönjük, hogy nálunk vásárolt!')