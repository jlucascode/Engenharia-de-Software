#include <stdio.h>

void calcular(int a, int b, int *soma, int *mult) {
    *soma = a + b;
    *mult = a * b;
}

int main() {
    int x, y, s, m;
    printf("Digite dois numeros inteiros: ");
    scanf("%d %d", &x, &y);
    calcular(x, y, &s, &m);
    printf("Soma: %d\nMultiplicacao: %d\n", s, m);
    return 0;
}
