#include <stdio.h>

int eh_par(int *num) {
    return (*num % 2 == 0) ? 1 : 0;
}

int main() {
    int n;
    printf("Digite um numero inteiro: ");
    scanf("%d", &n);
    if (eh_par(&n))
        printf("Par\n");
    else
        printf("Impar\n");
    return 0;
}
