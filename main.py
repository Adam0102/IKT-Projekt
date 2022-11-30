
import adat

name = input('Kérjük, adja meg nevét: ')
phoneNumber = input('Kérjük adja meg telefonszámát is: ')
dataOfBirth = input('Adja meg születési dátumát: ')
city = input('Adja meg tartózkodási helyét: ')

adat.logingIn(name, dataOfBirth, city, phoneNumber)
print(f'Üdv, {name}! Köszöntjük a KKFood-ban!')

valasztas = input('Kérem válasszon az alábbi lehetőségek közül: \n\t1 - Elmegyek érte \n\t2 - Házhoz kérem \nAz ön választása: ')
adat.valasztas(valasztas)

adat.menu()
