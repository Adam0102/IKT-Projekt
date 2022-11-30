
import EatDrink
import kosar
import rendeles
import lists

def logingIn(name, dataOfBirth, city, phoneNummber):
    file = open('adat.csv','r',encoding='utf-8')
    regisztralt = False
    for row in file:
        splittedData = row.strip().split(';')
        if splittedData[1] == name and splittedData[4] == phoneNummber:
            regisztralt = True
            break
    if regisztralt == False:
        print('Ön nem regisztrált felhasználó!')
        dataRegister(name, dataOfBirth, city, phoneNummber)
    file.close()

def newIndex():
    file = open('adat.csv', 'r', encoding='utf-8')
    max = 0
    file.readline()
    for row in file:
        splittedData = row.strip().split(';')
        if int(splittedData[0]) > max:
            max = int(splittedData[0])
    return max+1

def dataRegister(name, dataOfBirth, city, phoneNummber):
    file = open('adat.csv', 'a', encoding='utf-8')
    file.write(f'{newIndex()};{name};{dataOfBirth};{city};{phoneNummber}\n')
    print('Sikeresen felvettük adatait')
    file.close()

def menu():
    print('Menü:')
    print('0- Folytatás')
    print('1 - Kosár')
    print('2 - Rendeléseim')
    print('x - Kilépés')
    menuChoice = input('Mit szeretne csinálni? ')
    while menuChoice != 'x':
        if menuChoice == '0':
            v = input('Kérem válasszon az alábbiak közül: \n\t1 - Étlap \n\t2 - Itallap \n Az ön választása: ')
            if v == '1':  
                print('Az étlap:')
                EatDrink.etlapok()
            if v == 'a':
                print('Az itallap:')
                EatDrink.itallapok()
        elif menuChoice == '1':
            kosar.printCart()
            choice = input('Szeretné változtatni a kosár tartalmát? igen/nem').upper()
            if choice == 'IGEN':
                delete_Add = input('Törölni szeretne valamit?(1 - igen, 2 - nem').upper()
                if delete_Add == '1' or delete_Add =='IGEN':
                    torlendo = int(input('Hányadik ételt akarja törölni?'))
                    id = torlendo - 1
                    kosar.removeCart(id)
                elif delete_Add == '2' or delete_Add == 'NEM':
                    print(lists.etlap())
                    print(lists.itallap())
                    id = int(input('Mit szeretne hozzáadni?'))
                    kosar.addCart(id)
        elif menuChoice == '2':
            rendeles.rendelesek()
    print('Köszönjük, hogy nálunk vásárolt!')   