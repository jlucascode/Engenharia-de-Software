import secrets
senha = secrets.token_urlsafe(8)
print(senha)

import secrets
senha = secrets.token_hex(8)
print(senha)

import secrets
senha = secrets.token_bytes(8)
print(senha)

#senha = number = secrets.randbelow(100)
#print(senha)