#Leia uma string contendo letras de uma frase, inclusive os espaços em branco. Retirar os espaços em branco e depois escrever a frase resultante.
frase = input()

frase_sem_espacos = frase.replace(" ", "")
print(frase_sem_espacos)
#um forma alternativa print(input().replace(" ", ""))