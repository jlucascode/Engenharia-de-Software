#include <stdio.h>

int ehNulo(float n) {
    return n == 0;
}

int main() {
    float num;
    printf("Digite um valor: ");
    scanf("%f", &num);
    if (ehNulo(num))
        printf("Nulo\n");
    else
        printf("Nao nulo\n");
    return 0;
}
