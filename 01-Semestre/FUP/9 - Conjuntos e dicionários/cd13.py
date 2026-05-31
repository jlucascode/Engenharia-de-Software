def validar_data(data):
    partes = data.split("/")
    if len(partes) != 3:
        return False
    dia, mes, ano = partes
    if not (dia.isdigit() and mes.isdigit() and ano.isdigit()):
        return False
    d = int(dia)
    m = int(mes)
    return d >= 1 and d <= 31 and m >= 1 and m <= 12

def validar_cep(cep):
    return len(cep) == 10 and cep[2] == "." and cep[6] == "-" and cep.replace(".", "").replace("-", "").isdigit()

def validar_email(email):
    if email.count("@") != 1 or "." not in email:
        return False
    usuario, dominio = email.split("@")
    return usuario != "" and dominio != "" and dominio[0] != "." and dominio[-1] != "."

pessoa = {
    "nome": input(),
    "endereco": input(),
    "nascimento": input(),
    "cidade": input(),
    "cep": input(),
    "email": input()
}

if not validar_data(pessoa["nascimento"]):
    print("Data errada")
elif not validar_cep(pessoa["cep"]):
    print("CEP errado")
elif not validar_email(pessoa["email"]):
    print("E-mail errado")
else:
    print(pessoa)