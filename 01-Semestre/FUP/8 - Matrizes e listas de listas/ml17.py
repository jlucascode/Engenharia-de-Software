def e_primo(n):
    n_abs = abs(n)

    if n_abs == 0:
        return False

    if n_abs == 1 or n_abs == 2:
        return True

    for d in range(2, n_abs):
        if n_abs % d == 0:
            return False

    return True


def funcao(mat):
    div = []
    for j in range(len(mat[0])):
        menor = mat[0][j]
        primo = 0
        tem_primo = False
        for i in range(len(mat)):
            if menor > mat[i][j]:
                menor = mat[i][j]
            if e_primo(mat[i][j]) == True:
                if tem_primo == False:
                    primo = mat[i][j]
                elif primo < mat[i][j]:
                    primo = mat[i][j]
                tem_primo = True
        if tem_primo:
            div.append(primo)
        else:
            div.append(menor)

    for j in range(len(mat[0])):
        for i in range(len(mat)):
            a = mat[i][j]
            mat[i][j] = mat[i][j] / div[j]
            b = mat[i][j]
    return mat