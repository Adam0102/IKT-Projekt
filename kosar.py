from Cart import Cart

fullCart = []


def readCart():
    file = open('kosarak.csv', 'r', encoding = 'utf-8')
    
    for row in file:
        splittedData = row.strip().split(';')
        c = Cart()
        c.name = splittedData[0]
        c.price = int(splittedData[1])
        fullCart.append(c)        
    file.close()

def totalCart():
    total = 0
    for item in fullCart:
        total += item.price
    return total

def printCart():
    print("------ Kosarad ------")
    for item in fullCart:    
        print(f'{item.name} - {item.price} Ft')
    print(f"\nÖsszesen: {totalCart()} Ft") 


readCart()
printCart()


