from adat import *
from kosar import *
from rendeles import *


name = input('Üdv a KKFood-ban! Kérjük adja meg felhasználónevét: ')
nameLogin = nameLogingIn(name)
if nameLogin == False:
    nameRegister()
elif nameLogin == True:
    menu()
