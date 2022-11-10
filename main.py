
from adat import *
# from kosar import *
from rendeles import *


name = input('Üdv a KKFood-ban! Kérjük adja meg felhasználónevét: ')
if nameLogingIn(name) == False:
    nameRegister()
elif nameLogingIn(name) == True:
    menu()
input('-------------------------------------------\nKérem válasszon az alábbi opciók közül!: \n\tHelybenfogyasztás(elhozom) \n\tElvitel(itthon eszem meg)\n------------------------------------------- \t\n\nA választásom: ')