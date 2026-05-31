#Implemente um programa que leia o nome, a idade e o endereço de uma pessoa e armazene os dados em um dicionário. Imprima o dicionário.
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
endereco = input("Digite o endereço: ")
pessoa = {
    "nome": nome,
    "idade": idade,
    "endereco": endereco
}
print(pessoa)