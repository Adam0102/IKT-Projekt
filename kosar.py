from kosarak import kosarak

print(f'Kosár tartalma:')

f = open('kosar.csv','r', encoding='utf-8')

kosarak = []

res1 = kosarak()

res1.name = 'Mexikói cheddar sajtkrémleves sajtos pizzafedővel'
res1.type = 'Levesek'
res1.price = '1390'

kosarak.append(res1)

print(res1)
print(res1.name)
print(res1.type)
print(res1.price)

print(f'{res1.name}-{res1.type}-{res1.price}')
