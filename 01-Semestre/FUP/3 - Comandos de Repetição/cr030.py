palavrinha = input()
tamanho = 0
for caractere in palavrinha:
    tamanho = tamanho + 1

indice = tamanho - 1

while indice >= 0:
    print(palavrinha[indice], end="")
    indice = indice - 1
print()