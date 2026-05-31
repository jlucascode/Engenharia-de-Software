def somatorio_recursivo(n):
    
    # 1. CASO BASE (Condição de Parada)
    # Se n for 1, o somatório e 1.
    if n == 1:
        return 1
    
    # Caso para garantir que a função lida com numeros negativos ou zero, 
    # embora o enunciado especifique 'inteiro positivo'
    if n <= 0:
        return 0
    
    # 2. PASSO RECURSIVO
    # O somatorio de n e igual a n MAIS o somatorio do numero anterior (n-1).
    # A funcao chama a si mesma com um argumento menor, garantindo que vai convergir para o caso base.
    else:
        return n + somatorio_recursivo(n - 1)

# --- Bloco de Teste ---
try:
    # Leitura do numero inteiro positivo
    numero_limite = int(input("Digite um número inteiro positivo (n): "))
    
    # Chamada da funcao
    if numero_limite > 0:
        resultado = somatorio_recursivo(numero_limite)
        print(f"O somatório de 1 até {numero_limite} é: {resultado}")
    else:
        print("O número deve ser positivo.")

except:
    # Captura de erro simples para entrada nao numerica
    pass