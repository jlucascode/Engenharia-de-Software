def funcao(string1, string2):
    if len(string1) != len(string2):
        return False

    tamanho = len(string1)
    for i in range(tamanho):
        if string1[i] != string2[i]:
            return False
    return True