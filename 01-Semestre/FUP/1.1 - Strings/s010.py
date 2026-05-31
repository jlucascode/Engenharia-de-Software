#Construa um programa que leia duas strings fornecidas pelo usuário e verifique se a segunda string lida está contida no final da primeira, retornando o resultado da verificação.
S1 = input()

S2 = input()

resultado = S1.endswith(S2)
print(resultado)