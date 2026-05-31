#include <stdio.h>

void zerar(int *num) {
    *num = 0;
}

int main() {
    int n;
    printf("Digite um numero inteiro: ");
    scanf("%d", &n);
    zerar(&n);
    printf("Valor apos zerar: %d\n", n);
    return 0;
}
