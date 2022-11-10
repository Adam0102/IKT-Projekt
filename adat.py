
def nameLogingIn(name):
    file = open('adat.csv','r',encoding='utf-8')
    for row in file:
        splitted = row.split(';')
        if name not in splitted:
            return False
        return True
    file.close()

def nameRegister(name):
    file = open('adat.csv', 'a', encoding='utf-8')
    for row in file:
        splitted = row.split(';')
        if name not in splitted:
            file.write(name)
        return True
    file.close()

def menu():
    pass