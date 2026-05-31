#include <stdio.h>

// Versao recursiva
int fatorial_rec(int n) {
    if (n <= 1)
        return 1;
    return n * fatorial_rec(n - 1);
}

// Versao com laco (iterativa)
int fatorial_iter(int n) {
    int resultado = 1;
    for (int i = 2; i <= n; i++) {
        resultado *= i;
    }
    return resultado;
}

int main() {
    int num;

    printf("Digite um numero inteiro nao negativo: ");
    scanf("%d", &num);

    if (num < 0) {
        printf("Fatorial nao definido para numeros negativos.\n");
        return 1;
    }

    printf("Fatorial recursivo de %d: %d\n", num, fatorial_rec(num));
    printf("Fatorial iterativo de %d: %d\n", num, fatorial_iter(num));

    return 0;
}
