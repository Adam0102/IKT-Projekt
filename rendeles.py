def rendelesek():
    file = open('rendeles.csv','r', encoding='utf-8')
    for row in file:
        splittedData = row.split(';')
        print('\n' + splittedData[0] + '  ' + splittedData[1] + '  ' + splittedData[2] + '  ' + splittedData[3])
    file.close()
rendelesek()