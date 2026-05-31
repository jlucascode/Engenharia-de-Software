#include <stdio.h>

float menor(float a, float b) {
    if (a < b)
        return a;
    else
        return b;
}

float maior(float a, float b) {
    if (a > b)
        return a;
    else
        return b;
}

int main() {
    float n1, n2;
    printf("Digite dois numeros: ");
    scanf("%f %f", &n1, &n2);
    printf("Menor: %.2f\n", menor(n1, n2));
    printf("Maior: %.2f\n", maior(n1, n2));
    return 0;
}
