
import adat
import EatDrink

name = input('Kérjük, adja meg nevét: ')
phoneNumber = input('Kérjük adja meg telefonszámát is: ')
dataOfBirth = input('Adja meg születési dátumát: ')
city = input('Adja meg tartózkodási helyét: ')

adat.logingIn(name, dataOfBirth, city, phoneNumber)
print(f'Üdv, {name}! Köszöntjük a KKFood-ban!')

valasztas = input('Kérem válasszon az alábbi lehetőségek közül: \n\t1 - Elmegyek érte \n\t2 - Házhoz kérem \nAz ön választása: ')
if valasztas == '1':
    v = input('Kérem válasszon az alábbiak közül: \n\t\t1 - Étlap \n\t\t2 - Itallap \nAz ön választása: ')
    if v == '1':  
        print('Az étlap:')
        EatDrink.etlapok()
    if v == '2':
        print('Az itallap:')
        EatDrink.itallapok()
elif valasztas == '2':
    v = input('Kérem válasszon az alábbiak közül: \n\t\t1 - Étlap \n\t\t2 - Itallap \nAz ön választása: ')
    if v == '1':  
        print('Az étlap:')
        EatDrink.etlapok()
    if v == '2':
        print('Az itallap:')
        EatDrink.itallapok()   

adat.menu()
