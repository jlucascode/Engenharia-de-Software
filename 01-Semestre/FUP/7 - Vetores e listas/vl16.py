def funcao(X):
    vetor = []
    for i in range(10):
        repete = False

        for j in range(0, 10):
            if i != j and X[i] == X[j]:
                repete = True
        if not repete:
            vetor.append(X[i])
    return vetor