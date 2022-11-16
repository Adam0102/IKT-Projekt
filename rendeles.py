def rendelesek():
    f = open('rendeles.csv)','r', encoding='utf-8')
    for row in f:
        splittedData = row.split(';')
        print(splittedData[0] + splittedData[1] + splittedData[2] + splittedData[3])
    f.close()