import secrets
import string

#Definindo caracteres possíveis
caracteres = string.ascii_letters + string.digits + string.punctuation

#Senha de 12 caracteres
senha = ''.join(secrets.choice(caracteres) for i in range(12))

print("Senha gerada:", senha)

#import string
#import random
#print('Password: ', ''.join(random.choice(string.ascii_letters + string.digits) for _ in range (8)))