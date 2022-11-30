
def rendelesek():
    file = open('rendeles.csv','r', encoding='utf-8')
    # file.readline()
    for row in file:
        splittedData = row.split(';')
        print('\n' + splittedData[0] + ' \t' + splittedData[1] + '\t' + splittedData[2] + '\t' + splittedData[3])
    file.close()
