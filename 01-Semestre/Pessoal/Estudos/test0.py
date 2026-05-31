# Usando namedexpr_test (:=) e a estrutura if_stmt
if (n := len("Python")) > 5:
    # Usando o ternário da regra 'test'
    status = "Longo" if n > 10 else "Médio"
    print(f"O nome tem tamanho {n} e status: {status}")
