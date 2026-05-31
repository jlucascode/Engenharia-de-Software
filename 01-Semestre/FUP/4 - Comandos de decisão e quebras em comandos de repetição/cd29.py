numero = int(input())
e_primo = True

if numero <= 1:
    e_primo = False

for i in range(2, numero):

    if numero % i == 0:
        e_primo = False
        break

if e_primo == True:
    print("Primo")
else:
    print("Nao primo")