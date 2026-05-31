ano = int(input(''))
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print('Bissexto')
else:
    print('Nao bissexto')