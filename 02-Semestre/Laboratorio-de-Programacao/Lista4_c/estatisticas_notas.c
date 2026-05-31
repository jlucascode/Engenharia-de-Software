#include <stdio.h>

int main() {
    float n1, n2, n3;
    float maior, menor, media3, media2;

    printf("Digite as 3 notas: ");
    scanf("%f %f %f", &n1, &n2, &n3);

    media3 = (n1 + n2 + n3) / 3.0;

    maior = n1;
    if (n2 > maior) maior = n2;
    if (n3 > maior) maior = n3;

    menor = n1;
    if (n2 < menor) menor = n2;
    if (n3 < menor) menor = n3;

    media2 = (n1 + n2 + n3 - menor) / 2.0;

    printf("Media das 3 provas: %.2f\n", media3);
    printf("Melhor nota: %.2f\n", maior);
    printf("Pior nota: %.2f\n", menor);
    printf("Media com as 2 melhores: %.2f\n", media2);

    return 0;
}
