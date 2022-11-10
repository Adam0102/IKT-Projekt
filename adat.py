from main import *
def nameLogingIn(name):
    f = open('adat.csv','r',encoding='utf-8')
    for row in f:
        splitted = row.split(';')
        if name not in splitted:
            return False
        return True
    f.close()

def nameRegister():
    pass

def menu():
    pass