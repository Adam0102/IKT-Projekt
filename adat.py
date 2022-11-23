
def logingIn(name, dataOfBirth, city, phoneNummber):
    file = open('adat.csv','r',encoding='utf-8')
    for row in file:
        splittedData = row.split(';')
        if splittedData[1] == name and splittedData[4] == phoneNummber:
            return True
        else:
            print('Ön nem regisztrált felhasználó!')
            dataRegister(name, dataOfBirth, city, phoneNummber)
    file.close()

def newIndex():
    file = open('adat.csv', 'r', encoding='utf-8')
    max = 0
    file.readline()
    for row in file:
        splittedData = row.split(';')
        if int(splittedData[0]) > max:
            max = int(splittedData[0])
    return max+1

def dataRegister(name, dataOfBirth, city, phoneNummber):
    file = open('adat.csv', 'a', encoding='utf-8')
    file.write(f'{newIndex()};{name};{dataOfBirth};{city};{phoneNummber}\n')
    print('Sikeresen felvettük adatait')
    file.close()

def menu():
    pass