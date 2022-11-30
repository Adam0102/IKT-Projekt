from lists import etlap, itallap
drinksInCart = []
foodsInCart = []

def addCart(id):
    f = open('kosarak.csv', 'a', encoding='utf-8')
    f.write('\n', id)
    f.close()  

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

def printCart():
    print("------ Kosarad ------")
    for id in foodsInCart:
        print(f'{etlap[id].id} - {etlap[id].nev} - {etlap[id].ar} Ft')

    for id in drinksInCart:    
        print(f'{etlap[id].id} - {itallap[id].nev} - {itallap[id].ar} Ft')
    
    print(f"\nÖsszesen: {totalCart()} Ft") 


readCart()
printCart()


