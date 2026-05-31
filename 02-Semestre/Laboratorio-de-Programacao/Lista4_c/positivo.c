#include <stdio.h>

void verificarPositivo(float n) {
    if (n > 0)
        printf("Positivo\n");
    else if (n < 0)
        printf("Negativo\n");
    else
        printf("Zero (neutro)\n");
}

int main() {
    float num;
    printf("Digite um valor: ");
    scanf("%f", &num);
    verificarPositivo(num);
    return 0;
}
