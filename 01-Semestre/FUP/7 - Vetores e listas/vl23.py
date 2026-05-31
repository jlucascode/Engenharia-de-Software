def eh_primo(numero):
    if numero < 0:
        numero = -numero
    if numero <= 1:
        return False

    if numero <= 3:
        return True

    if numero % 2 == 0 or numero % 3 == 0:
        return False

    limite = int(numero ** 0.5)

    for divisor in range(5, limite + 1, 6):
        if numero % divisor == 0 or numero % (divisor + 2) == 0:
            return False
    return True


numeros_entrada = []
TAMANHO = 10

for _ in range(TAMANHO):
    numeros_entrada.append(int(input()))

primos_e_posicoes = []

for indice in range(len(numeros_entrada)):
    valor_atual = numeros_entrada[indice]

    if eh_primo(valor_atual):
        primos_e_posicoes.append(valor_atual)
        primos_e_posicoes.append(indice)

for i in range(0, len(primos_e_posicoes), 2):
    print(primos_e_posicoes[i])
    print(primos_e_posicoes[i + 1])