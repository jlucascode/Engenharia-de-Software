frase = input()
sem_vogais = ""
for letra in frase:

    e_vogal = (letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u' or
               letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U')
    if not e_vogal:
        sem_vogais = sem_vogais + letra

print(sem_vogais)