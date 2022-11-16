
def logingIn(name,phoneNummber):
    file = open('adat.csv','r',encoding='utf-8')
    for row in file:
        splittedData = row.split(';')
        if splittedData[1] == name and splittedData[4] == phoneNummber:
            pass
        else:
            print('Ön nem regisztrált felhasználó!')
            pass 
    file.close()

def dataRegister(name, dataOfBirth, city, phoneNummber):
    file = open('adat.csv', 'a', encoding='utf-8')
    for row in file:
        splittedData = row.split(';')

    file.close()

def menu():
    pass