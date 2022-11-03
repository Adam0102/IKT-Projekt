def etlap():
    f = open('étlap.csv','r', encoding='utf-8')
    for row in f:
        splitted = row.split(';')
    print(splitted[0], splitted[1],splitted[2])
    f.close()