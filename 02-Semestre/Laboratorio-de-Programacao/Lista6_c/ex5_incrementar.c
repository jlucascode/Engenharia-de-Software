#include <stdio.h>

void incrementar(int *num) {
    (*num)++;
}

int main() {
    int n;
    printf("Digite um numero inteiro: ");
    scanf("%d", &n);
    printf("Antes: %d\n", n);
    incrementar(&n);
    printf("Depois: %d\n", n);
    return 0;
}
