def itallap():    
    f = open('itallap.csv','r', encoding='utf-8')
    for row in f:
        splitted = row.split(';')
    print(splitted)
    f.close()