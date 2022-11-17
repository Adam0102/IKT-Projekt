def rendelesek():
    file = open('rendeles.csv','r', encoding='utf-8')
    for row in file:
        splittedData = row.split(';')
        print('\n' + splittedData[0] + '\t' + splittedData[1] + '\t' + splittedData[2])
    file.close()
rendelesek()