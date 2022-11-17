
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
    file = open('adat.csv', 'w', encoding='utf-8')
    for row in file:
        splittedData = row.split(';')
        splittedData[0] = int(splittedData[0]) + 1 
        if splittedData[1] not in file:
            name.write(file)
        elif splittedData[2] not in file:
            dataOfBirth.write(file)
        elif splittedData[3] not in file:
            city.write(file)
        elif splittedData[4] not in file:
            phoneNummber.write(file)
    print('Sikeresen felvettük adatait')
    file.close()

def menu():
    pass