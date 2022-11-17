def etlap():
    print('Válasszon az alábbiak közül:')
    print('1 - Levesek')
    print('2 - Főételek')
    print('3 - Tészták')
    print('4 - Pizzák')
    print('5- Desszertek')
    print('6 - Menük')
    v = input('Kérem adja meg: ')
    if v == 1:
        file = open('etlap.csv','r',encoding='utf-8')
        for row in file:
            splittedData = row.split(';')
            if splittedData[2] == 'Levesek':
                print(splittedData[0] + f'{splittedData[1]},-Ft')

    if v == 2:
        file = open('etlap.csv','r',encoding='utf-8')
        for row in file:
            splittedData = row.split(';')
            if splittedData[2] == 'Főételek':
                print(splittedData[0] + f'{splittedData[1]},-Ft')
    if v == 3:
        file = open('etlap.csv','r',encoding='utf-8')
        for row in file:
            splittedData = row.split(';')
            if splittedData[2] == 'Tészták':
                print(splittedData[0] + f'{splittedData[1]},-Ft')
    
    if v == 4:
        file = open('etlap.csv','r',encoding='utf-8')
        for row in file:
            splittedData = row.split(';')
            if splittedData[2] == 'Pizzák':
                print(splittedData[0] + f'{splittedData[1]},-Ft')

    if v == 5:
        file = open('etlap.csv','r',encoding='utf-8')
        for row in file:
            splittedData = row.split(';')
            if splittedData[2] == 'Desszertek':
                print(splittedData[0] + f'{splittedData[1]},-Ft')

    if v == 6:
        file = open('etlap.csv','r',encoding='utf-8')
        for row in file:
            splittedData = row.split(';')
            if splittedData[2] == 'Menük':
                print(splittedData[0] + f'{splittedData[1]},-Ft')