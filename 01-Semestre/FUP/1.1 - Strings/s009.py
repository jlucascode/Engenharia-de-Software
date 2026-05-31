#Escreva um programa que recebe do usuário uma string S, um caractere C, e uma posição I e devolve o índice da primeira posição da string onde foi encontrado o caractere C. A procura deve começar a partir da posição I.
S = input()
C = input()
I = int(input())

indice_encontrado = S.find(C, I)

print(indice_encontrado)