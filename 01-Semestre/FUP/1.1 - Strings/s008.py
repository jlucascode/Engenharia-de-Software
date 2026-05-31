#Faça um programa em que troque todas as ocorrências de uma letra L1 pela letra L2 em uma string. A string e as letras L1 e L2 devem ser fornecidas pelo usuário.
frase = input()
L1 = input()
L2 = input()

frase_modificada = frase.replace(L1, L2)

print(frase_modificada)