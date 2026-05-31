12import secrets
import string


def gerar_senha(tamanho, maiusculas, minusculas, numeros, simbolos):
    caracteres = ""
    if maiusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Selecione pelo menos um tipo de caractere!")

    return "".join(secrets.choice(caracteres) for _ in range(tamanho))


def main():
    print("=== GERADOR DE SENHAS ===\n")

    try:
        tamanho = int(input("Tamanho da senha [16]: ") or "16")
    except ValueError:
        tamanho = 16

    maiusculas = input("Incluir maiúsculas? (A-Z) [S/n]: ").strip().lower() != "n"
    minusculas = input("Incluir minúsculas? (a-z) [S/n]: ").strip().lower() != "n"
    numeros = input("Incluir números? (0-9) [S/n]: ").strip().lower() != "n"
    simbolos = input("Incluir símbolos? (!@#$...) [S/n]: ").strip().lower() != "n"

    try:
        senha = gerar_senha(tamanho, maiusculas, minusculas, numeros, simbolos)
        print(f"\nSenha gerada: {senha}")
    except ValueError as e:
        print(f"\nErro: {e}")


if __name__ == "__main__":
    main()
