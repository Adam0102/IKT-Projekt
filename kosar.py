from lists import etlap, itallap
import EatDrink

drinksInCart = []
foodsInCart = []

def addCart(id):
    if id == '0':
        foodsInCart.append(id)
    else:
        drinksInCart.append(id)
    

def removeCart(id):
    
    if id[0] == '0':
        foodsInCart.remove(id)
    else:
        drinksInCart.remove(id)
    f = open('kosarak.csv', 'w', encoding='utf-8')
    for item in drinksInCart:
        f.write(item)
    for item in foodsInCart:
        f.write(item)
    f.close()  

def readCart():
    file = open('kosarak.csv', 'r', encoding = 'utf-8')
    
    for row in file:
        row = row.strip()
        if row[0] == '0':
            foodsInCart.append(row)
        else:
            drinksInCart.append(row)
    file.close()

def totalCart():
    total = 0
    for id in foodsInCart:
        total += etlap[id].ar

    for id in drinksInCart:    
        total += itallap[id].ar
    return total

def keresesEtel(id):
    for etel in etlap:
        if etel.id == id:
            return etel
    return False

def keresesItal(id):
    for ital in itallap:
        if ital.id == id:
            return ital
    return False

def printCart():
    print("------ Kosarad ------")
    print(EatDrink.etlapok)
    # for id in foodsInCart:
    #     etel = keresesEtel(id)
    #     print(f'{id} - {etel.nev} - {etel.ar} Ft')

    # for id in drinksInCart:    
    #     ital = keresesItal(id)
    #     print(f'{id} - {ital.nev} - {ital.ar} Ft')
    # print(f"\nÖsszesen: {totalCart()} Ft") 
    print('Köszönjük, hogy nálunk vásárolt!')


